#! /bin/python3
import timeit

import sympy as sp

class Sudoku9():
    def __init__(self, values):
        self.entrada = values
        print(self.entrada)
        self.grid = self.entrada
        self.entradaConvert = [''] * 81
        cont = 0
        for i in range(1, 9 + 1):
            for j in range(1, 9 + 1):
                if self.entrada[i - 1][j - 1] > 7:
                    self.entradaConvert[cont] = 'x' + str(i) + str(j) + '+' + str(10 - self.entrada[i - 1][j - 1])
                elif self.entrada[i-1][j-1] == 0:
                    self.entradaConvert[cont] = 'x' + str(i) + str(j) + '-' + 'x' + str(i) + str(j)
                else:
                    self.entradaConvert[cont] = 'x' + str(i) + str(j) + '-' + str(self.entrada[i - 1][j - 1])
                cont += 1

        print(self.entradaConvert)

    def get_value(self, row, col):
        return self.grid[row][col]


    def solv(self):
        variables = sp.symbols(
            ['x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x21', 'x22', 'x23', 'x24', 'x25', 'x26',
             'x27', 'x28', 'x29', 'x31', 'x32', 'x33', 'x34', 'x35', 'x36', 'x37', 'x38', 'x39', 'x41', 'x42', 'x43',
             'x44', 'x45', 'x46', 'x47', 'x48', 'x49', 'x51', 'x52', 'x53', 'x54', 'x55', 'x56', 'x57', 'x58', 'x59',
             'x61', 'x62', 'x63', 'x64', 'x65', 'x66', 'x67', 'x68', 'x69', 'x71', 'x72', 'x73', 'x74', 'x75', 'x76',
             'x77', 'x78', 'x79', 'x81', 'x82', 'x83', 'x84', 'x85', 'x86', 'x87', 'x88', 'x89', 'x91', 'x92', 'x93',
             'x94', 'x95', 'x96', 'x97', 'x98', 'x99'])

        lista = ['x11+x12+x13+x14+x15+x16+x17+x18+x19-25', 'x21+x22+x23+x24+x25+x26+x27+x28+x29-25',
                 'x31+x32+x33+x34+x35+x36+x37+x38+x39-25', 'x41+x42+x43+x44+x45+x46+x47+x48+x49-25',
                 'x51+x52+x53+x54+x55+x56+x57+x58+x59-25', 'x61+x62+x63+x64+x65+x66+x67+x68+x69-25',
                 'x71+x72+x73+x74+x75+x76+x77+x78+x79-25', 'x81+x82+x83+x84+x85+x86+x87+x88+x89-25',
                 'x91+x92+x93+x94+x95+x96+x97+x98+x99-25', 'x11+x21+x31+x41+x51+x61+x71+x81+x91-25',
                 'x12+x22+x32+x42+x52+x62+x72+x82+x92-25', 'x13+x23+x33+x43+x53+x63+x73+x83+x93-25',
                 'x14+x24+x34+x44+x54+x64+x74+x84+x94-25', 'x15+x25+x35+x45+x55+x65+x75+x85+x95-25',
                 'x16+x26+x36+x46+x56+x66+x76+x86+x96-25', 'x17+x27+x37+x47+x57+x67+x77+x87+x97-25',
                 'x18+x28+x38+x48+x58+x68+x78+x88+x98-25', 'x19+x29+x39+x49+x59+x69+x79+x89+x99-25',
                 'x11+x21+x31+x12+x22+x32+x13+x23+x33-25', 'x14+x24+x34+x15+x25+x35+x16+x26+x36-25',
                 'x17+x27+x37+x18+x28+x38+x19+x29+x39-25', 'x41+x51+x61+x42+x52+x62+x43+x53+x63-25',
                 'x44+x54+x64+x45+x55+x65+x46+x56+x66-25', 'x47+x57+x67+x48+x58+x68+x49+x59+x69-25',
                 'x71+x81+x91+x72+x82+x92+x73+x83+x93-25', 'x74+x84+x94+x75+x85+x95+x76+x86+x96-25',
                 'x77+x87+x97+x78+x88+x98+x79+x89+x99-25', 'x11*x12*x13*x14*x15*x16*x17*x18*x19-10080',
                 'x21*x22*x23*x24*x25*x26*x27*x28*x29-10080', 'x31*x32*x33*x34*x35*x36*x37*x38*x39-10080',
                 'x41*x42*x43*x44*x45*x46*x47*x48*x49-10080', 'x51*x52*x53*x54*x55*x56*x57*x58*x59-10080',
                 'x61*x62*x63*x64*x65*x66*x67*x68*x69-10080', 'x71*x72*x73*x74*x75*x76*x77*x78*x79-10080',
                 'x81*x82*x83*x84*x85*x86*x87*x88*x89-10080', 'x91*x92*x93*x94*x95*x96*x97*x98*x99-10080',
                 'x11*x21*x31*x41*x51*x61*x71*x81*x91-10080', 'x12*x22*x32*x42*x52*x62*x72*x82*x92-10080',
                 'x13*x23*x33*x43*x53*x63*x73*x83*x93-10080', 'x14*x24*x34*x44*x54*x64*x74*x84*x94-10080',
                 'x15*x25*x35*x45*x55*x65*x75*x85*x95-10080', 'x16*x26*x36*x46*x56*x66*x76*x86*x96-10080',
                 'x17*x27*x37*x47*x57*x67*x77*x87*x97-10080', 'x18*x28*x38*x48*x58*x68*x78*x88*x98-10080',
                 'x19*x29*x39*x49*x59*x69*x79*x89*x99-10080', 'x11*x21*x31*x12*x22*x32*x13*x23*x33-10080',
                 'x14*x24*x34*x15*x25*x35*x16*x26*x36-10080', 'x17*x27*x37*x18*x28*x38*x19*x29*x39-10080',
                 'x41*x51*x61*x42*x52*x62*x43*x53*x63-10080', 'x44*x54*x64*x45*x55*x65*x46*x56*x66-10080',
                 'x47*x57*x67*x48*x58*x68*x49*x59*x69-10080', 'x71*x81*x91*x72*x82*x92*x73*x83*x93-10080',
                 'x74*x84*x94*x75*x85*x95*x76*x86*x96-10080', 'x77*x87*x97*x78*x88*x98*x79*x89*x99-10080',
                 '(x11-1)*(x11-2)*(x11-3)*(x11-4)*(x11-5)*(x11-6)*(x11-7)*(x11+2)*(x11+1)',
                 '(x12-1)*(x12-2)*(x12-3)*(x12-4)*(x12-5)*(x12-6)*(x12-7)*(x12+2)*(x12+1)',
                 '(x13-1)*(x13-2)*(x13-3)*(x13-4)*(x13-5)*(x13-6)*(x13-7)*(x13+2)*(x13+1)',
                 '(x14-1)*(x14-2)*(x14-3)*(x14-4)*(x14-5)*(x14-6)*(x14-7)*(x14+2)*(x14+1)',
                 '(x15-1)*(x15-2)*(x15-3)*(x15-4)*(x15-5)*(x15-6)*(x15-7)*(x15+2)*(x15+1)',
                 '(x16-1)*(x16-2)*(x16-3)*(x16-4)*(x16-5)*(x16-6)*(x16-7)*(x16+2)*(x16+1)',
                 '(x17-1)*(x17-2)*(x17-3)*(x17-4)*(x17-5)*(x17-6)*(x17-7)*(x17+2)*(x17+1)',
                 '(x18-1)*(x18-2)*(x18-3)*(x18-4)*(x18-5)*(x18-6)*(x18-7)*(x18+2)*(x18+1)',
                 '(x19-1)*(x19-2)*(x19-3)*(x19-4)*(x19-5)*(x19-6)*(x19-7)*(x19+2)*(x19+1)',
                 '(x21-1)*(x21-2)*(x21-3)*(x21-4)*(x21-5)*(x21-6)*(x21-7)*(x21+2)*(x21+1)',
                 '(x22-1)*(x22-2)*(x22-3)*(x22-4)*(x22-5)*(x22-6)*(x22-7)*(x22+2)*(x22+1)',
                 '(x23-1)*(x23-2)*(x23-3)*(x23-4)*(x23-5)*(x23-6)*(x23-7)*(x23+2)*(x23+1)',
                 '(x24-1)*(x24-2)*(x24-3)*(x24-4)*(x24-5)*(x24-6)*(x24-7)*(x24+2)*(x24+1)',
                 '(x25-1)*(x25-2)*(x25-3)*(x25-4)*(x25-5)*(x25-6)*(x25-7)*(x25+2)*(x25+1)',
                 '(x26-1)*(x26-2)*(x26-3)*(x26-4)*(x26-5)*(x26-6)*(x26-7)*(x26+2)*(x26+1)',
                 '(x27-1)*(x27-2)*(x27-3)*(x27-4)*(x27-5)*(x27-6)*(x27-7)*(x27+2)*(x27+1)',
                 '(x28-1)*(x28-2)*(x28-3)*(x28-4)*(x28-5)*(x28-6)*(x28-7)*(x28+2)*(x28+1)',
                 '(x29-1)*(x29-2)*(x29-3)*(x29-4)*(x29-5)*(x29-6)*(x29-7)*(x29+2)*(x29+1)',
                 '(x31-1)*(x31-2)*(x31-3)*(x31-4)*(x31-5)*(x31-6)*(x31-7)*(x31+2)*(x31+1)',
                 '(x32-1)*(x32-2)*(x32-3)*(x32-4)*(x32-5)*(x32-6)*(x32-7)*(x32+2)*(x32+1)',
                 '(x33-1)*(x33-2)*(x33-3)*(x33-4)*(x33-5)*(x33-6)*(x33-7)*(x33+2)*(x33+1)',
                 '(x34-1)*(x34-2)*(x34-3)*(x34-4)*(x34-5)*(x34-6)*(x34-7)*(x34+2)*(x34+1)',
                 '(x35-1)*(x35-2)*(x35-3)*(x35-4)*(x35-5)*(x35-6)*(x35-7)*(x35+2)*(x35+1)',
                 '(x36-1)*(x36-2)*(x36-3)*(x36-4)*(x36-5)*(x36-6)*(x36-7)*(x36+2)*(x36+1)',
                 '(x37-1)*(x37-2)*(x37-3)*(x37-4)*(x37-5)*(x37-6)*(x37-7)*(x37+2)*(x37+1)',
                 '(x38-1)*(x38-2)*(x38-3)*(x38-4)*(x38-5)*(x38-6)*(x38-7)*(x38+2)*(x38+1)',
                 '(x39-1)*(x39-2)*(x39-3)*(x39-4)*(x39-5)*(x39-6)*(x39-7)*(x39+2)*(x39+1)',
                 '(x41-1)*(x41-2)*(x41-3)*(x41-4)*(x41-5)*(x41-6)*(x41-7)*(x41+2)*(x41+1)',
                 '(x42-1)*(x42-2)*(x42-3)*(x42-4)*(x42-5)*(x42-6)*(x42-7)*(x42+2)*(x42+1)',
                 '(x43-1)*(x43-2)*(x43-3)*(x43-4)*(x43-5)*(x43-6)*(x43-7)*(x43+2)*(x43+1)',
                 '(x44-1)*(x44-2)*(x44-3)*(x44-4)*(x44-5)*(x44-6)*(x44-7)*(x44+2)*(x44+1)',
                 '(x45-1)*(x45-2)*(x45-3)*(x45-4)*(x45-5)*(x45-6)*(x45-7)*(x45+2)*(x45+1)',
                 '(x46-1)*(x46-2)*(x46-3)*(x46-4)*(x46-5)*(x46-6)*(x46-7)*(x46+2)*(x46+1)',
                 '(x47-1)*(x47-2)*(x47-3)*(x47-4)*(x47-5)*(x47-6)*(x47-7)*(x47+2)*(x47+1)',
                 '(x48-1)*(x48-2)*(x48-3)*(x48-4)*(x48-5)*(x48-6)*(x48-7)*(x48+2)*(x48+1)',
                 '(x49-1)*(x49-2)*(x49-3)*(x49-4)*(x49-5)*(x49-6)*(x49-7)*(x49+2)*(x49+1)',
                 '(x51-1)*(x51-2)*(x51-3)*(x51-4)*(x51-5)*(x51-6)*(x51-7)*(x51+2)*(x51+1)',
                 '(x52-1)*(x52-2)*(x52-3)*(x52-4)*(x52-5)*(x52-6)*(x52-7)*(x52+2)*(x52+1)',
                 '(x53-1)*(x53-2)*(x53-3)*(x53-4)*(x53-5)*(x53-6)*(x53-7)*(x53+2)*(x53+1)',
                 '(x54-1)*(x54-2)*(x54-3)*(x54-4)*(x54-5)*(x54-6)*(x54-7)*(x54+2)*(x54+1)',
                 '(x55-1)*(x55-2)*(x55-3)*(x55-4)*(x55-5)*(x55-6)*(x55-7)*(x55+2)*(x55+1)',
                 '(x56-1)*(x56-2)*(x56-3)*(x56-4)*(x56-5)*(x56-6)*(x56-7)*(x56+2)*(x56+1)',
                 '(x57-1)*(x57-2)*(x57-3)*(x57-4)*(x57-5)*(x57-6)*(x57-7)*(x57+2)*(x57+1)',
                 '(x58-1)*(x58-2)*(x58-3)*(x58-4)*(x58-5)*(x58-6)*(x58-7)*(x58+2)*(x58+1)',
                 '(x59-1)*(x59-2)*(x59-3)*(x59-4)*(x59-5)*(x59-6)*(x59-7)*(x59+2)*(x59+1)',
                 '(x61-1)*(x61-2)*(x61-3)*(x61-4)*(x61-5)*(x61-6)*(x61-7)*(x61+2)*(x61+1)',
                 '(x62-1)*(x62-2)*(x62-3)*(x62-4)*(x62-5)*(x62-6)*(x62-7)*(x62+2)*(x62+1)',
                 '(x63-1)*(x63-2)*(x63-3)*(x63-4)*(x63-5)*(x63-6)*(x63-7)*(x63+2)*(x63+1)',
                 '(x64-1)*(x64-2)*(x64-3)*(x64-4)*(x64-5)*(x64-6)*(x64-7)*(x64+2)*(x64+1)',
                 '(x65-1)*(x65-2)*(x65-3)*(x65-4)*(x65-5)*(x65-6)*(x65-7)*(x65+2)*(x65+1)',
                 '(x66-1)*(x66-2)*(x66-3)*(x66-4)*(x66-5)*(x66-6)*(x66-7)*(x66+2)*(x66+1)',
                 '(x67-1)*(x67-2)*(x67-3)*(x67-4)*(x67-5)*(x67-6)*(x67-7)*(x67+2)*(x67+1)',
                 '(x68-1)*(x68-2)*(x68-3)*(x68-4)*(x68-5)*(x68-6)*(x68-7)*(x68+2)*(x68+1)',
                 '(x69-1)*(x69-2)*(x69-3)*(x69-4)*(x69-5)*(x69-6)*(x69-7)*(x69+2)*(x69+1)',
                 '(x71-1)*(x71-2)*(x71-3)*(x71-4)*(x71-5)*(x71-6)*(x71-7)*(x71+2)*(x71+1)',
                 '(x72-1)*(x72-2)*(x72-3)*(x72-4)*(x72-5)*(x72-6)*(x72-7)*(x72+2)*(x72+1)',
                 '(x73-1)*(x73-2)*(x73-3)*(x73-4)*(x73-5)*(x73-6)*(x73-7)*(x73+2)*(x73+1)',
                 '(x74-1)*(x74-2)*(x74-3)*(x74-4)*(x74-5)*(x74-6)*(x74-7)*(x74+2)*(x74+1)',
                 '(x75-1)*(x75-2)*(x75-3)*(x75-4)*(x75-5)*(x75-6)*(x75-7)*(x75+2)*(x75+1)',
                 '(x76-1)*(x76-2)*(x76-3)*(x76-4)*(x76-5)*(x76-6)*(x76-7)*(x76+2)*(x76+1)',
                 '(x77-1)*(x77-2)*(x77-3)*(x77-4)*(x77-5)*(x77-6)*(x77-7)*(x77+2)*(x77+1)',
                 '(x78-1)*(x78-2)*(x78-3)*(x78-4)*(x78-5)*(x78-6)*(x78-7)*(x78+2)*(x78+1)',
                 '(x79-1)*(x79-2)*(x79-3)*(x79-4)*(x79-5)*(x79-6)*(x79-7)*(x79+2)*(x79+1)',
                 '(x81-1)*(x81-2)*(x81-3)*(x81-4)*(x81-5)*(x81-6)*(x81-7)*(x81+2)*(x81+1)',
                 '(x82-1)*(x82-2)*(x82-3)*(x82-4)*(x82-5)*(x82-6)*(x82-7)*(x82+2)*(x82+1)',
                 '(x83-1)*(x83-2)*(x83-3)*(x83-4)*(x83-5)*(x83-6)*(x83-7)*(x83+2)*(x83+1)',
                 '(x84-1)*(x84-2)*(x84-3)*(x84-4)*(x84-5)*(x84-6)*(x84-7)*(x84+2)*(x84+1)',
                 '(x85-1)*(x85-2)*(x85-3)*(x85-4)*(x85-5)*(x85-6)*(x85-7)*(x85+2)*(x85+1)',
                 '(x86-1)*(x86-2)*(x86-3)*(x86-4)*(x86-5)*(x86-6)*(x86-7)*(x86+2)*(x86+1)',
                 '(x87-1)*(x87-2)*(x87-3)*(x87-4)*(x87-5)*(x87-6)*(x87-7)*(x87+2)*(x87+1)',
                 '(x88-1)*(x88-2)*(x88-3)*(x88-4)*(x88-5)*(x88-6)*(x88-7)*(x88+2)*(x88+1)',
                 '(x89-1)*(x89-2)*(x89-3)*(x89-4)*(x89-5)*(x89-6)*(x89-7)*(x89+2)*(x89+1)',
                 '(x91-1)*(x91-2)*(x91-3)*(x91-4)*(x91-5)*(x91-6)*(x91-7)*(x91+2)*(x91+1)',
                 '(x92-1)*(x92-2)*(x92-3)*(x92-4)*(x92-5)*(x92-6)*(x92-7)*(x92+2)*(x92+1)',
                 '(x93-1)*(x93-2)*(x93-3)*(x93-4)*(x93-5)*(x93-6)*(x93-7)*(x93+2)*(x93+1)',
                 '(x94-1)*(x94-2)*(x94-3)*(x94-4)*(x94-5)*(x94-6)*(x94-7)*(x94+2)*(x94+1)',
                 '(x95-1)*(x95-2)*(x95-3)*(x95-4)*(x95-5)*(x95-6)*(x95-7)*(x95+2)*(x95+1)',
                 '(x96-1)*(x96-2)*(x96-3)*(x96-4)*(x96-5)*(x96-6)*(x96-7)*(x96+2)*(x96+1)',
                 '(x97-1)*(x97-2)*(x97-3)*(x97-4)*(x97-5)*(x97-6)*(x97-7)*(x97+2)*(x97+1)',
                 '(x98-1)*(x98-2)*(x98-3)*(x98-4)*(x98-5)*(x98-6)*(x98-7)*(x98+2)*(x98+1)',
                 '(x99-1)*(x99-2)*(x99-3)*(x99-4)*(x99-5)*(x99-6)*(x99-7)*(x99+2)*(x99+1)',
                 ]

        ecuaciones = self.entradaConvert.copy()
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

            matrizSol = [[0 for x in range(4)] for y in range(4)]
            cont = 0
            for i in range(4):
                for j in range(4):
                    matrizSol[i][j] = numSol[self.variables[cont]]
                    cont += 1
            print(matrizSol)
            self.grid = matrizSol
            return True
        else:
            numSol = list(self.sol.values())
            print(numSol[80])
            matrizSol = [[0 for x in range(9)] for y in range(9)]
            cont = 0
            for i in range(9):
                for j in range(9):
                    if numSol[cont] < 0:
                        matrizSol[i][j] = 10 + numSol[cont]
                    else:
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

        matrizSol = [[0 for x in range(9)] for y in range(9)]
        cont = 0
        for i in range(9):
            for j in range(9):
                matrizSol[i][j] = numSol[self.variables[cont]]
                cont += 1
        print(matrizSol)
        self.grid = matrizSol
        return True

    def __str__(self):
        out = "";
        for row in range(9):
            out += " ".join(map(str, self.grid[row])) + "\n"
        return out




