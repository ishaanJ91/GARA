import subprocess
import json
import os
import time
from github import Github
from github.GithubException import RateLimitExceededException

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set. Please set it.")

g = Github(GITHUB_TOKEN)

# Old
# Fetch PRs from two popular repositories

# New
# Fetch pull request data from Elasticsearch and Apache NiFi

def fetch_pr_numbers(repo, merged_since, limit=50):
    cmd = [
        'gh', 'pr', 'list',
        '--repo', repo,
        '--state', 'merged',
        '--search', f'merged:>{merged_since}',
        '--json', 'number,mergedAt',
        '--limit', str(limit)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"GitHub CLI Error: {result.stderr}")
    
    prs = json.loads(result.stdout)
    return [pr["number"] for pr in prs]

def fetch_pr_reviews(repo_name, pr_number):
    repo = g.get_repo(repo_name)
    
    try: 
        pr = repo.get_pull(pr_number)
        
        reviews = pr.get_reviews()
        review_comments = pr.get_review_comments()

        comments = []
        for review in reviews:
            if review.user.type != "Bot" and review.body:
                comments.append({
                    'user': review.user.login,
                    'comment': review.body,
                    'submitted_at': review.submitted_at.isoformat()
                })
                
        for comment in review_comments:
            if comment.user.type != "Bot" and comment.body:
                comments.append(comment.body)

        num_comments = len(comments)
        files = pr.get_files()
        num_files = files.totalCount
        
        return {
            'number': pr.number,
            'diff_url': pr.diff_url,
            'reviews': comments,
            'merged_at': pr.merged_at.isoformat(),
            'num_comments': num_comments,
            'num_files': num_files
        }
    
    except RateLimitExceededException:
        print("Rate limit hit, waiting 60 seconds...")
        time.sleep(60)
        return fetch_pr_reviews(repo_name, pr_number)

def fetch_prs(repo, merged_since, limit=50):
    pr_numbers = fetch_pr_numbers(repo, merged_since, limit)
    pr_data = []
    for pr_num in pr_numbers:
        try:
            pr_info = fetch_pr_reviews(repo, pr_num)
            if pr_info['reviews'] and pr_info['num_comments'] >= 3 and pr_info['num_files'] >= 5:
                pr_data.append(pr_info)
        except Exception as e:
            print(f"Failed to fetch PR #{pr_num}: {e}")
    return pr_data

    

if __name__ == "__main__":
    es_data = fetch_prs("elastic/elasticsearch", "2024-07-30", limit=200)
    nifi_data = fetch_prs("apache/nifi", "2024-07-30", limit=200)

    with open("es_data.json", "w") as f:
        json.dump(es_data, f, indent=2)

    with open("nifi_data.json", "w") as f:
        json.dump(nifi_data, f, indent=2)

    print(f"Fetched {len(es_data)} PRs from elasticsearch and {len(nifi_data)} PRs from nifi.")