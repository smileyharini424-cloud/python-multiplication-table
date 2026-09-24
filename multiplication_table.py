def generate_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


def main():
    try:
        number = int(input("Enter a number: "))
        limit = int(input("Enter table limit: "))

        if limit <= 0:
            print("Table limit must be greater than zero.")
            return

        generate_table(number, limit)

    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()
