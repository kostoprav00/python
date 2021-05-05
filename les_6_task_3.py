# Вариант 3

from random import randint


def most_common(n: int):
    massive = [randint(0, n) for i in range(n)]
    common_key = massive[0]
    max_occurrence_cnt = 1
    hash_map = dict({common_key: 1})
    for i in range(1, n-1):
        key = massive[i]
        current_key_occurrence_cnt = hash_map.get(key, 0) + 1
        hash_map[key] = current_key_occurrence_cnt
        if current_key_occurrence_cnt > max_occurrence_cnt:
            common_key = key
            max_occurrence_cnt = current_key_occurrence_cnt
    return common_key