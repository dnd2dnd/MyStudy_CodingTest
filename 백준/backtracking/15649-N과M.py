n, m = map(int, input().split())

def back(k, v, list=[]):
    if k==m:
        print(' '.join(map(str, list)))
        return
    for i in range(v, n+1):
        if i not in list:
            list.append(i)
            back(k+1, v+i, list)
            list.pop()

back(0, 1, [])