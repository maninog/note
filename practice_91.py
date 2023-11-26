import sys
from io import StringIO

# 周期性

# https://atcoder.jp/contests/agc024/tasks/agc024_a
def resolve_01():
    pass

# 判定、最小
# https://atcoder.jp/contests/abc065/tasks/abc065_b
def resolve_02():
#     sys.stdin=StringIO("""3
# 3
# 1
# 2""")
#     sys.stdin=StringIO("""4
# 3
# 4
# 1
# 2""")
    sys.stdin=StringIO("""5
3
3
4
2
4""")
    N=int(input())
    A=[0]*N
    for i in range(0,N):
        A[i]=int(input())

    is_cond=False
    nx=A[0]
    if nx==2: print(1)
    for i in range(0,10**5):
        nx=A[nx-1]
        if nx==2:
            print(i+2)
            is_cond=True
            exit()
    print(-1)

# https://atcoder.jp/contests/abc053/tasks/arc068_a
def resolve_03():
    # sys.stdin=StringIO("""7""")
    # sys.stdin=StringIO("""149696127901""")
    # sys.stdin=StringIO("""10""")
    # sys.stdin=StringIO("""11""")
    sys.stdin=StringIO("""12""")
    x=int(input())
    ans=(x//(6+5))*2
    if 1<=x%(6+5)<=6:
        ans+=1
    elif 7<=x%(6+5)<=10:
        ans+=2
    print(ans)

# https://atcoder.jp/contests/abc165/tasks/abc165_a


# https://atcoder.jp/contests/abc167/tasks/abc167_c
# https://atcoder.jp/contests/abc167/tasks/abc167_d
# https://atcoder.jp/contests/abc174/tasks/abc174_c
# TODO
# 
# 
# 

if __name__ == '__main__':
    resolve_03()

    