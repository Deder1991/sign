counter = 3

while counter > 0 :
	password = input("input password:")
	if password == "a123456":
		print("登入成功")
		break
	elif password != "a123456" and counter > 1 :
		print("密碼錯誤! 還有", counter - 1, "次機會")
		
	counter = counter - 1	

	