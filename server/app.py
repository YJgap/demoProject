from flask import Flask
from flask.templating import render_template
from connect_database import MyData
 
app = Flask(__name__) 
@app.route('/')
def test():
    data_list = MyData().get_database()
    return render_template("app.html", data_list=data_list)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5158)
