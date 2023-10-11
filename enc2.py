

hexs="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
#bytes.hex(b"c") # 63
#bytes.fromhex("63") # c

"""
x = 0
myh=""
myhexs = []
for h in hexs:
    myh=myh + h
    x+=1
    if x==2:
        myhexs.append(myh)
        #print(myhexs)
        myh=""
        x=0
    #print(myh)
print("".join([bytes.fromhex(h).decode("utf-8") for h in myhexs]))
#decodes = [bytes.fromhex(h).decode("utf-8") for h in myhexs]
#print("".join(decodes))
"""

print("".join([bytes.fromhex(hexs).decode("utf-8")]))
