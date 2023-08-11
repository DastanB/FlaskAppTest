# FlaskAppTest

This little app is designed to receive mp4 video and detect objects with provided propability accuracy.

Entrypoint URL: 'http://127.0.0.1:<port>/objects/'

Form-Data: 
```json
{
  "video": file.mp4
}
```

Success response 200:
```json
{
  "results": [
    [{"person": 0.98}, {"cat": 0.95}],
    [{"person": 0.98}, {"cat": 0.95}],
    [{"person": 0.98}, {"cat": 0.95}]
  ]
}
```

# Flow

<img width="820" alt="Screen Shot 2023-08-11 at 20 25 36" src="https://github.com/DastanB/FlaskAppTest/assets/22112395/20824d4d-d6f3-4c87-8dd3-b8318e65660b">
