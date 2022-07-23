# 초기 설정
```angular2html
pip install -r requirements.txt
```

# 실행 방법
```angular2html
flask run
```

### 포트 지정 후 실행 방법
```angular2html
flask run --port 1234
```
# API

### POST /api/login
##### body
```
{
    "email":"asdf",
    "password":"asdf"
}
```
##### response

```angular2html
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1ODI5MTUxOCwianRpIjoiZGY3MWYwMjctMmE5Yy00ZWEwLTkyMDUtYTA0ZWU5YTA1NTFkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InFAcXEucSIsIm5iZiI6MTY1ODI5MTUxOCwiZXhwIjoxNjU4MjkyNzE4fQ.K0F__RL0flRzZmvQba5WDXzko8Lrt52OH0uHlUMGEPA",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1ODI5MTUxOCwianRpIjoiNGNjNWM3ZjYtZWUzOS00NzRjLWFhM2UtZGY1NTEzMDg0NTNhIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJxQHFxLnEiLCJuYmYiOjE2NTgyOTE1MTgsImV4cCI6MTY1OTUwMTExOH0.Jr1epo4dLFzZsOAwFVWBUu2o9pJICWDxWU724IO32iM"
}
```

### POST /api/photos
##### body
```
form data - flie binary
```
##### response

```angular2html
{
    "black_photo_id":1,
    "color_photo_id":2  
}
```

### /api/photos/<photo_id>
```
        {"photo": 'test/newFile.png'}
```



### /api/photos

```angular2html
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
```