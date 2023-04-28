import math
import sys
import numpy
import warnings

warnings.filterwarnings("ignore")
numpy.set_printoptions(linewidth=sys.maxsize)


def read_matrix_by_choice():
    print('Пожалуйста, выберите откуда вы желаете ввести матрицу в программу:')
    print('1. Из терминала')
    print('2. Из файла(потребуется ввести имя файла)')
    choice = input()
    if choice == '1':
        h = int(input('Пожалуйста введите количество строк:'))
        assert h > 0
        w = int(input('Пожалуйста введите количество столбцов:'))
        assert w > 0
        assert w == h + 1
        matrix = []
        for i in range(h):
            matrix.append(list(map(float, input().split())))
            assert len(matrix[-1]) == w
        return numpy.array(matrix)
    elif choice == '2':
        return numpy.loadtxt(input('Пожалуйста введите название файла:'))


def to_triangle_form(matrix: numpy.ndarray):
    def swap_with_max_row(row: int):
        old_value: float = matrix[row][row]
        for i in range(row + 1, len(matrix)):
            if abs(matrix[i][row]) > abs(matrix[row][row]):
                matrix[[row, i]] = matrix[[i, row]]
        return abs(old_value - matrix[row][row]) > 0.0

    def clear_column(row: int):
        for j in range(row + 1, len(matrix)):
            assert math.isfinite((-matrix[j][row] / matrix[row][row]))
            matrix[j] += matrix[row] * (-matrix[j][row] / matrix[row][row])

    count_of_row_swaps = 0
    for i in range(len(matrix)):
        if swap_with_max_row(i):
            clear_column(i)
            count_of_row_swaps += 1
            print('Элемент', i + 1, 'в', i + 1, 'строке не максимальный по модулю в столбце. Обмен!\n', matrix)
        else:
            clear_column(i)
    return count_of_row_swaps


def get_determinant(matrix: numpy.ndarray, count_of_row_swaps: int):
    assert len(matrix) <= len(matrix[0])
    det = 1.0 if (count_of_row_swaps % 2 == 0) else -1.0
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det


def get_roots(matrix: numpy.ndarray):
    assert len(matrix) + 1 == len(matrix[0])
    roots = [0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        roots[i] = matrix[i][-1]
        for j in range(i + 1, len(matrix)):
            roots[i] -= matrix[i][j] * roots[j]
        roots[i] /= matrix[i][i]
    return numpy.array(roots)


def get_discrepancies(matrix: numpy.ndarray, roots: numpy.ndarray):
    assert len(matrix) + 1 == len(matrix[0])
    discrepancies = [0] * len(matrix)
    for i in range(len(matrix)):
        discrepancies[i] = matrix[i][-1]
        for j in range(i, len(matrix)):
            discrepancies[i] -= matrix[i][j] * roots[j]
    return numpy.array(discrepancies)


try:
    matrix = read_matrix_by_choice()
    print('Матрица:\n', matrix, '\n')
except:
    print('Упс. При чтении матрицы возникла ошибка.')
    exit(0)

try:
    count_of_swaps = to_triangle_form(matrix)
    print('Количество перестановок строк:', count_of_swaps, '\n')
    print('Треугольная матрица:\n', matrix, '\n')
except:
    print('Упс. При приведении матрицы к треугольному виду возникла ошибка.')
    exit(0)

try:
    determinant = get_determinant(matrix, count_of_swaps)
    if abs(determinant) == 0.0:
        print('Определитель матрицы равен 0, вычисление корней и невязок невозможно.')
        exit(0)
    print('Определитель:', determinant, '\n')
except:
    print('Упс. При вычислении определителя матрицы возникла ошибка.')
    exit(0)

try:
    roots = get_roots(matrix)
    print('Корни:', roots, '\n')
except:
    print('Упс. При вычислении корней возникла ошибка.')
    exit(0)

try:
    discrepancies = get_discrepancies(matrix, roots)
    print('Невязки:', discrepancies, '\n')
except:
    print('Упс. При вычислении невязок возникла ошибка.')
    exit(0)
