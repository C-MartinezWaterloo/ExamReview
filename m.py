


def calc_fibb(n, mem = {}):


    if n in mem:
        return mem[n]

    if n == 0 or n== 1:
        return 1


    mem[n] = calc_fibb(n-1, mem) + calc_fibb(n-2, mem)


    return mem[n]



def dyn_fibb(n):
    arr = [0] * (n+1)

    arr[0] = 1
    arr[1] = 1
   

    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n]

if __name__ == "__main__":
    print(calc_fibb(2))
    print(dyn_fibb(2))

    











