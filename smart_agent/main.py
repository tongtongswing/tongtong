from agents.intent import IntentAgent
from agents.planner import PlannerAgent
from agents.tool_agent import ToolAgent
from agents.evaluator import EvaluatorAgent
from memory.cache import get_cache, set_cache
import config

def run_system(user_input):
    if config.USE_CACHE:
        cached = get_cache(user_input)
        if cached:
            print("Using cache")
            return cached

    intent_agent = IntentAgent()
    structured = intent_agent.parse(user_input)

    planner = PlannerAgent()
    plans = planner.plan(structured)

    tool_agent = ToolAgent()
    enriched = tool_agent.enrich(plans)

    evaluator = EvaluatorAgent()
    ranked = evaluator.evaluate(enriched)

    if config.USE_CACHE:
        set_cache(user_input, ranked)

    return ranked

if __name__ == "__main__":
    query = input("请输入需求: ")
    result = run_system(query)
    print("\n最优方案：")
    for r in result:
        print(r)
