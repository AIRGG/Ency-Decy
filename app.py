from gevent import monkey
monkey.patch_all()
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, jsonify
from gevent.pywsgi import WSGIServer
import os
from cryptnya import EncyDecy

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/encrypt")
def encryptText():
	return render_template("encrypt.html")

@app.route("/decrypt")
def decryptText():
	return render_template("decrypt.html")

@app.route("/apiencydecy", methods=["POST", "GET"])
def apinya():
	if request.method == "GET":
		return "UPSS"
	apa = request.form["apa"]
	if request.method == "POST":
		if apa == "ency":
			pw = request.form["password"]
			msg = request.form["message"]
			tojsn = request.form["tojson"]
			ency = EncyDecy(pw).ency(msg).decode("UTF-8")
			if tojsn == "1":
				return {
					"chipertext":ency,
					"password":pw
				}
			return render_template("hasil.html", pw=pw, hasil=ency, apa=apa)

		if apa == "decy":
			pw = request.form["password"]
			msg = request.form["message"]
			tojsn = request.form["tojson"]
			decy = EncyDecy(pw).decy(msg)
			if(not decy):
				if tojsn == "1":
					return {
						"error":"Invalid Password!!!",
						"chipertext":msg,
						"password":pw
					}
				return "PASSWORDMU SALAH COKK <a href='/decrypt'>Back</a>"
			else:
				if tojsn == "1":
					return {
						"chipertext":msg,
						"password":pw,
						"msg":decy.decode("UTF-8")
					}
				return render_template("hasil.html", chiper=msg, pw=pw, hasil=decy.decode("UTF-8"), apa=apa)

	return "UPSS"

if __name__ == "__main__":
	# http_server = WSGIServer(('0.0.0.0', 3001), app)
	# http_server.serve_forever()
	# app.run()
	app.run(port=8082, debug=True, host="localhost")
