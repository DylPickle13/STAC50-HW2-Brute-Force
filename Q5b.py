import pandas as pd

binaryStrings = []


def weird_division(n, d):
    return n / d if d else 0


def YMatrix(df):
    Y0_matrix = {
        "Y0=0 L=0 A=0": [weird_division(df[(df.Y0 == 0) & (df.A == 0) & (df.L == 0)].count()[0], df[(df.A == 0) & (df.L == 0)].count()[0])],
        "Y0=0 L=0 A=1": [weird_division(df[(df.Y0 == 0) & (df.A == 1) & (df.L == 0)].count()[0], df[(df.A == 1) & (df.L == 0)].count()[0])],
        "Y0=1 L=0 A=0": [weird_division(df[(df.Y0 == 1) & (df.A == 0) & (df.L == 0)].count()[0], df[(df.A == 0) & (df.L == 0)].count()[0])],
        "Y0=1 L=0 A=1": [weird_division(df[(df.Y0 == 1) & (df.A == 1) & (df.L == 0)].count()[0], df[(df.A == 1) & (df.L == 0)].count()[0])],
        "Y0=0 L=1 A=0": [weird_division(df[(df.Y0 == 0) & (df.A == 0) & (df.L == 1)].count()[0], df[(df.A == 0) & (df.L == 1)].count()[0])],
        "Y0=0 L=1 A=1": [weird_division(df[(df.Y0 == 0) & (df.A == 1) & (df.L == 1)].count()[0], df[(df.A == 1) & (df.L == 1)].count()[0])],
        "Y0=1 L=1 A=0": [weird_division(df[(df.Y0 == 1) & (df.A == 0) & (df.L == 1)].count()[0], df[(df.A == 0) & (df.L == 1)].count()[0])],
        "Y0=1 L=1 A=1": [weird_division(df[(df.Y0 == 1) & (df.A == 1) & (df.L == 1)].count()[0], df[(df.A == 1) & (df.L == 1)].count()[0])]
    }

    Y0_matrix = pd.DataFrame(Y0_matrix)

    Y1_matrix = {
        "Y1=0 L=0 A=0": [weird_division(df[(df.Y1 == 0) & (df.A == 0) & (df.L == 0)].count()[0], df[(df.A == 0) & (df.L == 0)].count()[0])],
        "Y1=0 L=0 A=1": [weird_division(df[(df.Y1 == 0) & (df.A == 1) & (df.L == 0)].count()[0], df[(df.A == 1) & (df.L == 0)].count()[0])],
        "Y1=1 L=0 A=0": [weird_division(df[(df.Y1 == 1) & (df.A == 0) & (df.L == 0)].count()[0], df[(df.A == 0) & (df.L == 0)].count()[0])],
        "Y1=1 L=0 A=1": [weird_division(df[(df.Y1 == 1) & (df.A == 1) & (df.L == 0)].count()[0], df[(df.A == 1) & (df.L == 0)].count()[0])],
        "Y1=0 L=1 A=0": [weird_division(df[(df.Y1 == 0) & (df.A == 0) & (df.L == 1)].count()[0], df[(df.A == 0) & (df.L == 1)].count()[0])],
        "Y1=0 L=1 A=1": [weird_division(df[(df.Y1 == 0) & (df.A == 1) & (df.L == 1)].count()[0], df[(df.A == 1) & (df.L == 1)].count()[0])],
        "Y1=1 L=1 A=0": [weird_division(df[(df.Y1 == 1) & (df.A == 0) & (df.L == 1)].count()[0], df[(df.A == 0) & (df.L == 1)].count()[0])],
        "Y1=1 L=1 A=1": [weird_division(df[(df.Y1 == 1) & (df.A == 1) & (df.L == 1)].count()[0], df[(df.A == 1) & (df.L == 1)].count()[0])]
    }

    Y1_matrix = pd.DataFrame(Y1_matrix)

    ratiocheck = [weird_division(Y0_matrix.iloc[0][0], Y0_matrix.iloc[0][1]) == weird_division(Y0_matrix.iloc[0][2], Y0_matrix.iloc[0][3]) & weird_division(Y0_matrix.iloc[0][0], Y0_matrix.iloc[0][1]) != 0,
                  weird_division(Y0_matrix.iloc[0][4], Y0_matrix.iloc[0][5]) == weird_division(
                      Y0_matrix.iloc[0][6], Y0_matrix.iloc[0][7]) & weird_division(Y0_matrix.iloc[0][6], Y0_matrix.iloc[0][7]) != 0,
                  weird_division(Y1_matrix.iloc[0][0], Y1_matrix.iloc[0][1]) == weird_division(
                      Y1_matrix.iloc[0][2], Y1_matrix.iloc[0][3]) & weird_division(Y1_matrix.iloc[0][2], Y1_matrix.iloc[0][3]) != 0,
                  weird_division(Y1_matrix.iloc[0][4], Y1_matrix.iloc[0][5]) == weird_division(Y1_matrix.iloc[0][6], Y1_matrix.iloc[0][7]) & weird_division(Y1_matrix.iloc[0][6], Y1_matrix.iloc[0][7]) != 0]

    finalcheck = ratiocheck[0] & ratiocheck[1] & ratiocheck[2] & ratiocheck[3]
    return Y0_matrix, Y1_matrix, ratiocheck, finalcheck


def addBinaryStrings(arr, n):
    string = ""
    for i in range(0, n):
        string += str(arr[i])
    binaryStrings.append(string)


def generateAllBinaryStrings(n, arr, i):

    if i == n:
        addBinaryStrings(arr, n)
        return

    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)

    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)


if __name__ == "__main__":
    data = {
        "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "A": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        "Y": [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        "Y1": [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        "Y0": [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        "L": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    }
    # print(df)

    n = 12
    arr = [None] * n
    generateAllBinaryStrings(n, arr, 0)

    for binary in binaryStrings:
        for i in range(0, n):
            data["L"][i] = binary[i]
        df = pd.DataFrame(data)
        check = YMatrix(df)[3]
        print(binary, check)
        if check:
            break
