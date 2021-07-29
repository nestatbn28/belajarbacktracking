from csp import Constraint, CSP
from typing import Dict, List, Optional, Tuple


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        # q1c = queen 1 column, q1r = queen 1 row
        #print(assignment.items())
        #print(self.columns)
        
        for q1c, q1r in assignment.items():
            print(assignment.items())
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment: 
                    #print(assignment)  
                    q2r: int = assignment[q2c] # q2r = queen 2 row
                    print (q2r)
                    percobaan : Tuple = [q1c, q1r,q2c, q2r]
                    print(percobaan)
                    # print(sorted(percobaan))
                    if q1r == q2r: # same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c): # same diagonal?
                        return False
        return True # no conflict


if __name__ == "__main__":
    columns: List[int] = [1, 2, 3, 4]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4]
    #print(rows)
    csp: CSP[int, int] = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)