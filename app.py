from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
from flask_jwt_extended import set_access_cookies, set_refresh_cookies

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/api/login',  methods=['post'])
def hello_world():  # put application's code here
    resp = jsonify({'message': 'Login Successfully'})
    set_access_cookies(resp, "access")
    set_refresh_cookies(resp, "refresh")
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


@app.route('/api/photos/<int:photo_id>', methods=['get'])
def getPhotosById(photo_id):

    result = {"photo": 'test/newFile.png'}
    return result


@app.route('/api/photos', methods=['get'])
def posttPhotos():
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


if __name__ == '__main__':
    app.run()
