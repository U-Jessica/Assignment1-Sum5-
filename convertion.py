import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=int(jsonObj['a'])
    if a>=0 and a<2:
        response+="<b> The cat's age in cat's years is <b>"+str(a*11.5)+"</b><br>" 
    else:
        s=((a-2)*3.5)+(2*11.5)
        response+="<b> The cat's age in cat's years is <b>"+str(s)+"</b><br>"
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
