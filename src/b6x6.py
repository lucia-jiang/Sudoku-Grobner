#! /bin/python3
import timeit

import sympy as sp

# tarda entre 2 y 3 segundos

class Sudoku6():
    def __init__(self, values):
        self.entrada = values
        self.grid = self.entrada
        print(self.grid)
        self.entradaConvert = [''] * 36
        cont = 0
        for i in range(1, 6 + 1):
            for j in range(1, 6 + 1):
                if self.entrada[i-1][j-1] > 0:
                    self.entradaConvert[cont] = 'x' + str(i) + str(j) + '-' + str(self.entrada[i - 1][j - 1])
                else:
                    self.entradaConvert[cont] = 'x' + str(i) + str(j) + '-' + 'x' + str(i) + str(j)
                cont += 1
        print(self.entradaConvert)

    def get_value(self, row, col):
        return self.grid[row][col]

    def solv(self):
        variables = sp.symbols(
            ['x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x31', 'x32', 'x33',
             'x34',
             'x35', 'x36', 'x41', 'x42', 'x43', 'x44', 'x45', 'x46', 'x51', 'x52', 'x53', 'x54', 'x55', 'x56', 'x61',
             'x62',
             'x63', 'x64', 'x65', 'x66'])

        lista = ['(x11-1)*(x11-2)*(x11-3)*(x11-4)*(x11-5)*(x11-6)', '(x12-1)*(x12-2)*(x12-3)*(x12-4)*(x12-5)*(x12-6)',
                 '(x13-1)*(x13-2)*(x13-3)*(x13-4)*(x13-5)*(x13-6)', '(x14-1)*(x14-2)*(x14-3)*(x14-4)*(x14-5)*(x14-6)',
                 '(x15-1)*(x15-2)*(x15-3)*(x15-4)*(x15-5)*(x15-6)', '(x16-1)*(x16-2)*(x16-3)*(x16-4)*(x16-5)*(x16-6)',
                 '(x21-1)*(x21-2)*(x21-3)*(x21-4)*(x21-5)*(x21-6)', '(x22-1)*(x22-2)*(x22-3)*(x22-4)*(x22-5)*(x22-6)',
                 '(x23-1)*(x23-2)*(x23-3)*(x23-4)*(x23-5)*(x23-6)', '(x24-1)*(x24-2)*(x24-3)*(x24-4)*(x24-5)*(x24-6)',
                 '(x25-1)*(x25-2)*(x25-3)*(x25-4)*(x25-5)*(x25-6)', '(x26-1)*(x26-2)*(x26-3)*(x26-4)*(x26-5)*(x26-6)',
                 '(x31-1)*(x31-2)*(x31-3)*(x31-4)*(x31-5)*(x31-6)', '(x32-1)*(x32-2)*(x32-3)*(x32-4)*(x32-5)*(x32-6)',
                 '(x33-1)*(x33-2)*(x33-3)*(x33-4)*(x33-5)*(x33-6)', '(x34-1)*(x34-2)*(x34-3)*(x34-4)*(x34-5)*(x34-6)',
                 '(x35-1)*(x35-2)*(x35-3)*(x35-4)*(x35-5)*(x35-6)', '(x36-1)*(x36-2)*(x36-3)*(x36-4)*(x36-5)*(x36-6)',
                 '(x41-1)*(x41-2)*(x41-3)*(x41-4)*(x41-5)*(x41-6)', '(x42-1)*(x42-2)*(x42-3)*(x42-4)*(x42-5)*(x42-6)',
                 '(x43-1)*(x43-2)*(x43-3)*(x43-4)*(x43-5)*(x43-6)', '(x44-1)*(x44-2)*(x44-3)*(x44-4)*(x44-5)*(x44-6)',
                 '(x45-1)*(x45-2)*(x45-3)*(x45-4)*(x45-5)*(x45-6)', '(x46-1)*(x46-2)*(x46-3)*(x46-4)*(x46-5)*(x46-6)',
                 '(x51-1)*(x51-2)*(x51-3)*(x51-4)*(x51-5)*(x51-6)', '(x52-1)*(x52-2)*(x52-3)*(x52-4)*(x52-5)*(x52-6)',
                 '(x53-1)*(x53-2)*(x53-3)*(x53-4)*(x53-5)*(x53-6)', '(x54-1)*(x54-2)*(x54-3)*(x54-4)*(x54-5)*(x54-6)',
                 '(x55-1)*(x55-2)*(x55-3)*(x55-4)*(x55-5)*(x55-6)', '(x56-1)*(x56-2)*(x56-3)*(x56-4)*(x56-5)*(x56-6)',
                 '(x61-1)*(x61-2)*(x61-3)*(x61-4)*(x61-5)*(x61-6)', '(x62-1)*(x62-2)*(x62-3)*(x62-4)*(x62-5)*(x62-6)',
                 '(x63-1)*(x63-2)*(x63-3)*(x63-4)*(x63-5)*(x63-6)', '(x64-1)*(x64-2)*(x64-3)*(x64-4)*(x64-5)*(x64-6)',
                 '(x65-1)*(x65-2)*(x65-3)*(x65-4)*(x65-5)*(x65-6)', '(x66-1)*(x66-2)*(x66-3)*(x66-4)*(x66-5)*(x66-6)',
                 'x11+x12+x13+x14+x15+x16-21', 'x21+x22+x23+x24+x25+x26-21', 'x31+x32+x33+x34+x35+x36-21',
                 'x41+x42+x43+x44+x45+x46-21', 'x51+x52+x53+x54+x55+x56-21', 'x61+x62+x63+x64+x65+x66-21',
                 'x11+x21+x31+x41+x51+x61-21', 'x12+x22+x32+x42+x52+x62-21', 'x13+x23+x33+x43+x53+x63-21',
                 'x14+x24+x34+x44+x54+x64-21', 'x15+x25+x35+x45+x55+x65-21', 'x16+x26+x36+x46+x56+x66-21',
                 'x11+x12+x13+x21+x22+x23-21', 'x14+x15+x16+x24+x25+x26-21', 'x31+x32+x33+x41+x42+x43-21',
                 'x34+x35+x36+x44+x45+x46-21', 'x51+x52+x53+x61+x62+x63-21', 'x54+x55+x56+x64+x65+x66-21',
                 'x11*x12*x13*x14*x15*x16-720', 'x21*x22*x23*x24*x25*x26-720', 'x31*x32*x33*x34*x35*x36-720',
                 'x41*x42*x43*x44*x45*x46-720', 'x51*x52*x53*x54*x55*x56-720', 'x61*x62*x63*x64*x65*x66-720',
                 'x11*x21*x31*x41*x51*x61-720', 'x12*x22*x32*x42*x52*x62-720', 'x13*x23*x33*x43*x53*x63-720',
                 'x14*x24*x34*x44*x54*x64-720', 'x15*x25*x35*x45*x55*x65-720', 'x16*x26*x36*x46*x56*x66-720',
                 'x11*x12*x13*x21*x22*x23-720', 'x14*x15*x16*x24*x25*x26-720', 'x31*x32*x33*x41*x42*x43-720',
                 'x34*x35*x36*x44*x45*x46-720', 'x51*x52*x53*x61*x62*x63-720', 'x54*x55*x56*x64*x65*x66-720']

        # ecuaciones = solucion.copy()
        ecuaciones = self.entradaConvert.copy();
        # ecuaciones = principiante.copy()
        ecuaciones += lista

        groebner = sp.groebner(ecuaciones, variables, order='lex')

        print(groebner)

        self.sol = sp.solve(groebner)
        print(self.sol)

        self.numeroSol = 0

        if len(self.sol) == 0:
            return False
        elif isinstance(self.sol, list):
            numSol = self.sol[self.numeroSol]

            matrizSol = [[0 for x in range(6)] for y in range(6)]
            cont = 0
            for i in range(6):
                for j in range(6):
                    matrizSol[i][j] = numSol[self.variables[cont]]
                    cont += 1
            print(matrizSol)
            self.grid = matrizSol
            return True
        else:
            numSol = list(self.sol.values())

            matrizSol = [[0 for x in range(6)] for y in range(6)]
            cont = 0
            for i in range(6):
                for j in range(6):
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

        matrizSol = [[0 for x in range(6)] for y in range(6)]
        cont = 0
        for i in range(6):
            for j in range(6):
                matrizSol[i][j] = numSol[self.variables[cont]]
                cont += 1
        print(matrizSol)
        self.grid = matrizSol
        return True

    def __str__(self):
        out = "";
        print(self.grid)
        for row in range(6):
            out += " ".join(map(str, self.grid[row])) + "\n"
        return out



