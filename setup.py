import setuptools

setuptools.setup(
    name="ShapeFromShading",
    version="0.0.1",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=['shapefromshading'],
    entry_points={
        'console_scripts': [
            'sealconvert3d = shapefromshading.main:main',
        ],
    },
)
