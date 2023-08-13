
import sympy as sp


import timeit


class Sudoku4():
    def __init__(self, values):
        self.entrada = values
        self.grid = self.entrada
        print(self.grid)
        self.entradaConvert = [''] * 16
        cont = 0
        for i in range(1, 4 + 1):
            for j in range(1, 4 + 1):
                if self.entrada[i-1][j-1] > 0:
                    self.entradaConvert[cont] = 'x' + str(i) + str(j) + '-' + str(self.entrada[i - 1][j - 1])
                else:
                    self.entradaConvert[cont] = 'x' + str(i) + str(j) + '-' + 'x' + str(i) + str(j)
                cont += 1
        print(self.entradaConvert)

    def get_value(self, row, col):
        return self.grid[row][col]

    def solv(self):
        num_casillas = 16
        num_lados = 4

        variables_matriz = [['x' + str(i) + str(j) for j in range(1, num_lados + 1)] for i in range(1, num_lados + 1)]

        print(variables_matriz)

        variables = [''] * 16
        cont = 0
        for i in range(1, num_lados + 1):
            for j in range(1, num_lados + 1):
                variables[cont] = 'x' + str(i) + str(j)
                cont += 1

        # crear variables:
        x11, x12, x13, x14, x21, x22, x23, x24, x31, x32, x33, x34, x41, x42, x43, x44 = sp.symbols(
            'x11 x12 x13 x14 x21 x22 x23 x24 x31 x32 x33 x34 x41 x42 x43 x44')

        self.variables2 = sp.symbols(variables)

        f = [''] * 16
        # variables de la manera xij con i nº de fila y j nº de columna
        for i in range(num_casillas):
            for k in range(1, num_lados + 1):
                f[i] += '(' + str(variables[i]) + '-' + str(k) + ')*'
            f[i] = f[i][:-1]

        print("Restricciones de enteros:")
        print(f)

        p = [''] * 12  # restricciones de suma
        m = [''] * 12  # restricciones de multiplicación
        cont = 0
        # fila
        for i in range(num_lados):
            for j in range(num_lados):
                p[cont] += str(variables[i * num_lados + j]) + '+'
                m[cont] += str(variables[i * num_lados + j]) + '*'
            p[cont] = p[cont][:-1] + '-10'
            m[cont] = m[cont][:-1] + '-24'
            cont += 1

        print("Restricciones de fila:")
        print(p[0:4])
        print("Valor de cont: " + str(cont))

        # columna:
        for i in range(num_lados):
            for j in range(num_lados):
                p[cont] += str(variables[i + num_lados * j]) + '+'
                m[cont] += str(variables[i + num_lados * j]) + '*'
            p[cont] = p[cont][:-1] + '-10'
            m[cont] = m[cont][:-1] + '-24'
            cont += 1

        print("Restricciones de columna:")
        print(p[4:8])
        print("Valor de cont: " + str(cont))

        # cuadrados:
        p[8] = 'x11 + x12 + x21 + x22 - 10'
        p[9] = 'x13 + x14 + x23 + x24 - 10'
        p[10] = 'x31 + x32 + x41 + x42 - 10'
        p[11] = 'x33 + x34 + x43 + x44 - 10'

        m[8] = 'x11 * x12 * x21 * x22 - 24'
        m[9] = 'x13 * x14 * x23 * x24 - 24'
        m[10] = 'x31 * x32 * x41 * x42 - 24'
        m[11] = 'x33 * x34 * x43 * x44 - 24'

        lista = f
        lista += p
        lista += m
        lista += self.entradaConvert

        print(lista)

        groebner = sp.groebner(lista, self.variables2, order='lex')

        self.sol = sp.solve(groebner)
        print(self.sol)

        self.numeroSol = 0

        if len(self.sol) == 0:
            return False
        elif isinstance(self.sol, list):
            numSol = self.sol[self.numeroSol]

            matrizSol = [[0 for x in range(4)] for y in range(4)]
            cont = 0
            for i in range(4):
                for j in range(4):
                    matrizSol[i][j] = numSol[self.variables2[cont]]
                    cont += 1
            print(matrizSol)
            self.grid = matrizSol
            return True
        else:
            numSol = list(self.sol.values())

            matrizSol = [[0 for x in range(4)] for y in range(4)]
            cont = 0
            for i in range(4):
                for j in range(4):
                    matrizSol[i][j] = numSol[cont]
                    cont += 1
            print(matrizSol)
            self.grid = matrizSol
            return True

    def other_solutions(self):
        if ((len(self.sol) - 1 == self.numeroSol) or not(isinstance(self.sol, list))):
            return False

        self.numeroSol += 1
        numSol = self.sol[self.numeroSol]

        matrizSol = [[0 for x in range(4)] for y in range(4)]
        cont = 0
        for i in range(4):
            for j in range(4):
                matrizSol[i][j] = numSol[self.variables2[cont]]
                cont += 1
        print(matrizSol)
        self.grid = matrizSol
        return True


    def __str__(self):
        out = "";
        print(self.grid)
        for row in range(4):
            out += " ".join(map(str, self.grid[row])) + "\n"
        return out



