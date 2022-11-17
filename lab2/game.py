import random
from queue import Queue
import time
import psutil
import os
from math import inf

class Game:
    def __init__(self) -> None:
        self.queens = [
            (0,0),
            (0,1),
            (0,2),
            (0,3),
            (0,4),
            (0,5),
            (0,6),
            (0,7),
        ]


    def shuffle_queens(self):
        self.queens = []
        for i in range(8):
            self.queens.append((random.randint(0,7),i))

    def showField(self, queens):
        print('-------------------------------------------------')
        for i in range(8):
            print('|  ' , end='')
            for j in range(8):
                if self.queen_pos(queens,j,i):
                    print(str(1) + '  |  ' , end='')
                else:
                    print(str(0) + '  |  ' , end='')

            print()
            print('-------------------------------------------------')

    def queen_pos(self,queens, x, y):
        for queen in queens:
            if x == queen[0] and y == queen[1]:
                return True
        return False


# 

    def findSolution_RBFS(self):

        return self.RBFS_Search(self.queens, inf , 0)[0]

    def RBFS_Search(self, queens, f_limit, d):
        
        if not self.conflict(queens):

            return (queens, 0)

        moves = self.get_moves(queens)
        f = [0 for i in range(len(moves))]
        
        for i in range(len(moves)):
            f[i] = self.f2(moves[i]) + d

        while True:
            
            best = min(f)

            if best > f_limit:
                return (False, best)

            alternative = self.get_alternative(f)
            
            result , f[f.index(best)]= self.RBFS_Search( moves[ f.index(best) ] , min ( alternative, f_limit ), d+1 )

            if result:
                return (result, 0)

    def findSolution_RBFS_with_limits(self):

        return self.RBFS_Search(self.queens, inf , 0, time.time())[0]


    def RBFS_Search_with_limits(self, queens, f_limit, d, time):
        

        if time.time() - t0 > 1800 or psutil.Process(os.getpid()).memory_info().rss > 1024**3:
                print('task too complex')
                return (False, 0)

        if not self.conflict(queens):

            return (queens, 0)

        moves = self.get_moves(queens)
        f = [0 for i in range(len(moves))]
        
        for i in range(len(moves)):
            f[i] = self.f2(moves[i]) + d

        while True:
            
            best = min(f)

            if best > f_limit:
                return (False, best)

            alternative = self.get_alternative(f)
            
            result , f[f.index(best)]= self.RBFS_Search( moves[ f.index(best) ] , min ( alternative, f_limit ), d+1 )

            if result:
                return (result, 0)

    def get_alternative(self, f):
        copy = f.copy()
        copy.pop( f.index( min(f) ) )
        return min(copy)

    def f2(self, queens):
        counter = 0
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    counter += 1
        return counter

    def findSolution_BFS_with_limits(self):
        quene = Queue()
        t0 = time.time()
        quene.put(self.queens)  
     
        while not quene.empty():
            
            if time.time() - t0 > 1800 or psutil.Process(os.getpid()).memory_info().rss > 1024**3:
                print('task too complex')
                return False


            queens = quene.get()
            if not self.conflict(queens):

                return queens

            for move in self.get_moves(queens):
                quene.put(move)


    def findSolution_BFS(self):
        quene = Queue()
        t0 = time.time()
        quene.put(self.queens)  
     
        while not quene.empty():


            if time.time() - t0 > 600:
                return False


            queens = quene.get()
            if not self.conflict(queens):

                return queens

            for move in self.get_moves(queens):
                quene.put(move)


        

    def get_moves(self, queens):
        moves = []
        for i in range(len(queens)):
            for j in range(queens[i][0]):
                initital_state = queens.copy()
                initital_state[i] = (j , initital_state[i][1])
                moves.append(initital_state)

            for j in range(queens[i][0]+1, 8):

                initital_state = queens.copy()
                initital_state[i] = (j , initital_state[i][1])
                # print(initital_state)
                moves.append(initital_state)
        
        return moves

        
    def conflict(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

game = Game()

# game.queens = [
#     (5,0),
#     (6,1),
#     (2,2),
#     (7,3),
#     (3,4),
#     (3,5),
#     (1,6),
#     (6,7)

# ]

game.shuffle_queens()

print("BFS Search:")
game.showField(game.queens)
t0 = time.time()
game.findSolution_BFS_with_limits()
print('time: ', time.time()-t0)
game.showField(game.queens)


print('-----')


# game.queens = [
#     (5,0),
#     (6,1),
#     (2,2),
#     (7,3),
#     (3,4),
#     (3,5),
#     (1,6),
#     (6,7)
# ]
game.shuffle_queens()

print("RBFS Search:")
game.showField(game.queens)
t0 = time.time()
game.findSolution_RBFS()
print('time: ', time.time()-t0)
game.showField(game.queens)

    
