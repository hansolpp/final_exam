
i_list = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]

def my_function(x):

    # 분모
    denominator = 1

    # 부호
    sign = 1

    # 합
    sum = 0

    for i in range(x):
        sum += sign * (1/denominator)

        denominator += 2
        sign *= -1

    return round(4 * sum, 4)


print("i        m(i)")
for i in i_list:
    print(str(i) + "        " + str(my_function(i)))