# -*- coding: utf-8 -*-

import json
import copy
import urllib.request
import random
#from mawasuze2048 import right,left,up,down


def start():
	#一回目はURLとか違ったりAI組まなかったりするから別にする
	json_data = urllib.request.urlopen('http://ring:2048/hi/start/json')
	str_jdata = json_data.read().decode('utf-8')
	global dic_jdata
	global grid
	global x
	x = 0
	grid = [0,0,0,0]
	dic_jdata = json.loads(str_jdata)	
	grid = dic_jdata['grid']
	for i in range(0,len(grid)):
		print(grid[i])
	#盤を表示する
	print ("score: " + str(dic_jdata['score']) + "\n")
	nexs()

def nexs():
	global grid
	global r
	global x
	global gridr
	grid_r = copy.deepcopy(grid)
	grid_r_r = copy.deepcopy(grid)
	gridr = copy.deepcopy(grid)
	hyolist = [[0,0,0,0]]*(len(grid)**4)
	nexg(grid,gridr)
	grid = copy.deepcopy(gridt)
	ikelist = [[0,0],[0,1],[0,2],[0,3]]
	#ここで一回目移動シミュレート終了してる
	for f in range(0,len(grid)):
		grid_r = copy.deepcopy(grid_r_r)
		#一回目にダブっていないか確かめる
		if grid[f] != grid_r:
			grid_r = copy.deepcopy(grid[f])
			gridr[f] = copy.deepcopy(grid[f])
			nexg(grid[f],gridr[f])
			#二回目移動のシミュレート,gridtに4とおり入ってる
			grid[f] = copy.deepcopy(gridt)
			#grid[f]にシミュ結果を入れてる
			for g in range(0,len(grid[f])):
				#二回目にダブってないか確かめる
				if grid[f][g] != grid_r:
					grid_r = copy.deepcopy(grid[f][g])
					gridr[f][g] = copy.deepcopy(grid[f][g])
					nexg(grid[f][g],gridr[f][g])
					#三回目移動のシミュレート,gridtに4通り入ってる
					grid[f][g] = copy.deepcopy(gridt)
					for h in range (0,len(grid[f][g])):
						if grid[f][g][h] != grid_r: 
							count(grid[f][g][h])
							hyolist[f*16 + g*4 + h] = [hyouka,f,g,h]
							ikelist[f][0] = 1 + ikelist[f][0]
	hyolist.sort()
	hyolist.reverse()
	r = hyolist[0][1]

def nexs1():
	global grid
	global r
	global x
	global gridr
	grid_r = copy.deepcopy(grid)
	grid_r_r = copy.deepcopy(grid)
	gridr = copy.deepcopy(grid)
	hyolist = [[0,0,0,0]]*(len(grid)**4)
	nexg(grid,gridr)
	grid = copy.deepcopy(gridt)
	ikelist = [[0,0],[0,1],[0,2],[0,3]]
	#ここで一回目移動シミュレート終了してる
	for f in range(0,len(grid)):
		grid_r = copy.deepcopy(grid_r_r)
		#一回目にダブっていないか確かめる
		if grid[f] != grid_r:
			grid_r = copy.deepcopy(grid[f])
			gridr[f] = copy.deepcopy(grid[f])
			nexg(grid[f],gridr[f])
			#二回目移動のシミュレート,gridtに4とおり入ってる
			grid[f] = copy.deepcopy(gridt)
			#grid[f]にシミュ結果を入れてる
			for g in range(0,len(grid[f])):
				#二回目にダブってないか確かめる
				if grid[f][g] != grid_r:
					grid_r = copy.deepcopy(grid[f][g])
					gridr[f][g] = copy.deepcopy(grid[f][g])
					nexg(grid[f][g],gridr[f][g])
					#三回目移動のシミュレート,gridtに4通り入ってる
					grid[f][g] = copy.deepcopy(gridt)
					for h in range(0,len(grid[f][g])):
						if grid[f][g][h] != grid_r:
							ikelist[f][0] = 1 + ikelist[f][0]
							grid_r = copy.deepcopy(grid[f][g][h])
							gridr[f][g][h] = copy.deepcopy(grid[f][g][h])
							nexg(grid[f][g][h],gridr[f][g][h])
							#四回目移動のシミュレート
							grid[f][g][h] = copy.deepcopy(gridt)
							for i in range (0,len(grid[f][g][h])):
								if grid[f][g][h][i] != grid_r: 
									count(grid[f][g][h][i])
									hyolist[f*64 + g*16 + h*4 + i] = [hyouka,f,g,h,i]
									
	hyolist.sort()
	hyolist.reverse()
	r = hyolist[0][1]

