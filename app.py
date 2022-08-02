from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
import datetime
from flask_jwt_extended import set_access_cookies, set_refresh_cookies, create_access_token, create_refresh_token, JWTManager
from werkzeug.exceptions import Unauthorized

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "qwer"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] =datetime.timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=14)

jwt = JWTManager(app)

CORS(app, supports_credentials=True)

@app.route('/api/login',  methods=['post'])
def hello_world():  # put application's code here
    resp = jsonify({'message': 'Login Successfully'})
    
    set_access_cookies(resp,create_access_token(identity="access"))
    set_refresh_cookies(resp,create_refresh_token(identity="refresh"))
    return resp

@app.route('/api/logout',  methods=['post'])
def logout():  # put application's code here
    return "ok"

@app.route('/api/users', methods=['post'])
def jkl():
    print(request)
    print(request.get_json())
    print(request.get_json()['email'])
    print(request.get_json()['password'])
    print(request.get_json()['nickname'])
    return 'ok'


@app.route('/api/photos', methods=['post'])
def postPhotos():
    file = request.files['file']
    print(file.filename)
    print(file.content_type)
    return jsonify({
        "black_photo_id":1,
        "color_photo_id":2  
    })

@app.route('/api/users', methods=['get'])
def getUser():

    return jsonify({
         "user_id": 0,
          "email": "string",
          "nickname": "string",
          "created_at": "2022-07-31T09:17:18.078Z",
          "updated_at": "2022-07-31T09:17:18.078Z",
          "is_deleted": True
    })


@app.route('/api/users', methods=['patch'])
def patchUser():

    print(request.get_json()['password'])
    print(request.get_json()['new_password'])
    return "200"



@app.route('/api/photos/<int:photo_id>', methods=['get'])
def getPhotosById(photo_id):

    result = {"photo": 'test/newFile.png'}
    return result


@app.route('/api/photos', methods=['get'])
def posttPhotos():
    param = request.args.get('userId')
    if param is None:
        return jsonify({
            "photo_list": [
            [
                "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                "color/e34ebf55-2b07-4911-b341-ae6de27fcaca.jpeg"
            ],
            [
                "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                "color/fd0dc262-9fa4-4b00-8ed5-0b91bc0194d8.jpeg"
            ],
            [
                "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                "color/e34ebf55-2b07-4911-b341-ae6de27fcaca.jpeg"
            ],
                [
                    "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                    "color/fd0dc262-9fa4-4b00-8ed5-0b91bc0194d8.jpeg"
                ],
                [
                    "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                    "color/e34ebf55-2b07-4911-b341-ae6de27fcaca.jpeg"
                ],
                [
                    "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                    "color/fd0dc262-9fa4-4b00-8ed5-0b91bc0194d8.jpeg"
                ]
            ]
        })

    return jsonify({
        "photo_list": [
            [
                "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                "color/e34ebf55-2b07-4911-b341-ae6de27fcaca.jpeg"
            ],
            [
                "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                "color/fd0dc262-9fa4-4b00-8ed5-0b91bc0194d8.jpeg"
            ],
            [
                "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                "color/e34ebf55-2b07-4911-b341-ae6de27fcaca.jpeg"
            ],
            [
                "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                "color/fd0dc262-9fa4-4b00-8ed5-0b91bc0194d8.jpeg"
            ],
            [
                "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                "color/e34ebf55-2b07-4911-b341-ae6de27fcaca.jpeg"
            ],
                [
                    "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
                    "color/fd0dc262-9fa4-4b00-8ed5-0b91bc0194d8.jpeg"
                ]
        ]
    })


@app.route('/api/admin/users', methods=['get'])
def getAdmin():
    return jsonify(
    [
        {
            "created_at": "Thu, 21 Jul 2022 12:46:36 GMT",
            "email": "test@google.com",
            "is_deleted": False,
            "nickname": "TEST",
            "updated_at": "Thu, 21 Jul 2022 12:46:36 GMT",
            "user_id": 7
        },
        {
            "created_at": "Fri, 22 Jul 2022 06:44:45 GMT",
            "email": "aaa1",
            "is_deleted": False,
            "nickname": "test",
            "updated_at": "Fri, 22 Jul 2022 06:44:45 GMT",
            "user_id": 8
        },
        {
            "created_at": "Tue, 26 Jul 2022 06:04:05 GMT",
            "email": "asdf",
            "is_deleted": False,
            "nickname": "123",
            "updated_at": "Tue, 26 Jul 2022 06:04:05 GMT",
            "user_id": 9
        }
    ]
    )

@app.route('/api/admin/users', methods=['delete'])
def deleteUser():
    id=request.get_json()["id_list"]
    print(id)
    return "204"

@app.route('/api/login/check', methods=['get'])
def checkLogin():
    return jsonify({"is_login":False})

@app.route('/api/users/reset-password', methods=['post'])
def resetPw():
    # 이메일 틀리면 401
    return "200"

@app.route('/api/refresh', methods=['get'])
def refreshToken():
    return "200"

@app.route('/api/error')
def produce401Error():
    raise Unauthorized(description="401 error")


if __name__ == '__main__':
    app.run()
