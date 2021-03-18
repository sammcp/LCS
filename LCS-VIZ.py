def print_table(D):
    for i in range (0,len(D)):
        print_acc = (str(i) + "        | ")
        for j in range (0,len(D[i])):
                        print_acc = print_acc + (str(D[i][j]) + " | ")
        print(print_acc)

def print_lcs(b,X,i,j):
    if (i == 0) or (j == 0):
        return
    if b[i][j] == 1:
        print_lcs(b,X,(i-1),(j-1))
        print(X[i-1])
    elif b[i][j] == 2:
         print_lcs(b,X,(i-1),(j))
    else:
         print_lcs(b,X,(i),(j-1))

def get_user_input(): 
    print("please input the first string")
    string1 = input()
    print("please input the second string")
    string2 = input()
    return string1, string2

        
        

                        

#X = "ACACGCTAG"
#Y = "CCTATGGCTG"

X,Y = get_user_input()
m = len(X)
n = len(Y)
n2 = n + 1
m1 = m + 1
lcs = [[0 for k in range(n2)] for j in range(m1)]
b = [[0 for k in range(n2)] for j in range(m1)]
#gets lcs and b 
for i in range(1, m1):
    for j in range(1,n2):
        if X[i-1] == Y[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
            b[i][j] = 1
        elif (lcs[i-1][j]) >= (lcs[i][j-1]):
            lcs[i][j] = lcs[i-1][j]
            b[i][j] = 2
        else:
            lcs[i][j] = lcs[i][j-1]
            b[i][j] = 3

print_table(lcs)
print("")
print("------------------------------------------------------")
print("")
print_table(b)
print("")
print_lcs(b,X,m,n)






