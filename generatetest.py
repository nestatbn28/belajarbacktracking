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


pmk = "SELECT * from pmk limit 20"
cursor.execute(pmk)
pmks = cursor.fetchall()


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


def generate_grid(rows: int, columns: int) -> Grid:
    return [[[] for j in range(columns)] for i in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def generate_domain(grid: Grid) -> List[List[GridSchedule]]:
    domain: List[List[GridSchedule]] = []

    height: int = len(grid)
    width: int = len(grid[0])
    for row in range(height):
        for col in range(width):
            domain.append([GridSchedule(row, col)])
    return domain


class GenerateConstraint(Constraint[str, List[GridSchedule]]):
    def __init__(self, pmks: List[Tuple]) -> None:
        super().__init__(pmks)
        self.pmks: List[Tuple] = pmks

    def satisfied(self, assignment: Dict[Tuple, List[GridSchedule]]) -> None:
        # if there are any duplicates grid locations then there is an overlap
        print(assignment)
        # all_locations = [locs for values in assignment.values() for locs in  values]
        # return len(set(all_locations)) == len(all_locations)
        return True


if __name__ == "__main__":
    jumlah_sesi = len(sesis)
    jumlah_hari = len(haris)

    grid: Grid = generate_grid(jumlah_hari, jumlah_sesi)
    pmk: List[Tuple] = [row for row in pmks]
    location: Dict[Tuple, List[List[GridSchedule]]] = {}

    for items in pmk:
        location[items] = generate_domain(grid)

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
