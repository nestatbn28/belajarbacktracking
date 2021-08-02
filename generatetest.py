from re import L
from csp import Constraint, CSP
from typing import Dict, List, NamedTuple, Optional, Tuple

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database="ta2",
)

cursor = db.cursor()



akun="select * from app_akun"
cursor.execute(akun)
akuns = cursor.fetchall()


dosen="select * from pmk limit 10"
cursor.execute(dosen)
dosens = cursor.fetchall()


hari="select * from app_hari"
cursor.execute(hari)
haris = cursor.fetchall()

kelas="select * from app_kelas"
cursor.execute(kelas)
kelass = cursor.fetchall()

matkul="select * from app_matkul"
cursor.execute(matkul)
matkuls = cursor.fetchall()


sesi="select * from app_sesi"
cursor.execute(sesi)
sesis = cursor.fetchall()

# [print(list(list(row)))for row in dosens]

Grid = List[List[Tuple]]

class GridSchedule(NamedTuple):
    row: int
    column: int

def generate_grid(rows: int, columns: int)->Grid:
       return [[[] for j in range(columns)] for i in range(rows)]

def display_grid(grid: Grid)->None:
    for row in grid:
        print("".join(row))

 
   

def generate_domain(dms: Tuple,grid: Grid) -> List[List[GridSchedule]]:
    domain: List[List[GridSchedule]] = []
    
    height: int = len(grid)
    width: int = len(grid[0])
    for row in range(height):
        for col in range(width):
            domain.append([GridSchedule(row, col)])
    return domain


class GenerateConstraint(Constraint[Tuple, List[GridSchedule]]):
    def __init__(self, dms: List[Tuple]) -> None:
        super().__init__(dms)
        self.words: List[Tuple] = dms

    def satisfied(self, assignment: Dict[Tuple, List[GridSchedule]]) -> bool:
         for dms1 in assignment.items():
            for dms2 in assignment.items():
                if dms1[1] == dms2[1]:
                    return False
                if dms1[2] == dms2[2]:
                    return False
            return True
 

if __name__ == "__main__":
    jumlah_sesi = len(sesis)
    jumlah_hari = len(haris)
    
    grid: Grid=generate_grid(jumlah_hari, jumlah_sesi)
    dms : List[Tuple] =  [row for row in dosens]
    
    
    location: Dict[Tuple, List[List[GridSchedule]]] = {}
    for items in dms:
        location[items]= generate_domain(items,grid)

    csp: CSP[Tuple, List[GridSchedule]] = CSP(dms, location)
    csp.add_constraint(GenerateConstraint(dms))


    solution: Optional[Dict[Tuple, List[GridSchedule]]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)

  