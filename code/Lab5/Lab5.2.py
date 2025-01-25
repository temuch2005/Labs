def create_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            value = 7 - abs(i - j)
            row.append(value)
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    rows, cols = 7, 7
    matrix = create_matrix(rows, cols)
    print("Заповнений двовимірний масив 7x7:")
    print_matrix(matrix)


if __name__ == "__main__":
    main()
