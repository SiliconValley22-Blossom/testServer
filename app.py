from flask import Flask

app = Flask(__name__)
from flask import request

@app.route('/api/login')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/photos', methods=['post'])
def postPhotos():
    file = request.files['file']
    print(file.filename)
    print(file.content_type)
    return 'ok'


@app.route('/api/photos/<int:photo_id>', methods=['get'])
def getPhotosById():
    result = {"photo": 'test/newFile.png'}
    return result


@app.route('/api/photos', methods=['get'])
def getPhotos():

    return """
    {
    "photo_list": [
        [
            "bdee9966-0bb5-4301-b893-908902af518e.jpeg",
            "f96cc436-be73-4816-835b-3e492cd5c69a.jpeg"
        ],
        [
            "eb213a07-5261-40b0-a41d-4deeb376ee08.jpeg",
            "de05c8f6-e4ea-4079-9307-e8e0c07c214a.jpeg"
        ],
        [
            "274ae8ea-335a-430b-8326-3c8e63a3cce0.jpeg",
            "8f9731fa-95a1-4e95-8ce5-c3ead6923c50.jpeg"
        ],
        [
            "e0664209-bd26-41a2-a0c1-083f00dc4f6b.jpeg",
            "1df01092-5b63-4c03-a973-100e367c36d3.jpeg"
        ]
    ]
}
    """



if __name__ == '__main__':
    app.run()
