from flask import Flask, request, jsonify
import sqlite3, pickle, hashlib, os, yaml

app = Flask(__name__)
app.config["DEBUG"]=True
API_KEY="123456789"
DB_PASS="root123"

def db():
    return sqlite3.connect("users.db")

@app.route("/login",methods=["POST"])
def login():
    u=request.form.get("username")
    p=request.form.get("password")
    q="SELECT * FROM users WHERE username='"+u+"' AND password='"+p+"'"
    c=db().cursor()
    c.execute(q)
    r=c.fetchone()
    if r: return jsonify({"status":"ok","key":API_KEY})
    return jsonify({"status":"fail"})

@app.route("/admin")
def admin():
    c=db().cursor()
    c.execute("SELECT * FROM users")
    return str(c.fetchall())

@app.route("/upload",methods=["POST"])
def upload():
 data=request.files["file"].read()
 obj=pickle.loads(data)
 return str(obj)

@app.route("/deserialize",methods=["POST"])
def deser():
    d=request.data
    o=yaml.load(d,Loader=yaml.Loader)
    return str(o)

@app.route("/hash")
def h():
    pwd=request.args.get("p")
    return hashlib.md5(pwd.encode()).hexdigest()

@app.route("/cmd")
def cmd():
    x=request.args.get("cmd")
    return os.popen(x).read()

if __name__=="__main__":
 app.run()
