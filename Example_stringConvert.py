#
import json
x="(110,[8,9,11,12,13,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,36,38,59,62,93,99],[12.0,16.0,1.0,495.0,4.0,21.0,13.0,25.0,1.0,3225.0,14.0,6.0,119.0,14.0,3.0,20.0,3.0,3.0,3.0,3.0,3.0,1.0,1.0,1.0,1.0,1.0])"
y = x.replace("(","[").replace(")","]")

print(type(json.loads(y)))