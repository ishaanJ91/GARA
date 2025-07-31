from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch

app = FastAPI()

# Load base model and LoRA adapter
base = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.2",
    device_map="auto",
    load_in_4bit=True
)
model = PeftModel.from_pretrained(base, "ishaanj91/mistral-code-review-lora")
tokenizer = AutoTokenizer.from_pretrained("ishaanj91/mistral-code-review-lora")

# Define request schema
class ReviewRequest(BaseModel):
    diff: str

@app.post("/review")
def review_code(request: ReviewRequest):
    prompt = f"""You are an expert code reviewer. Here's a code diff from a pull request:
        {request.diff}
        Please write a constructive review summarizing:
        - What the code does
        - What changed
        - How it can be improved (if anything)
        - Whether it follows best practices
    """
    
    print("Prompt used for review:", prompt)

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_new_tokens=300, temperature=0.9)
    review = tokenizer.decode(output[0], skip_special_tokens=True)

    print("Decoded review:", review)
    return {"review": review}