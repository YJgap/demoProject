from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from flask.templating import render_template
from connect_database import MyData
from flask_cors import CORS
 
app = Flask(__name__) 

# router 오류를 해결하기 위해 선생님께 여쭤본 내용
# CORS(app, resources={r"*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}})
CORS(app)


@app.route('/read', methods=['GET'])
def read_data():
    data_list = MyData().get_database()
    return jsonify(data_list)
    # return render_template("app.html", data_list=data_list)




# @app.route('/update', methods=['POST'])
# def update_contact():
#     data_list = request.get_json()
#     MyData().update_database(
#         data_list['id'],
#         data_list['firstName'],
#         data_list['lastName'],
#         data_list['nickName'],
#         data_list['phone'],
#         data_list['memo']
#     )
#     return jsonify(sucesses=True)

@app.route('/update', methods=['POST'])
def update_contact():
    data_list = request.get_json()

    try:
        MyData().update_database(
            data_list['id'],
            data_list['firstName'],
            data_list['lastName'],
            data_list['nickName'],
            data_list['phone'],
            data_list['memo']
        )
        return jsonify(success=True)
    except Exception as e:
        print(f"Error updating contact: {e}")
        return jsonify(success=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5158)
