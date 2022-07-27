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
'message': 'Login Successfully'
}
```

### POST /api/logout


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
```