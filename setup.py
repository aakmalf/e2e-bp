from setuptools import setup, find_packages
from typing import List


HYPEN_DOT_E = "-e ."

def read_requirements(file_path: str) -> List[str]:
    
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
    
    if HYPEN_DOT_E in requirements:
        requirements.remove(HYPEN_DOT_E)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="akmal",
    author_email="akmalfauzi001@gmail.com", 
    packages=find_packages(),
    # include_package_data=True,
    install_requires=read_requirements("requirements.txt")
    # entry_points="""
    #     [console_scripts]
    #     src=src.cli:app
    # """,
)

# if __name__ == "__main__":
#     print(read_requirements("requirements.txt"))
    