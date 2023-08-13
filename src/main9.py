import time
import timeit

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
from b9x9 import Sudoku9


class SudokuGame(FloatLayout):
    # Initialize the grid of text inputs
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_inputs = []
        self.error_messages = []
        self.tiempos = []
        self.sol9 = []

        grid = self.ids["grid"]
        for i in range(81):
            text_input = SudokuCell()
            grid.add_widget(text_input)
            self.text_inputs.append(text_input)

        # Test grid: supposedly the most complicated Sudoku in the world
        # self.text_inputs[ 0].text = "8";
        # self.text_inputs[11].text = "3";
        # self.text_inputs[12].text = "6";
        # self.text_inputs[19].text = "7";
        # self.text_inputs[22].text = "9";
        # self.text_inputs[24].text = "2";
        # self.text_inputs[28].text = "5";
        # self.text_inputs[32].text = "7";
        # self.text_inputs[40].text = "4";
        # self.text_inputs[41].text = "5";
        # self.text_inputs[42].text = "7";
        # self.text_inputs[48].text = "1";
        # self.text_inputs[52].text = "3";
        # self.text_inputs[56].text = "1";
        # self.text_inputs[61].text = "6";
        # self.text_inputs[62].text = "8";
        # self.text_inputs[65].text = "8";
        # self.text_inputs[66].text = "5";
        # self.text_inputs[70].text = "1";
        # self.text_inputs[73].text = "9";
        # self.text_inputs[78].text = "4";

    # Get the value in a given cell
    # Return 0 if no value is specified
    def get_value(self, row, col):
        text = self.text_inputs[9 * row + col].text
        return int(text) if len(text) > 0 else 0

    # Solve the current board
    def solve(self):
        # Read values from the grid
        start = timeit.default_timer()
        values = [[self.get_value(row, col) for col in range(9)] for row in range(9)]
        print(values);

        self.sol9 = Sudoku9(values)
        print(self.sol9)

        if self.sol9.solv():
            print(self.sol9)
            for row in range(9):
                for col in range(9):
                    self.text_inputs[9 * row + col].text = str(self.sol9.get_value(row, col))
            stop = timeit.default_timer()
            tiempo_tardado = stop - start

            tiempo = Tiempo(round(tiempo_tardado, 2))
            self.tiempos.append(tiempo)
            self.add_widget(tiempo)
            Clock.schedule_once(self.remove_tiempo, tiempo_tardado + 3)

        else:
            error_message = ErrorMessage()
            self.error_messages.append(error_message)
            self.add_widget(error_message)
            Clock.schedule_once(self.remove_error_message, 3)

    # Remove the last error message on screen
    def remove_error_message(self, dt):
        error_message = self.error_messages.pop()
        self.remove_widget(error_message)

    def remove_tiempo(self, dt):
        tiempo = self.tiempos.pop()
        self.remove_widget(tiempo)

    # Remove all values on the board
    def clear(self):
        self.sol9 = []
        for text_input in self.ids["grid"].children:
            text_input.text = ""

    def other_solutions(self):
        if not(isinstance(self.sol9, list)):
            if self.sol9.other_solutions():
                print(self.sol9)
                for row in range(9):
                    for col in range(9):
                        self.text_inputs[9 * row + col].text = str(self.sol9.get_value(row, col))
            else:
                error_message = ErrorMessage()
                self.error_messages.append(error_message)
                self.add_widget(error_message)
                Clock.schedule_once(self.remove_error_message, 3)



class SudokuCell(TextInput):
    pass


class ErrorMessage(Label):
    pass


class Tiempo(Label):
    tiempo = StringProperty()

    def __init__(self, tiempo_tardado):
        super(Tiempo, self).__init__()
        self.tiempo = "Tiempo: " + str(tiempo_tardado) + "s"


class SudokuApp(App):
    def build(self):
        return SudokuGame()


if __name__ == '__main__':
    SudokuApp().run()