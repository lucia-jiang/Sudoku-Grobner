import time
import timeit

from kivy.app               import App
from kivy.uix.label         import Label
from kivy.uix.textinput     import TextInput
from kivy.uix.floatlayout   import FloatLayout
from kivy.clock             import Clock
from kivy.properties import StringProperty


from b6x6 import Sudoku6

class SudokuGame6(FloatLayout):
    # Initialize the grid of text inputs
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_inputs    = []
        self.error_messages = []
        self.tiempos = []
        self.sol6 = []

        grid = self.ids["grid"]
        for i in range(36):
            text_input = SudokuCell6()
            grid.add_widget(text_input)
            self.text_inputs.append(text_input)

    # Get the value in a given cell
    # Return 0 if no value is specified
    def get_value(self, row, col):
        text  = self.text_inputs[6 * row + col].text
        return int(text) if len(text) > 0 else 0

    # Solve the current board
    def solve(self):
        # Read values from the grid
        start = timeit.default_timer()
        values = [[self.get_value(row, col) for col in range(6)] for row in range(6)]
        print(values);
        # Try to solve the Sudoku

        self.sol6 = Sudoku6(values)
        print(self.sol6)

        if self.sol6.solv():
            print(self.sol6)
            for row in range(6):
                for col in range(6):
                    self.text_inputs[6 * row + col].text = str(self.sol6.get_value(row, col))
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
        self.sol6 = []
        for text_input in self.ids["grid"].children:
            text_input.text = ""

    def other_solutions(self):
        if not(isinstance(self.sol6, list)):
            if self.sol6.other_solutions():
                print(self.sol6)
                for row in range(6):
                    for col in range(6):
                        self.text_inputs[6 * row + col].text = str(self.sol6.get_value(row, col))
            else:
                error_message = ErrorMessage()
                self.error_messages.append(error_message)
                self.add_widget(error_message)
                Clock.schedule_once(self.remove_error_message, 3)





class SudokuCell6(TextInput):
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
        return SudokuGame6()


if __name__ == '__main__':
    SudokuApp().run()
