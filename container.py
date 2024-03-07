
cont = [[0 for i in range(1000)]
        for j in range(1000)]


def num_of_containers(n, x):
    count = 0
    cont[1][1] = x
    for i in range(1, n + 1):
        for j in range(1, i + 1):

            if (cont[i][j] >= 1):
                count += 1
                cont[i + 1][j] += (cont[i][j] - 1) / 2
                cont[i + 1][j + 1] += (cont[i][j] - 1) / 2
    print(count)


n = 3
x = 5
num_of_containers(n, x)
