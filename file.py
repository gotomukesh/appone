fp = open("abcd.txt","w")
fp.write("write access mode")
fp.writelines("Welcome to file ")

lines = ["Pyhton","Python Library", "Data science"]
fp.writelines(lines)

fp.close()