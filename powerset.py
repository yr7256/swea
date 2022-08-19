arr = ['A', 'B', 'C']
check = [0, 0, 0]


def powerset(idx):
    if idx == 3:
        print('체크 배열은 다음과 같음 :', *check)
        return

    check[idx] = 0
    powerset(idx+1)

    check[idx] = 1
    powerset(idx+1)


powerset(0)
