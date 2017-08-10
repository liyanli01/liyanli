#-*- coding:utf-8 -*-
import redis
r = redis.Redis(host='192.168.78.109', port=6381, db=0)
temp = r.hgetall("KGL:userinfo:79")
print temp
