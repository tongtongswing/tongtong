cache = {}
def get_cache(key):
    return cache.get(key, None)
def set_cache(key, value):
    cache[key] = value
