def findPosition(a,b,matrix):
    w = 0
    x = 0
    y = 0
    z = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (len(matrix[i][j])==3):
                if (a == 'I' or a == 'J'):
                    w = i
                    x = j
                elif (b == 'I' or b == 'J'):
                    y = i
                    z = j
            else:
                if (matrix[i][j]) == a:
                    w = i
                    x = j
                if (matrix[i][j]) == b:
                    y = i
                    z = j

    return w,x,y,z

def divideString(string):
    arr = [' ' for i in range(len(string)//2)]
    j = 0
    for i in range(len(arr)):
        if (j<len(string)-1):
            arr[i] = string[j] + string[j+1]
            j += 2
    return arr

def createMatrix(cipher):
    matrix = [[' ' for i in range(5)] for j in range(5)]
    temp = list(dict.fromkeys(cipher.upper()))
    k = 0
    n = 0
    m = 0
    for i in range(5):
        m = i
        for j in range(5):
            n = j
            if (k < len(temp)):
                matrix[i][j] = temp[k]
                k += 1
            else:
                break
        if (k >= len(temp)):
            break
    a = 65
    while m<5:
        while n<5:
            if chr(a) not in temp:
                if a == 73:
                    if chr(74) not in temp:
                        matrix[m][n] = 'I/J'
                    else:
                        matrix[m][n] = 'I'
                    a += 2
                    n += 1
                elif a == 74:
                    if chr(73) not in temp:
                        matrix[m][n] = 'I/J'
                    else:
                        matrix[m][n] = 'J'
                    a += 1
                    n += 1
                else:
                    matrix[m][n] = chr(a)
                    n += 1
                    a += 1
            else:
                a += 1
        n = 0
        m += 1

    return matrix
    
def createDiagram(plaintext):
    temp = ''
    for i in plaintext.split():
        temp += i
    if (len(plaintext) %2 !=0):
        temp += 'x'

    diagram = divideString(temp)
    for s in diagram:
        if (s.count(s[0]) ==2):
            s.replace(s[1],'x')
    return diagram

def encrypt(plaintext,cipher):
    ciphertext = ''
    if (len(plaintext) == 0 or len(cipher) == 0):
        return ''
    matrix = createMatrix(cipher)
    diagram = createDiagram(plaintext.upper())
    for s in diagram:
        w,x,y,z = findPosition(s[0],s[1],matrix)
        if(w == y):
            ciphertext += matrix[(w+1)%5][x] + matrix[(y+1)%5][z]
        
        elif(x == z):
            ciphertext += matrix[w][(x+1)%5] + matrix[y][(z+1)%5]

        else:
            ciphertext += matrix[w][z] + matrix[y][x]   

    return ciphertext


def decrypt(ciphertext,cipher):
    plaintext = ''
    if (len(ciphertext) == 0 or len(cipher) == 0):
        return ''
    matrix = createMatrix(cipher)
    diagram = createDiagram(ciphertext.upper())
    for s in diagram:
        w,x,y,z = findPosition(s[0],s[1],matrix)
        if(w == y):
            plaintext += matrix[abs(w-1)%5][x] + matrix[abs(y-1)%5][z]
        
        elif(x == z):
            plaintext += matrix[w][abs(x-1)%5] + matrix[y][abs(z-1)%5]

        else:
            plaintext += matrix[w][z] + matrix[y][x]   

    return plaintext