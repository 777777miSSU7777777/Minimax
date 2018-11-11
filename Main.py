from Minimax import Minimax
import sys

def main():

    matrix = []

    while True:
        row = input("Input row to continue or enter to finish.\n")
        if row:
            row_str = row.split()
            row_int = []
            for val in row_str:
                row_int.append(int(val))
            matrix.append(row_int)
        else:
            break

    print("Source matrix")
    for row in matrix:
        for element in row:
            sys.stdout.write(str(element))
            sys.stdout.write(" ")
        print()

    m = Minimax(matrix)
    saddle_points = m.compute()
    changed_matrix_str = m.matrixToStr()
    print("Matrix with additional column and row:")
    print(changed_matrix_str)
    if saddle_points != []:
        print("Saddle points")
        for saddle_point in saddle_points:
            i = saddle_point[0]
            j = saddle_point[1]
            print("Saddle point (%d,%d)=> %d" % (i+1,j+1,matrix[i][j]))
    else:
        print("There no saddle points")

main()