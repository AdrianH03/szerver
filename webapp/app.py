from flask import Flask
import os.path

app = Flask(__name__)
path = "/app/szam.txt"

@app.route("/")
def hello_world():
    check = os.path.isfile(path)
    f = None
    if not check:
        f = open(path,"w")
        f.write("0")
        f.close()
    f = open(path,"r")
    szoveg = f.readline()
    f.close()
    x = int(szoveg)
    x += 1
    f = open(path,"w")
    f.write(str(x))
    f.close()
    szoveg = "A weboldalt " + str(x) + " alkalommal nyitották meg."
    return szoveg
@app.route("/reset")
def reset():
    f = open(path, "w")
    f.write("0")
    f.close()
    return "<p>A számlálót alaphelyzetbe állítottam</p>"