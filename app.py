from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
import datetime
from flask_jwt_extended import set_access_cookies, set_refresh_cookies, create_access_token, create_refresh_token, JWTManager

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
    print(request.data)
    print(request.data['email'])
    print(request.data['password'])
    print(request.data['nickname'])
    return 'ok'


@app.route('/api/photos', methods=['post'])
def postPhotos():
    file = request.files['file']
    print(file.filename)
    print(file.content_type)
    return """
    {
    "black_photo_id":1,
    "color_photo_id":2  
}
    """
@app.route('/api/users', methods=['get'])
def getUser():

    return """
    {
         "user_id": 0,
          "email": "string",
          "nickname": "string",
          "created_at": "2022-07-31T09:17:18.078Z",
          "updated_at": "2022-07-31T09:17:18.078Z",
          "is_deleted": true
    }
    """

@app.route('/api/users', methods=['patch'])
def patchUser():
    print(request.data['password'])
    print(request.data['new_password'])
    return "ok"



@app.route('/api/photos/<int:photo_id>', methods=['get'])
def getPhotosById(photo_id):

    result = {"photo": 'test/newFile.png'}
    return result


@app.route('/api/photos', methods=['get'])
def posttPhotos():
    param = request.args.get('userId')
    if param is None:
        return """
{
    "photo_list": [
        [
            "black/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
            "color/74f90258-6e8c-4f0f-8e03-908f1c79787a.jpeg"
        ],
        [
            "black/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
            "color/74f90258-6e8c-4f0f-8e03-908f1c79787a.jpeg"
        ],
        [
            "black/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
            "color/74f90258-6e8c-4f0f-8e03-908f1c79787a.jpeg"
        ],
        [
            "black/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
            "color/74f90258-6e8c-4f0f-8e03-908f1c79787a.jpeg"
        ]
    ]
}
    """
    return """
{
    "photo_list": [
        [
            "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
            "black/74f90258-6e8c-4f0f-8e03-908f1c79787a.jpeg"
        ],
        [
            "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
            "black/74f90258-6e8c-4f0f-8e03-908f1c79787a.jpeg"
        ],
        [
            "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
            "black/74f90258-6e8c-4f0f-8e03-908f1c79787a.jpeg"
        ],
        [
            "color/1360f998-3ecd-431f-a0e1-ce607bf7d320.jpeg",
            "black/74f90258-6e8c-4f0f-8e03-908f1c79787a.jpeg"
        ]
    ]
}
    """

@app.route('/api/admin/users', methods=['get'])
def getAdmin():
    return """
    {
        {
            "created_at": "Thu, 21 Jul 2022 12:46:36 GMT",
            "email": "test@google.com",
            "is_deleted": false,
            "nickname": "TEST",
            "updated_at": "Thu, 21 Jul 2022 12:46:36 GMT",
            "user_id": 7
        },
        {
            "created_at": "Fri, 22 Jul 2022 06:44:45 GMT",
            "email": "aaa1",
            "is_deleted": false,
            "nickname": "test",
            "updated_at": "Fri, 22 Jul 2022 06:44:45 GMT",
            "user_id": 8
        },
        {
            "created_at": "Tue, 26 Jul 2022 06:04:05 GMT",
            "email": "asdf",
            "is_deleted": false,
            "nickname": "123",
            "updated_at": "Tue, 26 Jul 2022 06:04:05 GMT",
            "user_id": 9
        }
    ]
    """
@app.route('/api/users', methods=['delete'])
def deleteUser():
    return 204

@app.route('/api/login/check', methods=['get'])
def checkLogin():
    return jsonify({"is_login":True})

@app.route('/api/users/reset-pw', methods=['post'])
def resetPw():
    return 200

if __name__ == '__main__':
    app.run()
