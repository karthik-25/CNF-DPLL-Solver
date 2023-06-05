import sys

from io_processor import IO_Processor
from graph import Graph
from dpll import *

def main():
    iop = IO_Processor()
    iop.parse_input(sys.argv[1:])

    if iop.is_verbose:
        logging.basicConfig(level=logging.INFO, format='%(message)s')
    
    g = Graph()
    g.build_graph(iop.input_file)
    
    clauses = g.graph_constraints(iop.valid_colors)

    for clause in clauses:
        logging.info(clause)
    logging.info('\n')
    
    d = Dpll()
    output = d.dp(clauses)

    if output:
        logging.info("\n")
        for o in output:
            print(o)
    else:
        logging.info("\n")
        print('No solution found for input graph [{0}] with {1} colors.'.format(iop.input_file, iop.ncolors))


if __name__ == "__main__":
    main()