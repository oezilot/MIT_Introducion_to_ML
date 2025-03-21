# ========= PYTHON BASIC FUNCTIONS ========

# Aufgabe 3.1) Q21
'''
Given two lists of numbers, write a procedure that returns a list of the element-wise sum of the number in those two lists. In the following, no imports should be used.
'''
def add_two_lists(L1, L2):
    summed_list = []
    for index, element in enumerate(L1):
        sum = element + L2[index]
        summed_list.append(sum)
    return summed_list
print(add_two_lists([1, 2, 3], [1, 2, 3]))

'''schönere lösung:
def add_two_lists(a, b):
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i]+b[i])
    return new_list
'''

# Aufgabe 3.1) Q22
'''
Given two column vectors (each represented as a list of numbers), write a procedure dot that returns the (scalar) dot product of two input vectors, each represented as a list of numbers.
'''
def dot(V1, V2):
    sum = 0
    for index in range(len(V1)):
        product = V1[index]*V2[index]
        sum = sum + product
    return sum
print(f"Dot Product of V1 an V2: {dot([1, 2, 3], [1, 2, 3])}")

'''schöne lösung:
def dot(v1, v2):
    scalar = 0
    for i in range(len(v1)):
        scalar += v1[i] * v2[i]  # Accumulate the product of the corresponding elements
    return scalar
'''

# ========= PYTHON FUNCTIONS AS OBJECTS ========

# Aufgabe 3.2) Q23
'''
Write a function add_n that takes a single numeric argument n, and returns a function. The returned function should take a vector v as an argument and return a new vector with the value for n added to each element of vector v. For example, add_n(10)([1, 5, 3]) should return [11, 15, 13].
'''
def add_n(n, V):
    def add(v):
        for index, element in enumerate(v):
            v[index] = element + n
    return add(V)
print(f"add_n: {add_n(2, [1, 2, 3])}")

'''schönere lösung:
'''

# ========= PYTHON ARRAYS AS LISTS OF LISTS ========

# Aufgabe 3.2) Q23
'''
Write a function array_mult that takes two two-dimensional arrays and performs a matrix multiplication, return a new two-dimensional array. Each array should be represented as a list of lists, i.e., as a list of rows, as discussed earlier. For example,
'''
def array_mult(M1, M2):
    # überprüfen ob die liste überhaput mulitpliziert wrden können: jede liste hat gleich viele elemente und die länge der ersten matrix muss der länge einer unterliste der 2ten matrix entprechen
    if len(M1) != len(M2[0]):
        print("Diese beiden Matrizen können nicht multipliziert werden da n1 != m2 ist!")

    M3 = []

    n1 = len(M1)
    m1 = len(M1[0])
    n2 = m1
    m2 = len(M2[0])
    n3 = n1
    m3 = m2

    # statt dass ich durch die beiden inputmatrizen gehe gee ich diurch die resultierende matrix!
    for i in range(n3):
        for ii in range(m3):
            mults = []
            for iii in range(m1): # der range ist so gross wie die anzahl summanden
                mult = M1[i][ii]*M2[ii][i]
            point = sum(mults)



    for index in range(n1):
        M3.append([])
        for index2 in range(m1):
            point = M1[index][index2]*M2[index[index2]]
            M3[index].append(point)


    



# ========= FRAGEN ========
# Q23 -> warum muss man hier eine funktion in einer funktion definieren? oder kann man da mehrere funktionen definieren und verschchtelt aufrufen?