import json
import os
import requests

def load_pr_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def fetch_diff(diff_url):
    headers = {
        'Accept': 'application/vnd.github.v3.diff',
        'Authorization': f"token {os.getenv('GITHUB_TOKEN')}"
    }

    response = requests.get(diff_url, headers=headers)
    if response.status_code == 200:
        return response.text
    else: 
        print(f"Failed to fetch diff from {diff_url}, status {response.status_code}")
        return None
    
def generate_examples(pr_data):
    examples = []
    for pr in pr_data:
        diff = fetch_diff(pr['diff_url'])
        if not diff:
            continue

        for comment in pr['reviews']:
            if isinstance(comment, dict):
                text = comment['comment']
            elif isinstance(comment, str):
                text = comment
            else: 
                continue
            
            if len(text.strip()) < 10:
                continue

            prompt = f"Review this code diff:\n\n{diff.strip()}\n\nComment:"
            completion = f" {text.strip()}"
            examples.append({"prompt": prompt, "completion": completion})
    
    return examples

def is_valid_example(example):
    if not isinstance(example, dict):
        return False
    if 'prompt' not in example or 'completion' not in example:
        return False;
    if not isinstance(example['prompt'], str) or not isinstance(example['completion'], str):
        return False
    if len(example['prompt'].strip()) < 20 or len(example['completion'].strip()) < 10:
        return False
    else :
        return True
    
def validate_jsonl(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    valid, invalid = [], []
    for i, line in enumerate(lines):
        try: 
            obj = json.loads(line)
            if is_valid_example(obj):
                valid.append(obj)
            else:
                invalid.append((i + 1, "Invalid structure or length"))
        except json.JSONDecodeError as e:
            invalid.append((i + 1, f"JSON Error: {str(e)}"))

        print(f"Valid examples: {len(valid)}, \nInvalid examples: {len(invalid)}")
        for lineno, reason in invalid:
            print(f"Line {lineno}: {reason}")

        return valid


def save_jsonl(examples, output_file):
    with open(output_file, 'w') as file:
        for example in examples:
            json.dump(example, file)
            file.write('\n')

if __name__ == "__main__":
    all_data = []
    for path in ["es_data.json", "nifi_data.json"]:
        if os.path.exists(path):
            all_data.extend(load_pr_data(path))
        else:
            print(f"Warning: {path} not found, skipping.")

    examples = generate_examples(all_data)
    save_jsonl(examples, "training_data.jsonl")
    print(f"Saved {len(examples)} examples to training_data.jsonl")