"""
CÓMO SE CALCULAN LAS ECUACIONES

num_casillas = 36
num_lados = 6

# variables_matriz = [['x' + str(i) + str(j) for j in range(1, num_lados + 1)] for i in range(1, num_lados + 1)]

variables2 = [''] * num_casillas
cont = 0
for i in range(1, num_lados + 1):
    for j in range(1, num_lados + 1):
        variables2[cont] = 'x' + str(i) + str(j)
        cont += 1
# print(variables2)
# crear variables2:
# x11, x12, x13, x14, x21, x22, x23, x24, x31, x32, x33, x34, x41, x42, x43, x44 = sp.symbols(
#    'x11 x12 x13 x14 x21 x22 x23 x24 x31 x32 x33 x34 x41 x42 x43 x44')
variables = sp.symbols(variables2)
# print(variables2)
f = [''] * num_casillas
# variables2 de la manera xij con i nº de fila y j nº de columna
for i in range(num_casillas):
    for k in range(1, num_lados):
        f[i] += '(' + str(variables2[i]) + '-' + str(k) + ')*'
    f[i] += '(' + str(variables2[i]) + '-6)'

p = [''] * num_lados * 3  # restricciones de suma
m = [''] * num_lados * 3  # restricciones de multiplicación
cont = 0
# fila
for i in range(num_lados):
    for j in range(num_lados):
        p[cont] += str(variables2[i * num_lados + j]) + '+'
        m[cont] += str(variables2[i * num_lados + j]) + '*'
    p[cont] = p[cont][:-1] + '-21'
    m[cont] = m[cont][:-1] + '-720'
    cont += 1

# columna:
for i in range(num_lados):
    for j in range(num_lados):
        p[cont] += str(variables2[i + num_lados * j]) + '+'
        m[cont] += str(variables2[i + num_lados * j]) + '*'
    p[cont] = p[cont][:-1] + '-21'
    m[cont] = m[cont][:-1] + '-720'
    cont += 1

cuadrados = [['x11', 'x12', 'x13', 'x21', 'x22', 'x23'],
             ['x14', 'x15', 'x16', 'x24', 'x25', 'x26'],
             ['x31', 'x32', 'x33', 'x41', 'x42', 'x43'],
             ['x34', 'x35', 'x36', 'x44', 'x45', 'x46'],
             ['x51', 'x52', 'x53', 'x61', 'x62', 'x63'],
             ['x54', 'x55', 'x56', 'x64', 'x65', 'x66'],
             ]

# cont = 0

for i in range(num_lados):
    for j in range(num_lados):
        p[cont] += cuadrados[i][j] + '+'
        m[cont] += cuadrados[i][j] + '*'
    p[cont] = p[cont][:-1] + '-21'
    m[cont] = m[cont][:-1] + '-720'
    cont += 1
"""
