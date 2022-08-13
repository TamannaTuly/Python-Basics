msg='welcome to Python 101: Strings'
print(msg+" "+msg)
print(msg*2)
print(msg,msg)
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title()) # coverts each word's first character in upper case

msg2='welcome to it\'s Python 101: Strings'
print(msg2+" "+msg2)
print(msg2*2)
print(msg2,msg2)
print(msg2)
print(msg2.upper())
print(msg2.lower())
print(msg2.capitalize())
print(msg2.title()) # coverts each word's first character in upper case

msgc='welcome to Python 101: Strings'
print(msgc)
print(len(msgc))
print(msgc.count('o'))


####################################slicing

msgN = "welcome to python"
print(msgN)
print(msgN[3])
print(msgN[-1])
print(msgN[1:4])
print(msgN[:7])