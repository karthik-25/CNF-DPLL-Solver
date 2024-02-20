# CNF Generator and DPLL solver
Implementation of Conjunctive Normal Form (CNF) generator and Davis–Putnam–Logemann–Loveland (DPLL) algorithm solver

# Scripts
1. graph.py contains the code for Graph and GraphNode classes. It contains the logic for building a graph and generating CNF.

2. io_processor.py contains the code for IO_Processor class. It contains the logic for parsing
the user input via CLI

3. dpll.py contains the code for Dpll class. It contains the code for DPLL solver.

4. solver.py contains the main function and it is the script to run via CLI.

# Run Scripts
Please run solver.py as follows:
python3 solver.py [-v] n input_filename

-v: toggle verbose. Optional argument
n: number of colors. Required argument.
input_filename: input graph file. Must be a text file with ".txt" extension. Required argument.

Sample Commands:
python3 solver.py 4 ./files/us48.txt
python3 solver.py -v 4 ./files/us48.txt
python3 solver.py 3 ./files/triangle.txt
python3 solver.py -v 3 ./files/oz.txt
python3 solver.py -v 2 ./files/tiny.txt

# References
- Textbook
- https://cs.nyu.edu/~davise/ai/dp.txt
- https://stackoverflow.com/questions/61810643/how-do-i-make-the-sorted-function-ignore-some-characters
- https://stackoverflow.com/questions/8866652/determine-if-2-lists-have-the-same-elements-regardless-of-order
- https://www.programiz.com/python-programming/methods/dictionary/copy
- https://www.w3schools.com/python/gloss_python_join_lists.asp
- https://docs.python.org/3/howto/logging.html
- https://realpython.com/python-logging/
