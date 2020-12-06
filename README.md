# ShapeFromShading
Converting Images of seals into 3D objects

Part of the Coding Da Vinci Niedersachsen 2020 Hackathon, we scan images of seals and produce 3D object out of them.

## Instruction:
You need Python version >= 3.8

### Unix
```
python -m venv venv
. venv/bin/activate
pip install -e . -r requirements.txt
sealconvert3d [your source file]
```

### Windows
```
python -m venv venv
.\venv\Scripts\activate.bat
pip install -e . -r requirements.txt
sealconvert3d [your source file]
```

## Usage

For development, after clone, run:
```
pip install -e . -r requirements.txt
```

Now,
```
sealconvert3d [args]
```
should be available in your command line.
