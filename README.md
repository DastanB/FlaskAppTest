<img width="820" alt="Screen Shot 2023-08-11 at 21 52 48" src="https://github.com/DastanB/FlaskAppTest/assets/22112395/91b2b646-66e3-4ea5-8a0e-edaf5c5d7825"># FlaskAppTest

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
    [
      {
        "person": 0.98
      },
      {
        "cat": 0.95
      }
    ],
    [
      {
        "person": 0.98
      },
      {
        "cat": 0.95
      }
    ],
    [
      {
        "person": 0.98
      },
      {
        "cat": 0.95
      }
    ]
  ]
}
```

# Flow

<img width="820" alt="Screen Shot 2023-08-11 at 21 53 06" src="https://github.com/DastanB/FlaskAppTest/assets/22112395/8c5758a6-884e-4da9-abde-c2a9ef01b6fe">


