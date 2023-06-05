import sys

class IO_Processor:
    def __init__(self):
        self.is_verbose = False
        self.ncolors = None
        self.input_file = None
        self.input_parse_fail_str = "Error: Input parsing failed."
        self.all_colors = ['R', 'G', 'B', 'Y']
        self.valid_colors = None

    def parse_input(self, args):
        if len(args)!=2 and len(args)!=3:
            print(self.input_parse_fail_str, "Invalid arguments. Sample command: python solver.py [-v] ncolors input-file")
            sys.exit()

        if "-v" in args:
            self.is_verbose = True
        
        self.input_file = [arg for arg in args if ".txt" in arg][0]
        if not self.input_file:
            print(self.input_parse_fail_str, "Invalid input: input txt file not specified.")
            sys.exit()

        self.ncolors = int([arg for arg in args if arg not in ["-v", self.input_file]][0])
        if not self.ncolors:
            print(self.input_parse_fail_str, "Invalid input: ncolors not specified.")
            sys.exit()
        else:
            self.valid_colors = self.all_colors[:self.ncolors]
