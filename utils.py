import typing

def cache(func):
    _cache, _cache_hits,_cache_size  = dict(), [0], [0]
    def wrapper(*args):
        if not all(isinstance(x, typing.Hashable) for x in args):
            non_hashable_arguments = [str(x) for x in args if not isinstance(x, typing.Hashable)]
            raise Exception(f"Non-hashable arguments: {', '.join(non_hashable_arguments)}")

        frozen_args = frozenset(args)
        if frozen_args in _cache.keys():
            _cache_hits[0] += 1
            return _cache[frozen_args]
        
        _cache_size[0] += 1
        return_value = func(*args)
        _cache[frozen_args] = return_value
        return return_value
    
    def get_cache_hits():
        return _cache_hits[0]
    
    def get_cache_size():
        return _cache_size[0]

    wrapper.get_cache_hits = get_cache_hits
    wrapper.get_cache_size = get_cache_size

    return wrapper

def int_list(list_to_int):
    return list(map(int, list_to_int))

def get_valid_neighbors(x, y, array):
    if x > len(array[0]) - 1:
        raise Exception(f"{x} is outside the array of row length {len(array[0])}")
    if y > len(array) - 1:
        raise Exception(f"{y} is outside the array of column length {len(array)}")

    valid_neighbors = []
    potential_neighbors = [(x + 1, y + 1),(x - 1, y - 1),(x + 1, y - 1),(x - 1, y + 1),(x + 1, y),(x - 1, y),(x, y + 1),(x, y - 1)]
    for neighbor in potential_neighbors:
        if neighbor[0] <= -1 or neighbor[1] <= -1 or neighbor[0] >= len(array[0]) or neighbor[1] >= len(array):
            continue
        valid_neighbors.append(neighbor)
    return valid_neighbors