class Minimax:
    def __init__(self, matrix):
        self.__matrix = matrix
        self.__first_step_col = []
        self.__second_step_max_val = 0
        self.__third_step_row = []
        self.__fourth_step_min_val = 0
        self.__saddle_points = []
    
    def compute(self):
        self.__first_step()
        self.__second_step()
        self.__third_step()
        self.__fourth_step()
        self.__fifth_step()
        return self.__saddle_points
    
    # Returns matrix's string view with additional column and row.
    def matrixToStr(self):
        matrix = ''
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[0])):
                matrix += str(self.__matrix[i][j]) + ' '
            matrix += str(self.__first_step_col[i]) + '\n'
        for val in self.__third_step_row:
            matrix += str(val) + ' '
        return matrix

    # Adding new column with mins value of each row.
    def __first_step(self):
        for row in self.__matrix:
            self.__first_step_col.append(min(row))

    # Finding max value of additional column.
    def __second_step(self):
        self.__second_step_max_val = max(self.__first_step_col)
    
    # Adding new row with maxs value of each column.
    def __third_step(self):
        temp = []
        for i in range(len(self.__matrix[0])):
            for j in range(len(self.__matrix)):
                temp.append(self.__matrix[j][i])
            self.__third_step_row.append(max(temp))
            temp = []

    # Finding min value of additional row.
    def __fourth_step(self):
        self.__fourth_step_min_val = min(self.__third_step_row)

    # Looking for saddle points.
    def __fifth_step(self):
        if self.__second_step_max_val == self.__fourth_step_min_val:
            saddle_point_val = self.__second_step_max_val
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[i])):
                    if self.__matrix[i][j] == saddle_point_val and (i,j) not in self.__saddle_points:
                        self.__saddle_points.append((i,j))
                    

    