class EvaluatorAgent:
    def evaluate(self, plans):
        for p in plans:
            score = 100
            score -= p.get("time", 0) * 0.5
            score -= p.get("cost", 0) * 0.3
            if p["weather"]["weather"] == "rainy":
                if "步行" in p["plan"]:
                    score -= 20
            p["score"] = score
        return sorted(plans, key=lambda x: x["score"], reverse=True)
