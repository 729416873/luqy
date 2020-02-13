# -*- coding: utf-8 -*-
import json

a1 = {"result":0,"data":{"order":0,"cart":0},"msg":"\u6210\u529f"}
print(type(a1))
a = '{"result":0,"data":{"order":0,"cart":0},"msg":"\u6210\u529f"}'
print(type(a))
b = json.dumps(a)
c = json.loads(a)
d = json.dumps(c,ensure_ascii=False)
print(b,type(b))
print(c,type(c))
print(d,type(d))