# PyCalc

PyCalc is a sample calculator implemented using Python 3 and with a [PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html) GUI. PyCalc implements basic math operations, including division, multiplication, addition, and subtraction.

PyCalc is intended to be a demonstrative example of how to build a Python + PyQt6 GUI application using the Model-View-Controller (MVC) pattern.

## Requirements

For PyCalc to work, you need to have [Python](https://www.python.org) >= 3.6.1. Then you need to install the PyQt6 library. You can do this by using `pip` in a Python virtual environment:

```console
$ python -m venv venv
$ venv\Scripts\activate 
$ pip install pyqt6
```

After these commands have finished, you can run PyCalc as described in the next section.

## How to Run PyCalc

To run PyCalc from your system's command line or terminal, execute the following command:

```console
$ python pycalc.py
```

After running this command, you'll get PyCalc running on your machine.

## How to Use PyCalc

To use PyCalc, just enter a valid math expression using your mouse and then press `Enter` or click the `=` button to get the result:


## How to create an executable

```console
pip install pyinstaller
```

To make it disappear we have to indicate that it is a windowed application
```console
pyinstaller --windowed --icon=./icono.ico pycalc.py 
```

We can use a command to generate a single executable file that contains everything.
```console
pyinstaller --windowed --onefile --icon=./icono.ico pycalc.py 
```

We will have the executable file in the dist folder

## References
- https://github.com/realpython/materials/blob/master/pyqt-calculator-tutorial/pycalc/README.md


