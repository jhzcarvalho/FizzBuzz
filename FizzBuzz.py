def main():
    for i in range(100):
        buff = ""
        if (i % 3) == 0:
            buff += "Fizz"
        if (i % 5) == 0:
            buff += "Buzz"

        if buff == "":
            print(i)
        else:
            print(buff)


if __name__ == "__main__":
    main()
