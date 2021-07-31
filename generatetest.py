from re import L
from csp import Constraint, CSP
from typing import Dict, List, NamedTuple, Optional, Tuple

import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="ta2",
)

cursor = db.cursor()
ta = "select * from app_ta_matkul_kelas"
cursor.execute(ta)
tas = cursor.fetchall()


akun = "select * from app_akun"
cursor.execute(akun)
akuns = cursor.fetchall()


<<<<<<< HEAD
dosen="SELECT dms.no_dosen_id,dms.no_kelas_id,dms.no_matkul_id,matkul.sks,matkul.kategori_id FROM app_dosen_matkul_kelas dms INNER JOIN app_matkul matkul ON dms.no_matkul_id=matkul.id ORDER BY kategori_id ASC"
cursor.execute(dosen)
dosens = cursor.fetchall()
=======
pmk = "SELECT * from pmk limit 20"
cursor.execute(pmk)
pmks = cursor.fetchall()
>>>>>>> b86ae4fa8aada8b8e250adb3724015b3ca9febc0


hari = "select * from app_hari"
cursor.execute(hari)
haris = cursor.fetchall()

kelas = "select * from app_kelas"
cursor.execute(kelas)
kelass = cursor.fetchall()

matkul = "select * from app_matkul"
cursor.execute(matkul)
matkuls = cursor.fetchall()

kategori = "select * from app_kategori"
cursor.execute(kategori)
kategoris = cursor.fetchall()

sesi = "select * from app_sesi"
cursor.execute(sesi)
sesis = cursor.fetchall()

# [print(list(list(row)))for row in dosens]

Grid = List[List[List[Tuple]]]


class GridSchedule(NamedTuple):
    row: int
    column: int

<<<<<<< HEAD
def generate_grid(rows: int, columns: int)->Grid:
       return [[[] for j in range(columns)] for i in range(rows)]
=======
>>>>>>> b86ae4fa8aada8b8e250adb3724015b3ca9febc0

def generate_grid(rows: int, columns: int) -> Grid:
    return [[[] for j in range(columns)] for i in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))

<<<<<<< HEAD
 
   

def generate_domain(dms: Tuple,grid: Grid) -> List[List[GridSchedule]]:
=======

def generate_domain(grid: Grid) -> List[List[GridSchedule]]:
>>>>>>> b86ae4fa8aada8b8e250adb3724015b3ca9febc0
    domain: List[List[GridSchedule]] = []

    height: int = len(grid)
    width: int = len(grid[0])
    for row in range(height):
        for col in range(width):
<<<<<<< HEAD
                domain.append([GridSchedule(row, col)])
=======
            domain.append([GridSchedule(row, col)])
>>>>>>> b86ae4fa8aada8b8e250adb3724015b3ca9febc0
    return domain


class GenerateConstraint(Constraint[str, List[GridSchedule]]):
    def __init__(self, pmks: List[Tuple]) -> None:
        super().__init__(pmks)
        self.pmks: List[Tuple] = pmks

<<<<<<< HEAD
    def satisfied(self, assignment: Dict[Tuple, List[GridSchedule]]) -> bool:
         for dms1 in assignment.items():
            # print(assignment.items())
            for dms2 in assignment.items():
                if dms1[0] == dms2[0]:
                    return False
                if dms1[1] == dms2[1]:
                    return False
            return True
=======
    def satisfied(self, assignment: Dict[Tuple, List[GridSchedule]]) -> None:
        # if there are any duplicates grid locations then there is an overlap
        print(assignment)
        # all_locations = [locs for values in assignment.values() for locs in  values]
        # return len(set(all_locations)) == len(all_locations)
        return True
>>>>>>> b86ae4fa8aada8b8e250adb3724015b3ca9febc0


if __name__ == "__main__":
    jumlah_sesi = len(sesis)
    jumlah_hari = len(haris)

    grid: Grid = generate_grid(jumlah_hari, jumlah_sesi)
    pmk: List[Tuple] = [row for row in pmks]
    location: Dict[Tuple, List[List[GridSchedule]]] = {}
<<<<<<< HEAD
    for items in dms:
        location[items]= generate_domain(items,grid)

    csp: CSP[Tuple, List[GridSchedule]] = CSP(dms, location)
    csp.add_constraint(GenerateConstraint(dms))
=======
>>>>>>> b86ae4fa8aada8b8e250adb3724015b3ca9febc0

    for items in pmk:
        location[items] = generate_domain(grid)

<<<<<<< HEAD
    solution: Optional[Dict[Tuple, List[GridSchedule]]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)

  
=======
    csp = CSP(pmk, location)
    csp.add_constraint(GenerateConstraint(pmk))

    solution: Optional[Dict[Tuple, List[GridSchedule]]
                       ] = csp.backtracking_search()
    # if solution is None:
    #     print("No solution found!")
    # else:
    #     for word, grid_locations in solution.items():
    #         for index, letter in enumerate(word):
    #             (row, col) = (grid_locations[index].row, grid_locations[index].column)
    #             grid[row][col] = letter
    #     display_grid(grid)
>>>>>>> b86ae4fa8aada8b8e250adb3724015b3ca9febc0
