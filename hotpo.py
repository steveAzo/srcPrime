def hotpo(n):
    count = 0
    while n != 1:
        if n == 1:
            return 1
        elif n % 2 == 0:
            n = (n // 2)
            count += 1
        else:
            n = 3 * n + 1
            count += 1
    return count

def main():
    try:
        number = int(input("What number do you want to check the steps? "))
        if number <= 0:
            print("The number is supposed to be a positive number")
        else:
            result = hotpo(number)
            print(f"The number of steps {number} has to go through to reach 1 is {result}")
    except ValueError:
        print("Enter a positive number")

if __name__ == "__main__":
    main()


