# We will write this code LIVE together at the workshop!
# Keep this file empty for now, see you there!
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

#import MODULE
from database import db
from setup_model import story_generator

#--------------------
#define pydatic model
# POST method
#--------------------

app = FastAPI()

#pydantic model and Field validation
class StoryRequest(BaseModel):
    prompt: str = Field(..., min_length= 5 ,description= "The starting sentence of the story")
    max_length: int = Field(default= 50, ge = 10, le = 100, description= "Length of generated text (10 - 100 texts)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "prompt": "I woke up in a strange room and",
                "max_length": 20
            }
        }
    }

@app.post("/generate-story", status_code= status.HTTP_201_CREATED)
async def generate_story(req: StoryRequest):
    try:
        #b1. retrieve generated text from the model
        ai_output = story_generator(req.prompt, max_new_tokens = req.max_length )
        generated_text = ai_output[0]["generated_text"]
        #b2. prepare data --> db
        data = {
            "input_prompt": req.prompt,
            "length_setting": req.max_length,
            "response": generated_text,
            "status": "success"
        }
        #b3. save into db
        saved_data = db.stories.insert_one(data)
        #b4. return response
        return {
            "message": "sucessfull",
            "data_id": str(saved_data.inserted_id),
            "response": generated_text
        }
    except HTTPException: 
        raise
    except Exception as e:
        raise HTTPException(status_code= 500, detail = f"internal error: {e}")