def nexs2():
	global grid
	global r
	global x
	global gridr
	grid_r = copy.deepcopy(grid)
	grid_r_r = copy.deepcopy(grid)
	gridr = copy.deepcopy(grid)
	hyolist = [[0,0,0,0]]*(len(grid)**5)
	nexg(grid,gridr)
	grid = copy.deepcopy(gridt)
	ikelist = [[0,0],[0,1],[0,2],[0,3]]
	#ここで一回目移動シミュレート終了してる
	for f in range(0,len(grid)):
		grid_r = copy.deepcopy(grid_r_r)
		#一回目にダブっていないか確かめる
		if grid[f] != grid_r:
			grid_r = copy.deepcopy(grid[f])
			gridr[f] = copy.deepcopy(grid[f])
			nexg(grid[f],gridr[f])
			#二回目移動のシミュレート,gridtに4とおり入ってる
			grid[f] = copy.deepcopy(gridt)
			#grid[f]にシミュ結果を入れてる
			for g in range(0,len(grid[f])):
				#二回目にダブってないか確かめる
				if grid[f][g] != grid_r:
					grid_r = copy.deepcopy(grid[f][g])
					gridr[f][g] = copy.deepcopy(grid[f][g])
					nexg(grid[f][g],gridr[f][g])
					#三回目移動のシミュレート,gridtに4通り入ってる
					grid[f][g] = copy.deepcopy(gridt)
					for h in range(0,len(grid[f][g])):
						if grid[f][g][h] != grid_r:
							ikelist[f][0] = 1 + ikelist[f][0]
							grid_r = copy.deepcopy(grid[f][g][h])
							gridr[f][g][h] = copy.deepcopy(grid[f][g][h])
							nexg(grid[f][g][h],gridr[f][g][h])
							#四回目移動のシミュレート
							grid[f][g][h] = copy.deepcopy(gridt)
							for i in range(0,len(grid[f][g][h])):
								if grid[f][g][h][i] != grid_r:
									grid_r = copy.deepcopy(grid[f][g][h][i])
									gridr[f][g][h][i] = copy.deepcopy(grid[f][g][h][i])
									nexg(grid[f][g][h][i],gridr[f][g][h][i])
									#5回目移動のシミュレート
									grid[f][g][h][i] = copy.deepcopy(gridt)
									for j in range (0,len(grid[f][g][h][i])):
										if grid[f][g][h][i][j] != grid_r: 
											count(grid[f][g][h][i][j])
											hyolist[f*256 + g*64 + h*16 + i+4 + j] = [hyouka,f]
									
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

def count(grid):
	#評価
	kazu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#kazuは盤上の数字の個数
	global hyouka
	global re
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


def right(grid):
	#右は1です
	global gridt
	global zero
	global gridr
	zero = []
	gridt[1] = copy.deepcopy(grid)
	for i in range(0,len(gridt[1])):
		zeroc = 0
		while 0 in gridt[1][i]:
			gridt[1][i].remove(0)
		if len(gridt[1][i]) != 0:
			for j in range(0,len(gridt[1][i])-1):
				if gridt[1][i][len(gridt[1][i])-j-1] == gridt[1][i][len(gridt[1][i])-j-2] :
					gridt[1][i][len(gridt[1][i])-j-2] = gridt[1][i][len(gridt[1][i])-j-1] * 2
					gridt[1][i].pop(len(gridt[1][i])-j-1)
					#ここで2048用の独自の処理を加える。2240や2244の時の対策。
					if len(gridt[1][i]) - j > 2 and gridt[1][i][0] == gridt[1][i][1]:
						gridt[1][i][0] = gridt[1][i][1]*2
						gridt[1][i].pop(1)
						break
					else:
						break
		while len(gridt[1][i]) != 4:
			gridt[1][i].insert(0, 0)
			zero.append([i,zeroc])
			zeroc = zeroc + 1

