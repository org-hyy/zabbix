#!/usr/bin/python
#coding=utf-8
import commands
import json

if __name__ == "__main__":
	stat, proStr = commands.getstatusoutput("cat /proc/diskstats | egrep 'sd[a-z]\\b|xvd[a-z]\\b'|awk '{print $3}'")
	tmpList = proStr.split("\n")
	dnames = (i for i in tmpList)
	data = [{"#DNAME":dname} for dname in dnames]
	print (json.dumps({"data":data}))
