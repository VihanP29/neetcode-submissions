class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        cntr = 0
        x = len(grid) 
        y = len(grid[0])
        def ctg(a,b):
            return y*a + b
        def search(a, b):
            pos = ctg(a,b)
            # Up
            if a != 0 and grid[a-1][b] == '1':
                if pos-y not in seen:
                    seen.add(pos-y)
                    search(a-1,b)
            # Down
            if a != x-1 and grid[a+1][b] == '1':
                if pos+y not in seen:
                    seen.add(pos+y)
                    search(a+1,b)
            # Left
            if b != 0 and grid[a][b-1] == '1':
                if pos-1 not in seen:
                    seen.add(pos-1)
                    search(a,b-1)
            # Right
            if b != y-1 and grid[a][b+1] == '1':
                if pos+1 not in seen:
                    seen.add(pos+1)
                    search(a,b+1)

        for i in range(x):
            for j in range(y):
                if grid[i][j] == '1' and ctg(i,j) not in seen:
                    seen.add(ctg(i,j))
                    search(i,j)
                    cntr += 1

        return cntr

        
        