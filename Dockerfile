


# 1. Set the base image — we'll use Python 3.10 as a stable environment:
FROM python:3.10-slim

# 2. Set a working directory inside the container:
WORKDIR /app

# 3. Copy your project files into the container:
COPY . .

# 4. Install dependencies from `requirements.txt`:
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port FastAPI will run on:
EXPOSE 7860

# 6. Define the command to start your FastAPI app with Uvicorn:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]