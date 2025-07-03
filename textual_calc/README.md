# App
Calc App made with textual

## Requirements
```console
$ python -m venv venv
$ venv\Scripts\activate 
$ pip install textual
```

## How to Run
```console
$ python calculator.py
```


## How to create an executable

```console
pip install pyinstaller 
```

```console
pyinstaller calculator.py 
```


```console
pyinstaller --add-data "calculator.css;." calculator.py 
```

```console
pyinstaller --onefile --icon=./calculator.ico --add-data "calculator.css;." calculator.py 
```


# Reference
https://textual.textualize.io/