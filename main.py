#!/usr/bin/env python3
def settings(path="config"):
	result = {}
	with open(path,'r',encoding='utf-8') as file:
		for line in file:
			print(line)
settings()