from setuptools import find_packages, setup
from typing import List

HYPON_E_DOT ='-e .'
def get_requirements(file_path:str) ->List[str]:

    '''This function returns a list of requirements'''

    requirements = []
    with open ('requirements.txt') as fill_obj:
        requirements = fill_obj.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]

        if HYPON_E_DOT in requirements:
            requirements.remove(HYPON_E_DOT)
    
    return requirements


setup(
name = 'ML Project',
version = '0.0.1',
author= 'Hardik',
author_email = 'hardikuk05@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)