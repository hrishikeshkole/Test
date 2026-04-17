def calculate_average(numbers):
    if not numbers:
        return 0

    total = sum(numbers)
    return total / len(numbers)


def main():
    data = [10, 20, 30, 40]
    avg = calculate_average(data)
    print(f"Average: {avg}")


if __name__ == "__main__":
    main()