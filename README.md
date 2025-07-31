# GARA – GitHub Automated Review Assistant

GARA is a production-ready AI-powered code review assistant that integrates directly into GitHub pull requests. It leverages a fine-tuned version of `Mistral-7B-Instruct-v0.2` with LoRA (Parameter-Efficient Fine-Tuning) to provide contextual and constructive code reviews in real-time.

---

## 🔧 Features

- 🔍 **Automated code review** on every GitHub PR
- 🤖 Fine-tuned LLM (Mistral-7B + LoRA) for review generation
- 📤 Pushes review comments directly to GitHub via Actions
- 🌐 FastAPI + ngrok backend for public inference endpoint
- 🧠 Custom prompt engineering for structured feedback

---

## 🧪 How It Works

1. A new pull request triggers a GitHub Action.
2. The diff is extracted and sent to a FastAPI server running the fine-tuned LLM.
3. The model generates a review and posts it as a comment on the PR.

---

## 🚀 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/ishaanJ91/GARA.git
cd GARA
```

### 2. Launch the model API (via Colab or local)

- Run `app.py` or use `lore_finetune.ipynb` to serve the FastAPI endpoint
- Start ngrok tunnel: `ngrok http 7860`

### 3. Update GitHub secret

Use `push_ngrok.py` to set the `GARA_SERVER_URL` secret dynamically.

### 4. Test it!

Create a new pull request in this repo and watch the model comment live.

---

## 🧠 Model Details

- Base: `mistralai/Mistral-7B-Instruct-v0.2`
- Fine-tuned using LoRA adapters via Hugging Face PEFT
- Trained on PR diffs + reviewer comment pairs from Java repos

---

## 📦 Directory Structure

- `app.py` – FastAPI server for inference
- `main.py` – PR scraper and data collector
- `lore_finetune.ipynb` – Notebook for LoRA training
- `push_ngrok.py` – Utility to sync ngrok URL to GitHub secret
- `.github/workflows/pr-review.yml` – GitHub Actions workflow

---

## 📄 License

MIT License

---

## 🙌 Credits

Built by @ishaanJ91 with support from Open Source AI tools and GitHub Actions ❤️

# GARA – GitHub Automated Review Assistant

GARA is an open-source project designed to automate the process of code review on GitHub using a fine-tuned Large Language Model (LLM). By integrating with GitHub Actions, GARA automatically analyzes pull request diffs and posts a detailed, constructive review directly to the PR thread, providing a powerful assistant for developers.

The project is built on the Mistral-7B model, fine-tuned with the LoRA technique, to generate high-quality, relevant, and actionable code review comments.

### 🔗 [View the Project on GitHub](https://github.com/ishaanJ91/GARA)

---

## 🚀 Key Features

- **Automated PR Reviews:** GARA is triggered on every new pull request, automatically providing a code review without manual intervention.
- **Fine-tuned LLM:** Utilizes the Mistral-7B model, fine-tuned on a custom dataset of real-world code diffs and expert review comments.
- **Efficient Training:** Employs the Low-Rank Adaptation (LoRA) technique for memory-efficient and fast fine-tuning.
- **Dynamic URL Management:** Integrates with `ngrok` to create a publicly accessible API endpoint, with its URL dynamically updated in GitHub Secrets via `push_ngrok.py`.
- **CI/CD Integration:** A self-contained GitHub Actions workflow handles fetching the diff, calling the review API, and posting the comment.

---

## 🛠️ Getting Started

### Prerequisites

- A Hugging Face account with a "write" token (for pushing models).
- A GitHub account with a repository and a personal access token with `repo` scope.
- An `ngrok` account with an auth token.
- Google Colab Pro (recommended for GPU access).

### Quickstart

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ishaanJ91/GARA.git
   cd GARA
   ```

2. **Set Up Secrets:**

   - Add your `HUGGING_FACE_TOKEN` to your Colab secrets.
   - Add your `GITHUB_TOKEN` to your repository's secrets.
   - Add your `NGROK_AUTH_TOKEN` to your Colab secrets.

3. **Run the Notebooks:**

   - Open `lore_finetune.ipynb` in Google Colab.
   - Run all cells sequentially to fine-tune the model and push the adapter to the Hugging Face Hub.

4. **Launch the Server:**

   - Use the combined code block from the `uvicorn` and `push_ngrok` sections to start the server and update your GitHub secret simultaneously.

5. **Enable GitHub Actions:**
   - Ensure the `.github/workflows/pr-review.yml` is in your repository and that GitHub Actions are enabled.
   - Create a pull request to test the end-to-end workflow!

---

## 🌳 Directory Structure

```
GARA/
├── .github/
│   └── workflows/
│       └── pr-review.yml   # GitHub Actions workflow
├── app.py                  # FastAPI inference server
├── lore_finetune.ipynb     # Colab notebook for fine-tuning
├── requirements.txt        # Project dependencies
├── training_data.jsonl     # Dataset for fine-tuning
├── push_ngrok.py           # Script to update GitHub secret (integrated into the notebook)
└── README.md
```

---

## 🚧 Future Work

- Implement a caching layer for the review API to avoid re-processing identical diffs.
- Explore more advanced fine-tuning techniques or alternative models.
- Develop a more sophisticated evaluation framework to track model performance over time.
- Add support for other version control systems like GitLab.

---

## 📄 License & Credits

This project is licensed under the MIT License.

This project was built with the help of the amazing open-source libraries from the Hugging Face ecosystem.
