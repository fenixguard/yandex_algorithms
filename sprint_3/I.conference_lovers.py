from typing import List, Tuple, NoReturn


def solution(university_ids: List[int], k: int) -> NoReturn:
    conf_stud = dict()
    for un_id in university_ids:
        count = conf_stud.get(un_id)
        if count:
            conf_stud[un_id] += 1
        else:
            conf_stud[un_id] = 1
    result = []
    i = 0
    for item in sorted(conf_stud.items(), key=lambda value: (-value[1], value[0])):
        if i < k:
            result.append(str(item[0]))
            i += 1

    print(" ".join(result))


def input_data() -> Tuple[List[int], int]:
    n = int(input())
    university_ids = list(map(int, input().strip().split()))
    k = int(input())
    return university_ids, k


if __name__ == '__main__':
    solution(*input_data())
