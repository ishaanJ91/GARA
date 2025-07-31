from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch, os

app = FastAPI()

base = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.2", device_map="auto", load_in_4bit=True
)
model = PeftModel.from_pretrained(base, "ishaanj91/mistral-code-review-lora")
tokenizer = AutoTokenizer.from_pretrained("ishaanj91/mistral-code-review-lora")

class ReviewRequest(BaseModel):
    diff: str

@app.post("/review")
def review_code(req: ReviewRequest):
    prompt = f"Review this code diff:\n\n{req.diff}"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_new_tokens=300)
    review = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"review": review}