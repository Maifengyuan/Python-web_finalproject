from pymysql import connect

conn = connect("localhost","root","@2916(Maify)","logmess")
cursor = conn.cursor()
sql = "select * from stuaccount"
read_row = cursor.execute(sql)

login_information = cursor.fetchall()

def panduan_login(name,password):
	for item in login_information:
		if  item[4] == name and item[5] == password:
			return "true"
			

if __name__ == '__main__':
	panduan_login()

# panduan_information = [
# 	{"zhanghao":"michael","mima":"09164235"},
# 	{"zhanghao":"张行宇","mima":"666666"},
# 	{"zhanghao":"打工人","mima":"am8"}
# ]

# def panduan(zhanghao,mima):
# 	for item in panduan_information:
# 		if item["zhanghao"] == zhanghao and item["mima"] == mima:
# 			return "true"