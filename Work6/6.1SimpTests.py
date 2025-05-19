def compute_average(values: list) -> float | str:
    processed = []
    for val in values:
        if isinstance(val, (int, float)):
            processed.append(val)
        else:
            try:
                processed.append(float(val))
            except ValueError:
                return "Bad request"
    return round(sum(processed) / len(processed), 2)


assert compute_average([1, 1, 1]) == 1
assert compute_average([1.5, 2.5, 3.5]) == 2.5
assert compute_average(['1', '2', '3']) == 2
assert compute_average(['a', 'b', 'c']) == "Bad request"
assert compute_average(['a']) == "Bad request"
assert compute_average(['']) == "Bad request"
assert compute_average(['1', '2', 3]) == 2
assert compute_average(['1', '2', 3, 4]) == 2.5
assert compute_average([-1, -1, -1]) == -1
assert compute_average([-1]) == -1
assert compute_average([1.488, 1.488]) == 1.49
assert compute_average([1.555, 1.555]) == 1.55