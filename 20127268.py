n = int(input("Input row: "))
m = int(input("Input col: "))
arr = []

def inputMatrix():
    for i in range(n):
        ar = []
        for j in range(m):
            ar.append(int(input(f"arr[{i}][{j}]: ")))
        arr.append(ar)

def output(arr):
    for i in arr:
        print(i)
    print("")

def check(a):
    for i in a:
        if i != 0:
            return False
    return True

def Gauss_elimination(arr):
    temp = 0
    a, b = 0, 0
    for i in range(m-1):
        if check([arr[x][i] for x in range(temp, n)]):          #kiểm tra vector 0
            continue

        for j in range(temp, n-1):
            if arr[temp][i] == 0:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            a = arr[temp][i]
            b = arr[j + 1][i]
            for k in range(i,m):
                if arr[j + 1][i] == 0 and k == i:
                    break
                arr[j+1][k] = arr[j + 1][k] * a - arr[temp][k] * b
        temp += 1

inputMatrix()                                                   #nhập ma trận
print("--Before using gauss--")
output(arr)                                                     #xuất ma trận
Gauss_elimination(arr)                                          #đưa ma trận về dạng gauss
print("--After using gauss--")
output(arr)


no = [0] * (m-1)                                                #mảng nghiệm có độ dài m - 1
ans = 0
def back_substitution(arr):
    for i in range(n):
        if check(arr[n-1][:m-1]) and (arr[n - 1][m - 1] != 0):  
            return 0
        elif check(arr[n-1][:m-1]) and (arr[n - 1][m - 1] == 0):
            return 1
        ans = arr[n - 1 - i][m - 1]
        for j in range(i):                                       #vòng lặp trừ hết bên trái
            ans -= arr[n - 1 - i][m - 1 - (j + 1)] * no[j]
        no[i] = ans / arr[n - 1 - i][m - 2 - i]                  #nghiệm thứ m - i - 1
    return 2

if back_substitution(arr) == 0:
    print("Phuong trinh vo nghiem")
elif back_substitution(arr) == 1:
    print("Phuong trinh vo so nghiem")
else: 
    print("Phuong trinh co nghiem duy nhat")
    print(f"X = |{no[m - 2]}|")
    for i in range(1,len(no)):
        print(f"    |{no[m - 2 - i]}|")