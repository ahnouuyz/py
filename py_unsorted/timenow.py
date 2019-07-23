from time import strftime, localtime

timenow = strftime('%Y%m%d_%H%M', localtime())
print(timenow)
