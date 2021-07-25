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
ta="select * from app_ta_matkul_kelas"
cursor.execute(ta)
tas = cursor.fetchall()


akun="select * from app_akun"
cursor.execute(akun)
akuns = cursor.fetchall()


dosen="SELECT dms.no_dosen_id,dms.no_kelas_id,dms.no_matkul_id,matkul.sks,matkul.kategori_id FROM app_dosen_matkul_kelas dms INNER JOIN app_matkul matkul ON dms.no_matkul_id=matkul.id ORDER BY kategori_id ASC limit 40"
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

kategori="select * from app_kategori"
cursor.execute(kategori)
kategoris = cursor.fetchall()

sesi="select * from app_sesi"
cursor.execute(sesi)
sesis = cursor.fetchall()

# [print(list(list(row)))for row in dosens]

Grid = List[List[Tuple]]

class GridSchedule(NamedTuple):
    row: int
    column: int

def generate_grid(rows: int, columns: int)->Grid:
       return [[[row for row in dosens] for j in range(columns)] for i in range(rows)]

def display_grid(grid: Grid)->None:
    for row in grid:
        print("".join(row))

 
   
def generate_domain(grid: Grid) -> List[List[GridSchedule]]:
    domain: List[List[GridSchedule]] = []
    
    height: int = len(grid)
    width: int = len(grid[0])
    for row in range(height):
        for col in range(width):
            domain.append([GridSchedule(row, col)])
    # print(domain)
    return domain


class GenerateConstraint(Constraint[Tuple, List[GridSchedule]]):
    def __init__(self, dms: List[Tuple]) -> None:
        super().__init__(dms)
        self.words: List[Tuple] = dms

    def satisfied(self, assignment: Dict[Tuple, List[GridSchedule]]) -> bool:
        # if there are any duplicates grid locations then there is an overlap
        # print(assignment)
        # all_locations = [locs for values in assignment.values() for locs in  values]
        # return len(set(all_locations)) == len(all_locations)
        return True

    


 

if __name__ == "__main__":
    jumlah_sesi = len(sesis)
    jumlah_hari = len(haris)
    
    grid: Grid=generate_grid(jumlah_hari, jumlah_sesi)
    dms : List[Tuple] =  [row for row in dosens]
    location: Dict[Tuple, List[List[GridSchedule]]] = {}
    for items in dms:
        location[items]= generate_domain(grid)
    # for dms in dms:
    #         location[dms] = generate_domain(dms, grid)
    csp: CSP[Tuple, List[GridSchedule]] = CSP(dms, location)
    csp.add_constraint(GenerateConstraint(dms))


    # solution: Optional[Dict[Tuple, List[GridSchedule]]] = csp.backtracking_search()
    # if solution is None:
    #     print("No solution found!")
    # else:
    #     for word, grid_locations in solution.items():
    #         for index, letter in enumerate(word):
    #             (row, col) = (grid_locations[index].row, grid_locations[index].column)
    #             grid[row][col] = letter
    #     display_grid(grid)

  