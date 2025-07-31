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

## 🤝 Contributing

### Ways to Contribute

- **🐛 Bug Reports:** Found an issue? Open a GitHub issue with detailed steps to reproduce
- **💡 Feature Requests:** Have an idea for improvement? We'd love to hear it!
- **📝 Documentation:** Help improve our README, add code comments, or create tutorials
- **🔧 Code Contributions:** Submit pull requests for bug fixes or new features
- **🧪 Testing:** Help test new features and report feedback

### Getting Started

1. **Fork the Repository:** Click the "Fork" button on the GitHub page
2. **Create a Branch:** `git checkout -b feature/your-feature-name`
3. **Make Changes:** Implement your improvements with clear, commented code
4. **Test Thoroughly:** Ensure your changes work as expected
5. **Submit a PR:** Open a pull request with a clear description of your changes

### Development Guidelines

- Follow existing code style and conventions
- Add comments for complex logic
- Update documentation if you're changing functionality
- Test your changes before submitting

---


## 📄 License & Credits

This project is licensed under the MIT License.
This project was built with the help of the open-source libraries from the Hugging Face ecosystem.
