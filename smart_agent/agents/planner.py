from agents.base import BaseAgent
import json

class PlannerAgent(BaseAgent):
    def plan(self, structured_data):
        prompt = f'''
根据需求生成3个方案：
{structured_data}
输出JSON数组：
[{{"plan": "", "cost": "", "time": ""}}]
'''
        result = self.run(prompt)
        try:
            return json.loads(result)
        except:
            return [{"plan": result}]
