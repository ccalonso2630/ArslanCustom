from fastapi import FastAPI
from app.generate import generate_image
from pydantic import BaseModel

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(prompt_data: PromptInput):
    image_path = generate_image(prompt_data.prompt)
    return {"image_url": image_path}
