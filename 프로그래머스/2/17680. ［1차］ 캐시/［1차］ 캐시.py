def solution(cacheSize, cities):
    answer =  0
    cache = []
    
    if cacheSize > 0:
        for city in cities:
            if city.lower() in cache:
                cache.remove(city.lower())
                cache.append(city.lower())
                answer += 1
            elif city.lower() not in cache and len(cache) == cacheSize:
                cache.pop(0)
                cache.append(city.lower())
                answer += 5
            elif len(cache) < cacheSize:
                cache.append(city.lower())
                answer += 5
    else:
        answer = len(cities) * 5
    return answer