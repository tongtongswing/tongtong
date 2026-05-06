from openai import OpenAI
import config
client = OpenAI(api_key=config.OPENAI_API_KEY)

class BaseAgent:
    def __init__(self, model=config.MODEL_FAST):
        self.model = model

    def run(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a smart AI agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
