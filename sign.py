counter = 3
password = "a123456"
while counter > 0 :
	pwd = input("input password:")
	if pwd == password:
		print("登入成功")
		break
	elif pwd != password and counter > 1 :
		print("密碼錯誤! 還有", counter - 1, "次機會")

	counter = counter - 1	

	