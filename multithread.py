# -*- coding: utf-8 -*-

import json
import urllib.request
import random
import sys
import copy
import turn
from multiprocessing import Pool

class Grid:
	class turn(turn.Turn):
		pass

	def zero(self):
		zero = 0
		for i in range(4):
			zero = self.grid[i].count(0) + zero
		return(zero)

	def nexs(self):
		movekey = {0:self.turn.up,1:self.turn.right,2:self.turn.down,3:self.turn.left}
		self.est = [0,0,0,0]
		for i in range (0,4):
			movelist = movekey[i](self,self.grid)
			if movelist[0] != self.grid:
				self.est[i] = [self.hen(movelist[0],movelist[1])]
			else:
				self.est[i] = []
		p = Pool(4)
		self.est = list(p.map(self.ret,[0,1,2,3]))
		self.est.sort(reverse=True)
		p.close()
		r = self.est[0][2]
		if self.est[0][1] == sorted(self.est, key = lambda x:x[1]):
			r = self.est[1][1]
		return(r)

	def ret(self,i):
		zero = self.zero()
		if self.re<=400:
			loop = 3
		elif 400<self.re<=600:
			loop = 4
		elif 925<self.re<=1000:
			loop = 4
		elif zero<=1:
			loop = 6
		elif 1<zero<=5:
			loop = 5
		else:
			loop = 4
		if self.est[i] != []:
			for j in range(0,loop):
				#loop回先読みする。先読みした項の数から考えていく
				self.est[i] = self.assem(self.est[i])
			if self.est[i] != []:
				for j in range(len(self.est[i])):
					self.est[i][j] = self.count(self.est[i][j])
				self.est[i] = [max(self.est[i]),len(self.est[i]),i]
				#最大値、いける数、方向
			else:
				self.est[i] = [0,0,i]
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
		gridt = copy.deepcopy(grid)
		#評価
		kazu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		#kazuは盤上の数字の個数
		if self.re <= 700:
			for i in range(0,len(grid)):
				kazu[0] = grid[i].count(0) + kazu[0]
				for j in range(1,len(kazu)):
					kazu[j] = grid[i].count(2**j) + kazu[j]
				#数を数えている。0は特例
			if self.re<=300:
				hyouka = kazu[0]*800
			else:
				hyouka = kazu[0]*1500
			#盤上を評価する。0が5点、それ以外は1.7*i点→素数にすると簡単に判別できるかも？
			for i in range(1,len(kazu)):
				if kazu[i] != 0:
					hyouka = int(kazu[i]*(1.7**(i*2))) + hyouka
			return hyouka
		else:
			gridt[0].append(grid[0][0])
			gridt[0].append(grid[0][0])
			gridt[0].append(grid[0][1])
			gridt[0].append(grid[0][3])
			gridt[0].append(grid[0][3])
			gridt[0].append(grid[0][2])
			gridt[1].append(grid[1][0])
			gridt[1].append(grid[1][3])
			gridt[2].append(grid[2][0])
			gridt[2].append(grid[2][3])
			gridt.append(grid[1])
			for j in range(1,len(kazu)):
				kazu[j] = gridt[0].count(2**j)*4 + kazu[j]
			for i in range(1,len(gridt)):
				for j in range(1,len(kazu)):
					kazu[j] = gridt[i].count(2**j) + kazu[j]
				#数を数えている。0は特例
			if self.re<=300:
				hyouka = kazu[0]*800
			elif 300<self.re<=1000:
				hyouka = kazu[0]*1500
			elif 1000<self.re<=1300:
				hyouka = kazu[0]*4000
			else:
				hyouka = kazu[0]*7000
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
			#0は非表示
			colordic = {0:'\033[30m\033[40m',2:'\033[1m',4:'\033[1m',8:'\033[1m\033[1;34m\033[47m',16:'\033[1m\033[32m\033[47m',32:'\033[1m\033[35m\033[47m',64:'\033[1m\033[31m\033[47m',
			128:'\033[1m\033[1;44m',256:'\033[1m\033[42m',512:'\033[1m\033[45m',1024:'\033[1m\033[41m',2048:'\033[1m\033[43m',4096:'\033[1m\033[41m'}
			print(self.est)
			print("count: " + str(self.re))
			direction = ["↑","→","↓","←"]
			print("direction: " + direction[r])
			grid = dic_jdata['grid']
			for i in range(0,len(grid[0])):
				for j in range(4):
					print (colordic[grid[i][j]] + "%4d"% grid[i][j] + "\033[0m" , end = " ")
				print("\n")
			print ("Score: " + str(dic_jdata['score']))
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
			gridtem[i] = grid
			gridtem[i][zero[i][0]][zero[i][1]] = 2
			return(gridtem[i])
		else:
			return(grid)

def yaruze(url):
	#動くところ	
	grid = Grid()
	grid.re = 1
	grid.grid = start(url)
	grid.est = ""
	while dic_jdata['over'] != True:
		if grid.re<90:
			#moveしてないからgrid.grid設定されてないなのです！
			grid.move(random.randint(0,2),url)
		else:
			grid.move(grid.nexs(),url)
		grid.re = grid.re + 1
	print("over!")
	#ファイルの書き出し。統計のためです
	file = open('shutm.txt', mode='a')
	if grid.re > 100:
		file.write('\n')
		file.write(str(dic_jdata['score']) +" " + str(grid.grid) + str(grid.re))
	else:
		file.write("," + str(dic_jdata['score']) + " " + str(grid.re))
	file.close()

def start(url):
	json_data = urllib.request.urlopen('http://' + url +'hi/start/size/4/tiles/2/victory/20/rand/2/json')
	str_jdata = json_data.read().decode('utf-8')
	global dic_jdata
	grid = [0,0,0,0]
	dic_jdata = json.loads(str_jdata)	
	grid = dic_jdata['grid']
	colordic = {0:'\033[30m\033[40m',2:'\033[1m',4:'\033[1m'}
	for i in range(0,len(grid[0])):
		for j in range(4):
			print (colordic[grid[i][j]] + "%4d"% grid[i][j] + "\033[0m" , end = " ")
		print("\n")
	#盤を表示する
	print ("score: " + str(dic_jdata['score']) + "\n")
	return(grid)


if __name__ == "__main__":
	#poolの関係上こっちに回数を組込する
	u = 0
	u = int(input("URL(1:outside, 2:ring): "))
	count = int(input("やりたい回数: "))
	if u == 1:
		url = "2048.semantics3.com/"
	elif u == 2:
		url = "ring:2048/"
	else:
		print("ha????????")
		sys.exit()
	for i in range(0,count):
		print (str(i+1) + "回目" + "\n")
		yaruze(url)