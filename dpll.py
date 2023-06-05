import logging

class Dpll:
    def __init__(self) -> None:
        self.color = {"R":"Red", "G":"Green", "B":"Blue", "Y":"Yellow"}

    def get_atoms(self, S):
        """Given S (clauses) as input, returns a sorted list of atoms in S"""
        atoms = []
        for clause in S:
            atoms_temp = clause.split()
            atoms = atoms + atoms_temp
        
        atoms = list(set(atoms))
        
        atoms_sorted = sorted(atoms, key=lambda x: x.replace("!", ""))

        return atoms_sorted
    
    def get_V(self, atoms):
        """Given atoms, generate V dictionary"""
        v_list = []
        for a in atoms:
            if a[0]=="!":
                v_list.append(a[1:])
            else:
                v_list.append(a)
        v_list = list(set(v_list))
        return {k: None for k in v_list}

    def find_pure_literal(self, atoms):
        """atoms input is already a sorted list, returns the first pure symbol encountered"""
        for atom in atoms:
            if atom[0] == "!" and atom[1:] not in atoms:
                return atom[1:], False
            elif atom[0] != "!" and "!" + atom not in atoms:
                return atom, True
            else:
                return None, None

    def find_single_literal(self, S):
        """Given S (clauses) return a single literal"""
        single_literals = []
        for clause in S:
            atoms = self.get_atoms([clause])
            if len(atoms)==1:
                single_literals += atoms

        if single_literals:
            single_literals = list(set(single_literals))     
            single_literal = sorted(single_literals, key=lambda x: x.replace("!", ""))[0]
            if single_literal[0] == "!":
                return single_literal[1:], False
            else:
                return single_literal, True 
        else:
            return None, None
    
    def convert_to_solution(self):
        """Convert solution to readable format"""
        for k,v in self.soln_V.items():
            if v is None:
                self.soln_V[k] = False
        logging.info(self.soln_V)
        soln_list = [k for k, v in self.soln_V.items() if v == True]
        soln_output_list = []
        for node_col in soln_list:
            soln_output_list.append(node_col.split('_')[0] + " = " + self.color[node_col.split('_')[1]])

        return sorted(soln_output_list)
    
    def propagate(self, S, V):
        S_keep = []
        for clause in S:
            atoms_c = self.get_atoms([clause])
            keep_clause = True
            atoms_to_drop = []
            for a in atoms_c:
                if a[0] == "!":
                    if V[a[1:]] == False:
                        keep_clause = False
                        break
                    if V[a[1:]] == True:
                        atoms_to_drop.append(a)

                if a[0] != "!":
                    if V[a] == True:
                        keep_clause = False 
                        break
                    if V[a] == False:
                        atoms_to_drop.append(a)

            if set(atoms_c) == set(atoms_to_drop):
                return False, S

            if keep_clause:
                if atoms_to_drop:
                    updated_atoms = [a for a in atoms_c if a not in atoms_to_drop]
                    S_keep.append(" ".join(updated_atoms))
                else:
                    S_keep.append(clause)

        return True, S_keep

        
    def dp(self, S):

        atoms = self.get_atoms(S)
        V = self.get_V(atoms)

        if self.dp1(S, V):
            return self.convert_to_solution()
        else:
            return None
    
    def dp1(self, S, V):
        
        cont_solve, S = self.propagate(S, V)

        if not cont_solve:
            return False
        
        if not S:
            self.soln_V = V
            return True
        
        # easy case
        pure_literal, pure_literal_assign = self.find_pure_literal(self.get_atoms(S))
        if pure_literal:
            V[pure_literal] = pure_literal_assign
            logging.info("easy case: pure literal {0}={1}".format(pure_literal, pure_literal_assign))
            return self.dp1(S, V)
        
        single_literal, single_literal_assign = self.find_single_literal(S)
        if single_literal:
            V[single_literal] = single_literal_assign
            logging.info("easy case: unit literal {0}".format(single_literal))
            return self.dp1(S, V)

        # hard case
        atom_guess = self.get_atoms(S)[0]
        if atom_guess[0] == "!":
            atom_guess = atom_guess[1:]
        
        V[atom_guess] = True
        logging.info("hard case: guess {0}=true".format(atom_guess))
        S1 = S.copy()
        V1 = V.copy()
        if self.dp1(S1, V1):
            return True
        
        V[atom_guess] = False
        logging.info("contradiction: backtrack guess {0}=false".format(atom_guess))
        
        S1 = S.copy()
        V1 = V.copy()
        return self.dp1(S1,V1)
