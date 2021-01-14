from flask import Flask,render_template,request,jsonify,escape
from panduan import panduan_login
from geo import weatherInfo,geocode
from pymysql import connect
import pandas as pd
Mai_key = "217fc9b3f26daa32adb8c391fe0a372f"

app = Flask(__name__)

def log_request(req:"flask_request",res:str):
	with open("view.log","a") as log:
		print(req.form,req.remote_addr,req.user_agent,res,file=log,sep="|")

# 查询方法
def look_over():
	con = connect(host="127.0.0.1",port=3306,user="root",password="@2916(Maify)",db="logmess")
	cursor1 = con.cursor()
	sql = "select * from stuaccount"
	cursor1.execute(sql)
	res = cursor1.fetchall()
	print(res)
	return res

@app.route("/test",methods = ["POST"])
def hello_test_01():
	phrase = request.form["phrase"]
	letters = request.form["letters"]
	a = panduan_login(phrase,letters)
	# zhanghao = request.form["zhanghao"]
	# mima = request.form["mima"]
	# a = panduan(zhanghao,mima)
	if a == "true":
		return render_template('test.html')
	else:
		return "登入失败"

@app.route("/")
def hello() -> str:
	return "hello world"

@app.route("/welcome")
def wel_first() -> 'html':
	return render_template('wel_web.html')

@app.route("/entry")
def entry_page() -> 'html':
	return render_template('entry.html',the_title ="高德API+web_flask项目实践")

@app.route('/add_stu')
def addstudent_page():
	return render_template("addpage.html", the_title = "请添加你的信息以完成注册")

@app.route('/add_info',methods = ['POST'])
def addstudent():
	student_id = request.form["student_id"]
	student_name = request.form["student_name"]
	student_gender = request.form["student_gender"]
	student_class = request.form["student_class"]
	student_account = request.form["account_number"]
	student_password = request.form["user_password"]
	con = connect(host="127.0.0.1",port=3306,user="root",password="@2916(Maify)",db="logmess")
	cursor2 = con.cursor()
	sql = "insert into stuaccount set stu_numb='%s',stu_name='%s',stu_gen='%s',stu_class='%s',stu_acc='%s',stu_key='%s'"%(student_id,student_name,student_gender,student_class,student_account,student_password)
	cursor2.execute(sql)
	con.commit()
	return render_template("entry.html")

# @app.route('/add_enterinfo',methods = ['POST'])
# def add_enter():
# 	student_ID = request.form["account_ID"]
# 	student_account = request.form["account_number"]
# 	student_password = request.form["user_password"]
# 	con = connect(host="127.0.0.1",port=3306,user="root",password="@2916(Maify)",db="userbd")
# 	cursor3 = con.cursor()
# 	sql = "insert into useradmin set id='%s',username='%s',password='%s'"%(student_ID,student_account,student_password)
# 	cursor3.execute(sql)
# 	con.commit()
# 	return render_template("entry.html")

@app.route("/search",methods = ['POST'])
def search() -> 'html':
	# zhanghao = request.form.get("zhanghao")
	# mima = request.form.get("mima")
	# a = panduan(zhanghao,mima)
	user_input = request.form['City']
	geoone = weatherInfo(Mai_key,user_input)
	province1 = geoone["lives"][0]['province']
	city1 = geoone["lives"][0]['city']
	adcode1 = geoone["lives"][0]['adcode']
	weather1 = geoone["lives"][0]['weather']
	temperature1 = geoone["lives"][0]['temperature']
	winddirection1 = geoone["lives"][0]['winddirection']
	windpower1 = geoone["lives"][0]['windpower']
	humidity1 = geoone["lives"][0]['humidity']
	reporttime1 = geoone["lives"][0]['reporttime']
	result1 = str(province1)+str(city1)+str(adcode1)+str(weather1)+str(temperature1)+str(windpower1)+str(humidity1)+str(reporttime1)
	log_request(request,result1)
	return render_template('results.html',
		the_title = "查询成功，显示结果",
		the_geocode = geoone,
		province = province1,
		city = city1,
		adcode = adcode1,
		weather = weather1,
		temperature = temperature1,
		winddirection = winddirection1,
		windpower = windpower1,
		humidity = humidity1,
		reporttime = reporttime1
		)
	# if a =="true":
		# province1 = geoone["lives"][0]['province']
		# city1 = geoone["lives"][0]['city']
		# adcode1 = geoone["lives"][0]['adcode']
		# weather1 = geoone["lives"][0]['weather']
		# temperature1 = geoone["lives"][0]['temperature']
		# winddirection1 = geoone["lives"][0]['winddirection']
		# windpower1 = geoone["lives"][0]['windpower']
		# humidity1 = geoone["lives"][0]['humidity']
		# reporttime1 = geoone["lives"][0]['reporttime']
		# result1 = str(province1)+str(city1)+str(adcode1)+str(weather1)+str(temperature1)+str(windpower1)+str(humidity1)+str(reporttime1)
		# log_request(request,result1)
		# return render_template('results.html',
		# 	the_title = "登入成功，欢迎进入主页",
		# 	the_geocode = geoone,
		# 	province = province1,
		# 	city = city1,
		# 	adcode = adcode1,
		# 	weather = weather1,
		# 	temperature = temperature1,
		# 	winddirection = winddirection1,
		# 	windpower = windpower1,
		# 	humidity = humidity1,
		# 	reporttime = reporttime1
		# 	)
	# else:
	# 	return "账号或密码错误，登入查询失败"


@app.route("/results",methods =["GET"])
def results_page() -> "html":
	return render_template('results.html',the_title ="welcome to searchletters on the web")

@app.route("/viewlog")
def hello_viewlog():
	with open("view.log","r") as log:
		contents = []
		for item in log:
			contents.append([])
			for i in item.split("|"):
				contents[-1].append(escape(i))
	# return str(contents)
		
	log_title = ["Form data","Remote_addr","User_agent","results"]
	return render_template("view.html",title1 = "查看日志",the_data = contents,the_log_title = log_title)

@app.route("/geocode_01")
def hello_geocode():
	return render_template("res_geocode.html",title = "Welcome to experience 高德-API")

@app.route("/geocode_query_res",methods = ["POST"])
def answer_geocode_query_res() -> 'html':
	user_input_geocode = request.form['key_geocode']
	con_input_geocode = request.form['add_geocode']
	geotwo = geocode(user_input_geocode,con_input_geocode)
	country2 = geotwo["geocodes"][0]['country']
	province2 = geotwo["geocodes"][0]['province']
	city2 = geotwo["geocodes"][0]['city']
	district2 = geotwo["geocodes"][0]['district']
	adcode2 = geotwo["geocodes"][0]['adcode']
	location2 = geotwo["geocodes"][0]['location']
	return render_template("geocode_result.html",
		the_title = "查询成功，显示结果",
		country = country2,
		province = province2,
		city = city2,
		district = district2,
		adcode = adcode2,
		location = location2
		)


if __name__ =='__main__':
	app.run(debug = True)