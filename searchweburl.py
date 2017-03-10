#! -*- coding:utf-8 -*-

'''
根据网站URL，寻找该URL所在的网站物理路径。
'''

__author__="nMask"
__Blog__="http://thief.one"
__Date__="20170310"

import urlparse
import os
import argparse
import time

x=0

def search(paths,file_name,tag,lists):
	'''
	递归函数：查找指定名称的文件夹的路径
	'''
	if os.path.isdir(paths):  #如果是目录
		if file_name==tag:    #如果目录名称为tag
			lists.append(paths) #将该路径添加到列表中
		else:                 #如果目录名称不为tag
			try:
				files_list=os.listdir(paths)  #列出目录中所有的文件
				for file_name in files_list:
					path_new=os.path.join(paths,file_name)  #构造文件路径
					search(path_new,file_name,tag,lists)    #递归
			except: #遇到特殊目录名时会报错
				pass

	elif os.path.isfile(paths): #如果是文件
		pass

	return lists

def run(test,t,x,lists):
	'''
	递归函数，根据传递的参数个数(目录层次个数)，执行search函数相应的次数。
	x的作用，是获取path_list不同的元素，用来判断不同层次的目录名称
	'''
	try:
		for i in search(test,t,tag=path_list[x],lists=[]): #得到一个列表，对列表进行循环，进入下一层目录
			if i.endswith(ends):  #如果路径最后几位的字符串等于目录最后一个参数
				print "[Info]Find one paths [%s]" % i
				lists.append(i)
			run(i,"",x+1,lists) #进入下一层目录，因此目录名称的判断tag也要改变。
	except:
		'''
		此处报错是由path_list[x]引起，因为x已经超出范围，用来结束此递归函数。
		'''
		pass

	return lists


def get_parameter(url):
	'''
	分析url，构造目录参数，返回一个参数列表。
	http://www.xxx.com/a/b/c?d=1
	["a","b"]表示有2层目录，第一层为a，第二层为b
	'''
	path=urlparse.urlparse(url).path
	path_list=path.split("/")[1:-1]
	return path_list

def print_information():
	print ""
	print "*********************************"
	print "*-------------------------------*"
	print "*-----Blog:http://thief.one-----*"
	print "*-------------------------------*"
	print "*--------Author:By nMask--------*"
	print "*-------------------------------*"
	print "*--------Date:2017.03.10--------*"
	print "*-------------------------------*"
	print "*********************************"
	print ""



usages='\n[*]python seachweburl.py -p "./" -u "http://www.xxx.com/a/b/c/d?e=1"'
parser=argparse.ArgumentParser(usage=usages)
parser.add_argument("-p","--path",help="File path to be detected")
parser.add_argument("-u","--url",help="URL to be detected")
args=parser.parse_args()
path=args.path
url=args.url

if path==None or url==None:
	parser.print_help()  ##设置帮助信息
else:
	print_information()
	path_list=get_parameter(url)
	ends=path_list[::-1][0] #获取目录结构的最后一个目录名称
	t1=time.time()
	lists=run(path,"",x,lists=[])
	t2=time.time()
	print ""
	print "[Result]A total of %s pahts Found" % str(len(lists))
	print "[Result]Spend time %ss" % str(t2-t1) 
