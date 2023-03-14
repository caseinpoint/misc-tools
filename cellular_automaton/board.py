from csv import reader
from statistics import fmean
from random import choices


class Board:
    def __init__(self, width, height, cells, born=None, survive=None,
                 alive='█', dead=' '):
        self.width = width
        self.height = height
        self.cells = cells
        self.born = born if born is not None else {3}
        self.survive = survive if survive is not None else {2, 3}
        self.alive = alive
        self.dead = dead
        self.generation = 1

        # for analysis:
        self.live_neighbors_avgs = []

    def __repr__(self):
        return f'<Board width={self.width} height={self.height}>'

    @staticmethod
    def generate_cells(width, height, weights=None, alive='█', dead=' '):
        if weights is None:
            weights = (1, 4)

        cells = []
        for _ in range(height):
            cells.append(choices((alive, dead), weights=weights, k=width))
        return cells

    @classmethod
    def random_board(cls, width, height, weights=None, born=None,
                     survive=None, alive='█', dead=' '):
        cells = cls.generate_cells(width, height, weights, alive, dead)
        return cls(width=width, height=height, cells=cells, born=born,
                   survive=survive, alive=alive, dead=dead)

    @classmethod
    def from_file(cls, filename, born=None, survive=None, alive='█', dead=' '):
        """Return a Board from a .csv file."""

        with open(filename) as f:
            csv_reader = reader(f)
            cells = list(csv_reader)

        height = len(cells)
        width = len(cells[0])

        return cls(width=width, height=height, cells=cells, born=born,
                   survive=survive, alive=alive, dead=dead)

    def print_cells(self):
        rows = []
        for row in self.cells:
            rows.append(''.join(row))
        print('\n'.join(rows))

    def _count_live_neighbors(self, cell_h, cell_w):
        live = 0

        for h in range(cell_h - 1, cell_h + 2):
            if h < 0 or h >= self.height:
                continue

            for w in range(cell_w - 1, cell_w + 2):
                if w < 0 or w >= self.width:
                    continue
                if h == cell_h and w == cell_w:
                    # don't count passed in cell as neighbor
                    continue

                if self.cells[h][w] == self.alive:
                    live += 1

        return live

    def tick(self):
        self.generation += 1

        new_cells = []
        for _ in range(self.height):
            new_cells.append([None] * self.width)

        live_neighbors = []
        for h in range(self.height):
            for w in range(self.width):
                cell = self.cells[h][w]
                num_live = self._count_live_neighbors(h, w)

                live_neighbors.append(num_live)

                if cell == self.dead:
                    if num_live in self.born:
                        cell = self.alive
                elif cell == self.alive:
                    if num_live not in self.survive:
                        cell = self.dead

                new_cells[h][w] = cell

        self.live_neighbors_avgs.append(fmean(live_neighbors))
        self.cells = new_cells
