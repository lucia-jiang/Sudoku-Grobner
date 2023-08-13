# Sudoku-Grobner

This project utilizes Grobner basis theory to solve Sudoku puzzles of sizes 9x9, 6x6, and 4x4, as well as their variations. Sudoku puzzles are represented as systems of equations through three distinct approaches: 
1. Sum and product constraints
2. Graph coloring
3. Boolean variables.

The implementation employs `Python` along with the `Kivy` library for the user interface. Moreover, the application is also designed to function on Android devices. 

It's worth noting that utilizing Grobner basis for Sudoku solving isn't as efficient as backtracking, which proves to be much quicker. However, it's important to mention that for the majority of cases, attempting to solve 9x9 sudokus using this method often leads to time exceed limitations. Nevertheless, this project serves as a valuable learning exercise in exploring alternative solving methods and modelizing real life problems into mathematics.

![6x6planteado](https://github.com/lucia-jiang/Sudoku-Grobner/assets/104275311/dcdf923a-14a8-421e-8e28-9e989b750f1b)
