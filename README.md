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
{
  "results": [
    [{"person": 0.98}, {"cat": 0.95}],
    [{"person": 0.98}, {"cat": 0.95}],
    [{"person": 0.98}, {"cat": 0.95}]
  ]
}

Flow
<img width="744" alt="Screen Shot 2023-08-11 at 20 14 55" src="https://github.com/DastanB/FlaskAppTest/assets/22112395/a638c684-5909-4848-a217-0545e97da453">