def left(grid):
	#左は3です
	global gridt
	global zero
	zero = []
	gridt[3] = copy.deepcopy(grid)
	for i in range(0,len(gridt[3])):
		zeroc = 0
		while 0 in gridt[3][i]:
			gridt[3][i].remove(0)
		if len(gridt[3][i]) != 0:
			for j in range(0,len(gridt[3][i])-1):
				if gridt[3][i][j] == gridt[3][i][j+1] :
					gridt[3][i][j] = gridt[3][i][j] * 2
					gridt[3][i].pop(j+1) 
					if len(gridt[3][i])-j > 2 and gridt[3][i][j+1] == gridt[3][i][j+2]:
						gridt[3][i][j+1] = gridt[3][i][j+2]*2
						gridt[3][i].pop(j+2)
						break
					else:
						break
		while len(gridt[3][i]) != 4:
			gridt[3][i].append(0)
			zero.append([i,3-zeroc])
			zeroc = zeroc + 1

def up(grid):
	#上は0です
	global gridt
	global zero
	zero = []
	#gridtのtはtemporaryのtだよっ！一回左右に変換してからやり直す
	gridtt = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	gridt[0] = copy.deepcopy(grid)
	for i in range(0,len(gridt[0])):
		for j in range(0,len(gridt[0][i])):
			gridtt[i][j] = gridt[0][j][i]
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
	for i in range(0,len(gridt[0])):
		for j in range(0,len(gridt[0])):
			gridt[0][i][j] = gridtt[j][i]
	for i in range(0,len(zero)):
		zero[i].reverse()

def down(grid):
	#下は2です
	#gridtのtはtemporaryのtだよっ！一回左右に変換してからやり直す
	global gridt
	global zero
	zero = []
	gridtt = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	gridt[2] = copy.deepcopy(grid)
	for i in range(0,len(gridt[2])):
		for j in range(0,len(gridt[2][i])):
			gridtt[i][j] = gridt[2][j][i]
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
	for i in range(0,len(gridt[2])):
		for j in range(0,len(gridt[2])):
			gridt[2][i][j] = gridtt[j][i]
	for i in range(0,len(zero)):
		zero[i].reverse()

def nexg(grid,gridr):
	global gridt
	global gridk
	global zero
	gridt = [0,0,0,0]
	right(grid)
	hen(gridt[1],gridr)
	gridt[1] = copy.deepcopy(gridk)
	left(grid)
	hen(gridt[3],gridr)
	gridt[3] = copy.deepcopy(gridk)
	up(grid)
	hen(gridt[0],gridr)
	gridt[0] = copy.deepcopy(gridk)
	down(grid)
	hen(gridt[2],gridr)
	gridt[2] = copy.deepcopy(gridk)

def yaruze():
	#動くところ
	global grid
	global hyouka
	global r
	global x
	global dic_jdata
	global kazu
	global zero
	global re
	re = 0
	start()
	while 1:
		print(str(re) + "回目の移動")
		json_data = urllib.request.urlopen('http://ring:2048/hi/state/' + dic_jdata['session_id'] + '/move/' + str(r) +'/json')
		str_jdata = json_data.read().decode('utf-8')
		dic_jdata = json.loads(str_jdata)
		print("direction: " + str(r))
		grid = dic_jdata['grid']
		count(grid)
		for i in range(0,len(grid[0])):
			print (grid[i])
		print ("score: " + str(dic_jdata['score']))
		if dic_jdata['over'] == True:
			print("over!")
			#ファイルの書き出し。統計のためです
			file = open('shuty.txt', mode='a')
			file.write(str(dic_jdata['score']) +" " + str(grid) + str(re))
			file.write('\n')
			file.close()
			break
		else:
			if hyouka == x:
				ｒ = random.randint(0,3)
				print("ohoh")
			else:
				x = hyouka
				re = re + 1
				print ("評価点: " + str(x) + "\n")
				if re<70:
					r = random.randint(0,2)
				elif 70<= re<500:
					nexs()
				elif 500<= re <800:
					nexs1()
				else:
					nexs2()

def hen(grid,gridr):
	global zero
	global hyouka
	global gridk
	if len(zero) != 0 and grid != gridr:
		gridtem =[0]*len(zero)
		i  = random.randint(0,len(zero)-1)
		gridtem[i] = copy.deepcopy(grid)
		gridtem[i][zero[i][0]][zero[i][1]] = 2
		gridk = copy.deepcopy(gridtem[i])
	else:
		gridk = copy.deepcopy(grid)



if __name__ == "__main__":
    yaruze()









