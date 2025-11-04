from setuptools import find_packages, setup
from typing import List

# Declaring a constant for the -e . flag
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # The list comprehension cleans up the '\n' character from each line
        requirements = [req.replace('\n', '') for req in requirements] 

        # This removes the special '-e .' flag from the requirements list
        # so it doesn't try to install it as a library name
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Absaar',
    author_email='absar.aasher@gmail.com', # Corrected email domain
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)