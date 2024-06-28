def main():

    N = int(input('Enter the number N: '))
    result = []

    for x in range(0,N+1):
        math = 2**x
        result.append(math)
    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
