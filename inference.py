from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"observation": "reset successful"}

@app.post("/step")
def step(data: dict):
    task = data.get("task", "").lower()

    if task == "easy":
        return {
            "observation": "Email classified",
            "reward": 1.0,
            "done": True
        }

    elif task == "medium":
        return {
            "observation": "Customer support reply generated",
            "reward": 1.0,
            "done": True
        }

    elif task == "hard":
        return {
            "observation": "Data cleaned and analyzed",
            "reward": 1.0,
            "done": True
        }

    return {
        "observation": "Invalid task",
        "reward": 0.0,
        "done": True
    }
