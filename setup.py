from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT='-e .'
def get_packages(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n",'') for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements
    


setup(
    name="ML Project",
    version='0.0.1',
    author='Aravind',
    author_email='aravindyeduri@gmail.com',
    packages=find_packages(),
    install_requires=get_packages('requirements.txt')
)