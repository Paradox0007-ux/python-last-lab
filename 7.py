
import random

def display_matrix(matrix):
    for row in matrix:
        print(row)


def remove_negative(matrix):
    result = list(map(
        lambda row: list(filter(lambda x: x >= 0, row)),
        matrix
    ))
    return result


def square_matrix(matrix):
    return list(map(
        lambda row: list(map(lambda x: x * x, row)),
        matrix
    ))


def sort_rows(matrix):
    return list(map(lambda row: sorted(row), matrix))


def sort_by_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))


def flatten_matrix(matrix):
    return [element for row in matrix for element in row]


def main():
    matrix = [
        [5, -2, 8],
        [3, -4, 1],
        [9, 2, -6],
        [7, 0, 4]
    ]

    while True:
        print("\n===== MATRIX TRANSFORMATION SUITE =====")
        print("1. Display Matrix")
        print("2. Remove Negative Numbers")
        print("3. Square All Elements")
        print("4. Sort Each Row")
        print("5. Sort Rows by Sum")
        print("6. Flatten Matrix")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_matrix(matrix)

        elif choice == "2":
            result = remove_negative(matrix)
            print("Matrix without negative numbers:")
            display_matrix(result)

        elif choice == "3":
            result = square_matrix(matrix)
            print("Squared Matrix:")
            display_matrix(result)

        elif choice == "4":
            result = sort_rows(matrix)
            print("Sorted Rows:")
            display_matrix(result)

        elif choice == "5":
            result = sort_by_sum(matrix)
            print("Rows sorted by sum:")
            display_matrix(result)

        elif choice == "6":
            result = flatten_matrix(matrix)
            print("Flattened Matrix:", result)

        elif choice == "7":
            print("Exiting Matrix Transformation Suite...")
            break

        else:
            print("Invalid choice! Try again.")


main()
