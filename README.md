# PDF to Speech

This is a standard python package 

Smartreader is a Python library for for converting and PDF content to Speech .




## IN Virtual Environment(Recommended):
>conda info -e # To see list of environment

>conda create -n yourenvname python=x.x 

>conda activate yourenvname

>conda install git

>Use the package manager> [pip] install git+https://AnkitAnand2@bitbucket.org/AnkitAnand2/weather_api_call  #to install weather_py

>conda deactivate# To deactivate virtual environment

>conda env remove -n yourenvname #To remove any environment permanently.


## Normal installation:

Use the package manager [pip] install git+https://AnkitAnand2@bitbucket.org/AnkitAnand2/weather_api_call to install weather_py

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




