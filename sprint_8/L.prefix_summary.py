
def solution(s: str):

    p = [0] * len(s)
    j = 0
    i = 1

    while i < len(s):
        if s[j] != s[i]:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
        else:
            p[i] = j + 1
            i += 1
            j += 1

    return p


def input_data():
    s = input().strip()
    return s


if __name__ == '__main__':
    answer = solution(input_data())
    print(' '.join(map(str, answer)))
