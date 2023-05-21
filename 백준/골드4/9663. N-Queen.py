n, m = map(int, input().split())

def back(k, list=[]):
    if k==m:
        print(' '.join(map(str, list)))
        return
    for i in range(1, n+1):
        if i not in list:
            list.append(i)
            back(k+1, list)
            list.pop()

back(0, [])