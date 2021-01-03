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

Options are:
```
usage: sealconvert3d [-h] [-o OUTPUT] [-alg {tsai_shah,tsai_shah_specular}] [-s SLANT] [-t TILT] [-i ITERATIONS] [-l LOGLEVEL] source

Seal Shape From Shading out of Potsdam

positional arguments:
  source

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Filename to write to
  -alg {tsai_shah,tsai_shah_specular}, --algorithm {tsai_shah,tsai_shah_specular}
                        Shape from Shading Algorithm to use
  -s SLANT, --slant SLANT
                        Slant of lighting source
  -t TILT, --tilt TILT  Tilt of lighting source
  -i ITERATIONS, --iterations ITERATIONS
                        Iterations to run the algorithm through
  -l LOGLEVEL, --loglevel LOGLEVEL
                        Set debugging level. Use "debug" for highest details
```
