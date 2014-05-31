# -*- coding: utf-8 -*-

import json
import copy
import urllib.request
import random
import sys
import turn
from multiprocessing import Pool

class Grid:
	def __init__(self):
		self.est = []

	class turn(turn.Turn):
		pass

	def nexs(self,loop):
		movekey = {0:self.turn.up,1:self.turn.right,2:self.turn.down,3:self.turn.left}
		self.est = [0,0,0,0]
		for i in range (0,4):
			movelist = movekey[i](self,self.grid)
			if movelist[0] != self.grid:
				self.est[i] = [self.hen(movelist[0],movelist[1])]
			else:
				self.est[i] = []
		p = Pool(1)
		self.est = list(p.map(self.ret,[0,1,2,3]))
		self.est.sort()
		self.est.reverse()
		print(self.est)
		r = self.est[0][2]
		return(r)

	def ret(self,i):
		if self.est[i] != []:
			for j in range(0,3):
				#loop回先読みする。先読みした項の数から考えていく
				self.est[i] = self.assem(self.est[i])
			if self.est[i] != []:
				for j in range(len(self.est[i])):
					self.est[i][j] = self.count(self.est[i][j])
				self.est[i] = [max(self.est[i]),len(self.est[i]),i]
		else:
			self.est[i] = [0,0,i]
		return(self.est[i])

	def assem(self,gridlist):
		#与えられたgridのリストに対して予測したものを返す関数
		gridt = []
		for i in range(0,len(gridlist)):
			right = self.turn.right(self,gridlist[i])
			if right[0] != gridlist[i]:
				gridt.append(self.hen(right[0],right[1]))
			left = self.turn.left(self,gridlist[i])
			if left[0] != gridlist[i]:
				gridt.append(self.hen(left[0],left[1]))
			up = self.turn.up(self,gridlist[i])
			if up[0] != gridlist[i]:
				gridt.append(self.hen(left[0],left[1]))
			down = self.turn.down(self,gridlist[i])
			if down[0] != gridlist[i]:
				gridt.append(self.hen(down[0],down[1]))
		return(gridt)

	def count(self,grid):
		global re
		#評価
		kazu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		#kazuは盤上の数字の個数
		for i in range(0,len(grid)):
			kazu[0] = grid[i].count(0) + kazu[0]
			for j in range(1,len(kazu)):
				kazu[j] = grid[i].count(2**j) + kazu[j]
			#数を数えている。0は特例
		if re<=50:
			hyouka = kazu[0]*800
		elif 50<re<=900:
			hyouka = kazu[0]*1500
		else:
			hyouka = kazu[0]*3000
		#盤上を評価する。0が5点、それ以外は1.7*i点→素数にすると簡単に判別できるかも？
		for i in range(1,len(kazu)):
			if kazu[i] != 0:
				hyouka = int(kazu[i]*(1.7**(i*2))) + hyouka
		return hyouka

	def move(self,r,url):
		#サーバーに送ってgridを返すもの。同じだったらランダムで入れ替わる
		global dic_jdata
		json_data = urllib.request.urlopen('http://' + url +'hi/state/' + dic_jdata['session_id'] + '/move/' + str(r) +'/json')
		str_jdata = json_data.read().decode('utf-8')
		if dic_jdata['grid'] != json.loads(str_jdata)['grid']:
			dic_jdata = json.loads(str_jdata)
			r = random.randint(0,3)
			print(str(re) + "回目の移動")
			direction = ["↑","→","↓","←"]
			print("direction: " + direction[r])
			grid = dic_jdata['grid']
			for i in range(0,len(grid[0])):
				print (grid[i])
			print ("Score: " + str(dic_jdata['score']))
			cnt = self.count(grid)
			print ("評価点: " + str(cnt) + "\n")
			self.grid = grid
		else:
			r = random.randint(0,3)
			print('hello world')
			self.move(r,url)


	def hen(self,grid,zero):
		#ランダムに2を入れて返す関数
		if len(zero) != 0:
			gridtem =[0]*len(zero)
			i  = random.randint(0,len(zero)-1)
			gridtem[i] = copy.deepcopy(grid)
			gridtem[i][zero[i][0]][zero[i][1]] = 2
			return(gridtem[i])
		else:
			return(grid)

def yaruze(url):
	#動くところ	
	global re
	re = 1
	grid = Grid()
	grid.grid = start(url)
	while dic_jdata['over'] != True:
		if re<-80:
			#moveしてないからgrid.grid設定されてないなのです！
			grid.move(random.randint(0,2),url)
		elif -80<= re<500:
			#実際に先読みするのはこれ+1回
			grid.move(grid.nexs(3),url)
		elif 500<= re <800:
			grid.move(grid.nexs(4),url)
		else:
			grid.move(grid.nexs(5),url)
		re = re + 1
	print("over!")
	#ファイルの書き出し。統計のためです
	file = open('shutz.txt', mode='a')
	file.write(str(dic_jdata['score']) +" " + str(grid.grid) + str(re))
	file.write('\n')
	file.close()

def start(url):
	json_data = urllib.request.urlopen('http://' + url +'hi/start/size/4/tiles/2/victory/20/rand/2/json')
	str_jdata = json_data.read().decode('utf-8')
	global dic_jdata
	grid = [0,0,0,0]
	dic_jdata = json.loads(str_jdata)	
	grid = dic_jdata['grid']
	for i in range(0,len(grid)):
		print(grid[i])
	#盤を表示する
	print ("score: " + str(dic_jdata['score']) + "\n")
	return(grid)

if __name__ == "__main__":
	u = 0
	u = int(input("URL(1:outside, 2:ring): "))
	if u == 1:
		url = "2048.semantics3.com/"
	elif u == 2:
		url = "ring:2048/"
	else:
		print("ha????????")
		sys.exit()
	yaruze(url)	
