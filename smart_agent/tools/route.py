def get_route(option):
    if "地铁" in option:
        return {"time": 30, "cost": 4}
    elif "打车" in option:
        return {"time": 20, "cost": 35}
    else:
        return {"time": 40, "cost": 2}
