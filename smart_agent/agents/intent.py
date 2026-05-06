from agents.base import BaseAgent
import json

class IntentAgent(BaseAgent):
    def parse(self, user_input):
        prompt = f'''
将用户需求结构化：
输入: {user_input}
输出JSON:
{{"goal": "", "constraints": [], "preferences": []}}
'''
        result = self.run(prompt)
        try:
            return json.loads(result)
        except:
            return {"goal": user_input, "constraints": [], "preferences": []}
