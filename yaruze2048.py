# -*- coding: utf-8 -*-

import json
import copy
import urllib.request
import random
import sys
import turn

class Grid:
	class turn(turn.Turn):
		pass
	def nexs(self,grid):
		global gridr
		grid_r = copy.deepcopy(grid)
		grid_r_r = copy.deepcopy(grid)
		gridr = copy.deepcopy(grid)
		hyolist = [[0,0,0,0]]*(len(grid)**4)
		grid = copy.deepcopy(nexg(grid,gridr))
		ikelist = [[0,0],[0,1],[0,2],[0,3]]
		#ここで一回目移動シミュレート終了してる
		for f in range(0,len(grid)):
			grid_r = copy.deepcopy(grid_r_r)
			#一回目にダブっていないか確かめる
			if grid[f] != grid_r:
				grid_r = copy.deepcopy(grid[f])
				gridr[f] = copy.deepcopy(grid[f])
				#二回目移動のシミュレート
				grid[f] = copy.deepcopy(nexg(grid[f],gridr[f]))
				#grid[f]にシミュ結果を入れてる
				for g in range(0,len(grid[f])):
					#二回目にダブってないか確かめる
					if grid[f][g] != grid_r:
						grid_r = copy.deepcopy(grid[f][g])
						gridr[f][g] = copy.deepcopy(grid[f][g])
						#三回目移動のシミュレート
						grid[f][g] = copy.deepcopy(nexg(grid[f][g],gridr[f][g]))
						for h in range (0,len(grid[f][g])):
							if grid[f][g][h] != grid_r: 
								hyolist[f*16 + g*4 + h] = [count(grid[f][g][h]),f,g,h]
								ikelist[f][0] = 1 + ikelist[f][0]
		hyolist.sort()
		hyolist.reverse()
		r = hyolist[0][1]
		return(r)

	def nexs1(self,grid):
		global gridr
		grid_r = copy.deepcopy(grid)
		grid_r_r = copy.deepcopy(grid)
		gridr = copy.deepcopy(grid)
		hyolist = [[0,0,0,0]]*(len(grid)**4)
		grid = copy.deepcopy(nexg(grid,gridr))
		ikelist = [[0,0],[0,1],[0,2],[0,3]]
		#ここで一回目移動シミュレート終了してる
		for f in range(0,len(grid)):
			grid_r = copy.deepcopy(grid_r_r)
			#一回目にダブっていないか確かめる
			if grid[f] != grid_r:
				grid_r = copy.deepcopy(grid[f])
				gridr[f] = copy.deepcopy(grid[f])
				#二回目移動のシミュレート
				grid[f] = copy.deepcopy(nexg(grid[f],gridr[f]))
				#grid[f]にシミュ結果を入れてる
				for g in range(0,len(grid[f])):
					#二回目にダブってないか確かめる
					if grid[f][g] != grid_r:
						grid_r = copy.deepcopy(grid[f][g])
						gridr[f][g] = copy.deepcopy(grid[f][g])
						#三回目移動のシミュレート
						grid[f][g] = copy.deepcopy(nexg(grid[f][g],gridr[f][g]))
						for h in range(0,len(grid[f][g])):
							if grid[f][g][h] != grid_r:
								ikelist[f][0] = 1 + ikelist[f][0]
								grid_r = copy.deepcopy(grid[f][g][h])
								gridr[f][g][h] = copy.deepcopy(grid[f][g][h])
								#四回目移動のシミュレート
								grid[f][g][h] = copy.deepcopy(nexg(grid[f][g][h],gridr[f][g][h]))
								for i in range (0,len(grid[f][g][h])):
									if grid[f][g][h][i] != grid_r: 
										hyolist[f*64 + g*16 + h*4 + i] = [count(grid[f][g][h][i]),f,g,h,i]
										
		hyolist.sort()
		hyolist.reverse()
		r = hyolist[0][1]
		return(r)

	def nexs2(self,grid):
		global gridr
		grid_r = copy.deepcopy(grid)
		grid_r_r = copy.deepcopy(grid)
		gridr = copy.deepcopy(grid)
		hyolist = [[0,0,0,0]]*(len(grid)**5)
		grid = copy.deepcopy(nexg(grid,gridr))
		ikelist = [[0,0],[0,1],[0,2],[0,3]]
		#ここで一回目移動シミュレート終了してる
		for f in range(0,len(grid)):
			grid_r = copy.deepcopy(grid_r_r)
			#一回目にダブっていないか確かめる
			if grid[f] != grid_r:
				grid_r = copy.deepcopy(grid[f])
				gridr[f] = copy.deepcopy(grid[f])
				#二回目移動のシミュレート
				grid[f] = copy.deepcopy(nexg(grid[f],gridr[f]))
				#grid[f]にシミュ結果を入れてる
				for g in range(0,len(grid[f])):
					#二回目にダブってないか確かめる
					if grid[f][g] != grid_r:
						grid_r = copy.deepcopy(grid[f][g])
						gridr[f][g] = copy.deepcopy(grid[f][g])
						#三回目移動のシミュレート
						grid[f][g] = copy.deepcopy(nexg(grid[f][g],gridr[f][g]))
						for h in range(0,len(grid[f][g])):
							if grid[f][g][h] != grid_r:
								ikelist[f][0] = 1 + ikelist[f][0]
								grid_r = copy.deepcopy(grid[f][g][h])
								gridr[f][g][h] = copy.deepcopy(grid[f][g][h])
								#四回目移動のシミュレート
								grid[f][g][h] = copy.deepcopy(nexg(grid[f][g][h],gridr[f][g][h]))
								for i in range(0,len(grid[f][g][h])):
									if grid[f][g][h][i] != grid_r:
										grid_r = copy.deepcopy(grid[f][g][h][i])
										gridr[f][g][h][i] = copy.deepcopy(grid[f][g][h][i])
										nexg(grid[f][g][h][i],gridr[f][g][h][i])
										#5回目移動のシミュレート
										grid[f][g][h][i] = copy.deepcopy(nexg(grid[f][g][h][i],gridr[f][g][h][i]))
										for j in range (0,len(grid[f][g][h][i])):
											if grid[f][g][h][i][j] != grid_r: 
												hyolist[f*256 + g*64 + h*16 + i+4 + j] = [count(grid[f][g][h][i][j]),f]
										
		hyolist.sort()
		hyolist.reverse()
		n = 0
		while ikelist[hyolist[n][1]][0] == 0:
			n = n + 1
			if n == len(hyolist)-3:
				break
		ikelist.sort()
		print(ikelist)
		while hyolist[n][1] == ikelist[0][1]:
			n = n + 1
			if n == len(hyolist)-2:
				break
		r = hyolist[n][1]
		return(r)

	def nexs3(self,grid):
		global gridr
		grid_r = copy.deepcopy(grid)
		grid_r_r = copy.deepcopy(grid)
		gridr = copy.deepcopy(grid)
		hyolist = [[0,0,0,0]]*(len(grid)**6)
		grid = copy.deepcopy(nexg(grid,gridr))
		ikelist = [[0,0],[0,1],[0,2],[0,3]]
		#ここで一回目移動シミュレート終了してる
		for f in range(0,len(grid)):
			grid_r = copy.deepcopy(grid_r_r)
			#一回目にダブっていないか確かめる
			if grid[f] != grid_r:
				grid_r = copy.deepcopy(grid[f])
				gridr[f] = copy.deepcopy(grid[f])
				#二回目移動のシミュレート
				grid[f] = copy.deepcopy(nexg(grid[f],gridr[f]))
				#grid[f]にシミュ結果を入れてる
				for g in range(0,len(grid[f])):
					#二回目にダブってないか確かめる
					if grid[f][g] != grid_r:
						grid_r = copy.deepcopy(grid[f][g])
						gridr[f][g] = copy.deepcopy(grid[f][g])
						#三回目移動のシミュレート
						grid[f][g] = copy.deepcopy(nexg(grid[f][g],gridr[f][g]))
						for h in range(0,len(grid[f][g])):
							if grid[f][g][h] != grid_r:
								ikelist[f][0] = 1 + ikelist[f][0]
								grid_r = copy.deepcopy(grid[f][g][h])
								gridr[f][g][h] = copy.deepcopy(grid[f][g][h])
								#四回目移動のシミュレート
								grid[f][g][h] = copy.deepcopy(nexg(grid[f][g][h],gridr[f][g][h]))
								for i in range(0,len(grid[f][g][h])):
									if grid[f][g][h][i] != grid_r:
										grid_r = copy.deepcopy(grid[f][g][h][i])
										gridr[f][g][h][i] = copy.deepcopy(grid[f][g][h][i])
										#5回目移動のシミュレート
										grid[f][g][h][i] = copy.deepcopy(nexg(grid[f][g][h][i],gridr[f][g][h][i]))
										for j in range(0,len(grid[f][g][h][i])):
											if grid[f][g][h][i][j] != grid_r:
												grid_r = copy.deepcopy(grid[f][g][h][i][j])
												gridr[f][g][h][i] = copy.deepcopy(grid[f][g][h][i][j])
												#5回目移動のシミュレート
												grid[f][g][h][i][j] = copy.deepcopy(nexg(grid[f][g][h][i][j],gridr[f][g][h][i][j]))
												for k in range (0,len(grid[f][g][h][i][j])):
													if grid[f][g][h][i][j][k] != grid_r: 
														hyolist[f*1024 + g*256 + h*64 + i+16 + j*4 + k] = [count(grid[f][g][h][i][j][k]),f]									
		hyolist.sort()
		hyolist.reverse()
		n = 0
		while ikelist[hyolist[n][1]][0] == 0:
			n = n + 1
			if n == len(hyolist)-3:
				break
		ikelist.sort()
		print(ikelist)
		while hyolist[n][1] == ikelist[0][1]:
			n = n + 1
			if n == len(hyolist)-2:
				break
		r = hyolist[n][1]
		return(r)

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
		if re<=500:
			hyouka = kazu[0]*800
		elif 500<re<=900:
			hyouka = kazu[0]*1500
		else:
			hyouka = kazu[0]*3000
		#盤上を評価する。0が5点、それ以外は1.7*i点→素数にすると簡単に判別できるかも？
		for i in range(1,len(kazu)):
			if kazu[i] != 0:
				hyouka = int(kazu[i]*(1.7**(i*2))) + hyouka
		return hyouka

	def nexg(self,grid,gridr):
		gridt = [0,0,0,0]
		gridt[1] = copy.deepcopy(hen(right(grid),gridr))
		gridt[3] = copy.deepcopy(hen(left(grid),gridr))
		gridt[0] = copy.deepcopy(hen(up(grid),gridr))
		gridt[2] = copy.deepcopy(hen(down(grid),gridr))
		return(gridt)

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
			cnt = grid.count(grid)
			print ("評価点: " + str(cnt) + "\n")
			if dic_jdata['over'] == True:
				print("over!")
				#ファイルの書き出し。統計のためです
				file = open('shutz.txt', mode='a')
				file.write(str(dic_jdata['score']) +" " + str(grid) + str(re))
				file.write('\n')
				file.close()
				sys.exit()
			else:
				return(grid)
		else:
			r = random.randint(0,3)
			self.move(r,url)

	def hen(self,grid,gridr):
		#ランダムに2を入れて返す関数
		global zero
		if len(zero) != 0 and grid != gridr:
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
	while 1:
		if re<70:
			grid.grid = grid.move(random.randint(0,2),url)
		elif 70<= re<500:
			grid.grid = grid.move(nexs(grid.grid),url)
		elif 500<= re <800:
			grid.grid = grid.move(nexs1(grid.grid),url)
		else:
			grid.grid = grid.move(nexs2(grid.grid),url)
		re = re + 1

def start(url):
	json_data = urllib.request.urlopen('http://' + url +'hi/start/json')
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
