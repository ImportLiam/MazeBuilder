import random

class Cell:
  
   #the most fundamental element of the maze
    
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    
    #acts to separate the cells from one another
    
    def __init__(self, x, y):
        
        #Starting the first cell on the x,y axis in a fully walled state.
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
        
        def has_all_walls (self):
            #checks to see if the cell has its walls
            return all(self.walls.values())
        
        def knock_down_wall(self, other, wall):
            #knock down all walls between the cell's self and other
            self.walls[wall] = False
            other.walls[Cell.wall_pairs[wall]] = False
            
            
class Maze:
    #using a grid of cells
    def __init__(self, nx, ny, ix=0, iy=0):
        #the maze consists of "nx by ny" cells
        
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_map = [[Cell(x, y) for y in range(ny)]for x in range(nx)]
        
    def cell_at(self, x, y):
        #returns the cell obj. as at (x, y)
        
        return self.maze_map[x][y]
    
    def __str__(self):
        #returns a coarse representation of a maze
        
        maze_rows = ['-' * self.nx * 2]
        for y in range (self.ny):
            maze_row = ['|']
            for x in range(self.nx): 
                if self.maze_map[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_rows.append ([('')])
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
        for x in range(self.nx):
            if self.maze_map[x][y].walls['S']:
                maze_row.append(' +')
                
            else:
                maze_row.append(' +')
        maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

def write_svg(self, filename):
    #writes an SVG image of the maze to filename
    
    aspect_ratio = self.nx / self.ny
    padding = 10
    #padding the maze all around the maze by the prescribed amount
    height = 500
    width = int(height * aspect_ratio)
    #height & with of the maze image without padding
    scy, scx = height / self.ny, width / self.nx
    #scaling factors that map maze coordinates to image coordinates
    def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
        #writes a single wall to the SVG image file handle f
        print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)
        
        with open(filename, 'w') as f:
            #SVG pre-stataments with styles
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'.format(width + 2 * padding, height + 2 * padding, -padding, -padding, width + 2 * padding, height + 2 * padding), 
                  file=f)
            print ('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line{', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)
            
            
            for x in range(self.nx):
                for y in range(self.ny):
                    if self.cell_at(x, y).walls['S']:
                        x1, y1, x2, y2, = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
                if self.cell_at(x, y).walls['E']:
                    x1, y1, x2, y2, = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
                    write_wall(f, x1, y1, x2, y2)
         #acript above draws the South & East walls of each cell, if they are present
         #they are the North & West walls of the neighboring cell in general
            
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
            print('</svg>', file=f)
            
def fine_valid_neighbors(self, cell):
    
    delta = [('W', (-1, 0)),
             ('E', (1, 0)),
             ('S', (0, 1)),
             ('N', (0, -1))]
    neighbors = []
    for direction, (dx, dy) in delta:
        x2, y2 = cell.x + dx, cell.y + dy
        if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
            neighbor = self.cell_at(x2, y2)
            if neighbor.has_all_walls():
                neighbors.append((direction, neighbor))
    return neighbors
#Above script draws the North & West maze border which won't have been drawn by the previous script
def make_maze(self):
    n = self.nx * self * ny 
    cell_stack = []
    current_cell = self.cell_at(self.ix, self.iy)
    #above script show total number of cells
    nv = 1
    #total number of visited cells during maze construction
    
    while nv < n:
        neighbors = self.find_valid_neighbors(current_cell)
        
        if not neighbors:
            #a deadend basically, retrace steps
            current_cell = cell_stack.pop()
            continue
            
            direction, next_cell = random.choice(neighbors)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1


nx, ny = 15, 15
#Dimensions of the maze (x=columns, y=rows)
ix, iy = 0, 0


maze = ((nx, ny, ix, iy), maze.make_maze ())

print(maze)
maze.write_svg ('maze.svg')
        
            

            