"""
CÓMO SE CALCULAN LAS ECUACIONES

        num_casillas = 81
        num_lados = 9

        # variables_matriz = [['x' + str(i) + str(j) for j in range(1, num_lados + 1)] for i in range(1, num_lados + 1)]

        variables = [''] * num_casillas
        cont = 0
        for i in range(1, num_lados + 1):
            for j in range(1, num_lados + 1):
                variables[cont] = 'x' + str(i) + str(j)
                cont += 1
        print(variables)
        # crear variables:
        # x11, x12, x13, x14, x21, x22, x23, x24, x31, x32, x33, x34, x41, x42, x43, x44 = sp.symbols(
        #    'x11 x12 x13 x14 x21 x22 x23 x24 x31 x32 x33 x34 x41 x42 x43 x44')
        variables = sp.symbols(variables)
        # print(variables)
        f = [''] * num_casillas
        # variables de la manera xij con i nº de fila y j nº de columna
        for i in range(num_casillas):
            for k in range(1, num_lados - 1):
                f[i] += '(' + str(variables[i]) + '-' + str(k) + ')*'
            f[i] += '(' + str(variables[i]) + '+2)*'
            f[i] += '(' + str(variables[i]) + '+1)'

        p = [''] * num_lados * 3  # restricciones de suma
        m = [''] * num_lados * 3  # restricciones de multiplicación
        cont = 0
        # fila
        for i in range(num_lados):
            for j in range(num_lados):
                p[cont] += str(variables[i * num_lados + j]) + '+'
                m[cont] += str(variables[i * num_lados + j]) + '*'
            p[cont] = p[cont][:-1] + '-25'
            m[cont] = m[cont][:-1] + '-10080'
            cont += 1

        # columna:
        for i in range(num_lados):
            for j in range(num_lados):
                p[cont] += str(variables[i + num_lados * j]) + '+'
                m[cont] += str(variables[i + num_lados * j]) + '*'
            p[cont] = p[cont][:-1] + '-25'
            m[cont] = m[cont][:-1] + '-10080'
            cont += 1

        for i in (0, 3, 6):
            for k in range(0, 3):
                for j in range(3):
                    p[cont] += str(variables[num_lados * (i) + k * 3 + j]) + '+'
                    p[cont] += str(variables[num_lados * (i + 1) + k * 3 + j]) + '+'
                    p[cont] += str(variables[(num_lados) * (i + 2) + k * 3 + j]) + '+'
                    m[cont] += str(variables[num_lados * (i) + k * 3 + j]) + '*'
                    m[cont] += str(variables[num_lados * (i + 1) + k * 3 + j]) + '*'
                    m[cont] += str(variables[(num_lados) * (i + 2) + k * 3 + j]) + '*'
                p[cont] = p[cont][:-1] + '-25'
                m[cont] = m[cont][:-1] + '-10080'
                cont += 1

        # p+=['x11+x21+x31+x12+x22+x32+x13+x23+x33-25', 'x14+x24+x34+x15+x25+x35+x16+x26+x36-25', 'x17+x27+x37+x18+x28+x38+x19+x29+x39-25', 'x41+x51+x61+x42+x52+x62+x43+x53+x63-25', 'x44+x54+x64+x45+x55+x65+x46+x56+x66-25', 'x47+x57+x67+x48+x58+x68+x49+x59+x69-25', 'x71+x81+x91+x72+x82+x92+x73+x83+x93-25', 'x74+x84+x94+x75+x85+x95+x76+x86+x96-25', 'x77+x87+x97+x78+x88+x98+x79+x89+x99-25']
        # cuadrados:
        lista = f
        lista += p
        lista += m
"""
