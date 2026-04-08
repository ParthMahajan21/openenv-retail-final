import os
from openai import OpenAI
from env import RetailEnv, Action

client = OpenAI(api_key=os.getenv("HF_TOKEN"))

env = RetailEnv()

def run_task(task):
    obs = env.reset(task)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": obs.text}]
    )

    reply = response.choices[0].message.content

    obs, reward, done, _ = env.step(Action(response=reply))

    print(f"TASK: {task}")
    print(f"AI OUTPUT: {reply}")
    print(f"SCORE: {reward}")
    print("-----------")

for t in ["easy", "medium", "hard"]:
    run_task(t)