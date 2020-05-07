counter = 3
password = "a123456"
while counter > 0 :
	counter = counter - 1
	pwd = input("input password:")
	if pwd == password:
		print("登入成功")
		break
	else :
		print("密碼錯誤!")
		if counter > 0:
			print("還有", counter, "次機會")
		

	