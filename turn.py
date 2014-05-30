
# -*- coding: utf-8 -*-
import copy

class Turn:
	def right(self,grid):
		#右は1です
		zero = []
		gridt = copy.deepcopy(grid)
		for i in range(0,len(gridt)):
			zeroc = 0
			while 0 in gridt[i]:
				gridt[i].remove(0)
			if len(gridt[i]) != 0:
				for j in range(0,len(gridt[i])-1):
					if gridt[i][len(gridt[i])-j-1] == gridt[i][len(gridt[i])-j-2] :
						gridt[i][len(gridt[i])-j-2] = gridt[i][len(gridt[i])-j-1] * 2
						gridt[i].pop(len(gridt[i])-j-1)
						#ここで2048用の独自の処理を加える。2240や2244の時の対策。
						if len(gridt[i]) - j > 2 and gridt[i][0] == gridt[i][1]:
							gridt[i][0] = gridt[i][1]*2
							gridt[i].pop(1)
							break
						else:
							break
			while len(gridt[i]) != 4:
				gridt[i].insert(0, 0)
				zero.append([i,zeroc])
				zeroc = zeroc + 1
		return [gridt,zero]

	def left(self,grid):
		#左は3です
		global zero
		zero = []
		gridt = copy.deepcopy(grid)
		for i in range(0,len(gridt)):
			zeroc = 0
			while 0 in gridt[i]:
				gridt[i].remove(0)
			if len(gridt[i]) != 0:
				for j in range(0,len(gridt[i])-1):
					if gridt[i][j] == gridt[i][j+1] :
						gridt[i][j] = gridt[i][j] * 2
						gridt[i].pop(j+1) 
						if len(gridt[i])-j > 2 and gridt[i][j+1] == gridt[i][j+2]:
							gridt[i][j+1] = gridt[i][j+2]*2
							gridt[i].pop(j+2)
							break
						else:
							break
			while len(gridt[i]) != 4:
				gridt[i].append(0)
				zero.append([i,3-zeroc])
				zeroc = zeroc + 1
		return [gridt,zero]

	def up(self,grid):
		#上は0です
		global zero
		zero = []
		#gridtのtはtemporaryのtだよっ！一回左右に変換してからやり直す
		gridtt = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		gridt = copy.deepcopy(grid)
		for i in range(0,len(gridt)):
			for j in range(0,len(gridt[i])):
				gridtt[i][j] = gridt[j][i]
		#move left
		for i in range(0,len(gridtt)):
			zeroc = 0
			while 0 in gridtt[i]:
				gridtt[i].remove(0)
			if len(gridtt[i]) != 0:
				for j in range(0,len(gridtt[i])-1):
					if gridtt[i][j] == gridtt[i][j+1] :
						gridtt[i][j] = gridtt[i][j] * 2
						gridtt[i].pop(j+1) 
						if len(gridtt[i])-j > 2 and gridtt[i][j+1] == gridtt[i][j+2]:
							gridtt[i][j+1] = gridtt[i][j+2]*2
							gridtt[i].pop(j+2)
							break
						else:
							break
			while len(gridtt[i]) != 4:
				gridtt[i].append(0)
				zero.append([i,3-zeroc])
				zeroc = zeroc + 1
		for i in range(0,len(gridt)):
			for j in range(0,len(gridt)):
				gridt[i][j] = gridtt[j][i]
		for i in range(0,len(zero)):
			zero[i].reverse()
		return [gridt,zero]

	def down(self,grid):
		#下は2です
		#gridtのtはtemporaryのtだよっ！一回左右に変換してからやり直す
		global zero
		zero = []
		gridtt = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		gridt = copy.deepcopy(grid)
		for i in range(0,len(gridt)):
			for j in range(0,len(gridt[i])):
				gridtt[i][j] = gridt[j][i]
		#move right
		for i in range(0,len(gridtt)):
			zeroc = 0
			while 0 in gridtt[i]:
				gridtt[i].remove(0)
			if len(gridtt[i]) != 0:
				for j in range(0,len(gridtt[i])-1):
					if gridtt[i][j] == gridtt[i][j+1] :
						gridtt[i][j+1] = gridtt[i][j] * 2
						gridtt[i].pop(j)
						#ここで2048用の独自の処理を加える。2240や2244の時の対策。
						if len(gridtt[i])-j > 2 and gridtt[i][j+1] == gridtt[i][j+2]:
							gridtt[i][j+1] = gridtt[i][j+2]*2
							gridtt[i].pop(j+2)
							break
						else:
							break
			while len(gridtt[i]) != 4:
				gridtt[i].insert(0, 0)
				zero.append([i,zeroc])
				zeroc = zeroc + 1
		for i in range(0,len(gridt)):
			for j in range(0,len(gridt)):
				gridt[i][j] = gridtt[j][i]
		for i in range(0,len(zero)):
			zero[i].reverse()
		return [gridt,zero]
		
if __name__=="__main__":
	grid = Turn()
	grid.grid = () #このへんで呼び出し

#print(grid.right())っていうかんじで
