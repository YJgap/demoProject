from flask import Flask, jsonify
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='P@ssw0rd',
                     db='Anycall',
                     charset='utf8')

app = Flask(__name__)
@app.route('/test')
def test():
    sql = "SELECT * FROM yjgap;"
    data = cursor.execute(sql)
    return jsonify(data)

@app.route("/test", methods=["POST"])
def test():
    sql = "SELECT * FROM yjgap;"
    name = name
    phone = phone

    return jsonify({
        "name": name,
        "phone": phone,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    cursor = db.cursor()
    
db.close()