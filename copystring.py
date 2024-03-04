def myCopy(s1, s2):

    for i in range(len(s1)):

        k = s2[i] = s1[i]
        print(k)
    return "".join(s2)


s1 = list("syfu")
s2 = [""]*len(s1)
print(myCopy(s1, s2))
