# PDF to Speech

This is a standard python package 

Smartreader is a Python library for for converting and PDF content to Speech .




## IN Virtual Environment(Recommended):
>conda info -e # To see list of environment

>conda create -n yourenvname python=x.x 

>conda activate yourenvname

>conda install git

>Use the package manager> [pip] install git+https://github.com/AnkitAnand2/smartreader #to install Smartreader
>conda deactivate# To deactivate virtual environment

>conda env remove -n yourenvname #To remove any environment permanently.


## Normal installation:

Use the package manager [pip] install git+https://github.com/AnkitAnand2/smartreader.git to install Smartreader

## Installation using .rar file:

>python setup.py install



## Usage

```python
from Smartreader import Smartreader

Smartreader.readline() 
file_path=input('Enter the path of file: ')# Input the location of the pdf file to read
file_name=input('Enter the pdf file name: ')# Input the pdf file name
inputpage=int(input("Enter the page Number : "))# Input the page name

```

## requirements.txt file

This contains all the packages used.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.




