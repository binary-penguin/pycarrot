from setuptools import setup, find_packages

VERSION = '0.7.7' 
DESCRIPTION = 'Easy Desktop GUIs'
LONG_DESCRIPTION = 'The easiest way to create Desktop GUIs with Python'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pycarrot", 
        version=VERSION,
        author="Jorge Flores",
        author_email="<jafp07@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
