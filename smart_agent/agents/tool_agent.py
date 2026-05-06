from tools.weather import get_weather
from tools.route import get_route

class ToolAgent:
    def enrich(self, plans):
        weather = get_weather()
        enriched = []
        for p in plans:
            route_info = get_route(p["plan"])
            p["weather"] = weather
            p["time"] = route_info["time"]
            p["cost"] = route_info["cost"]
            enriched.append(p)
        return enriched
