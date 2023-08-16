from dotenv import load_dotenv
from os import getenv
from setuptools import setup, find_packages
 
load_dotenv()

EMAIL = getenv("EMAIL")
AUTHOR = getenv("AUTHOR")
 
setup(
    name = "py_lava_api",
    version = "0.1.0",
    keywords = ("lava", ),
    description = "Simple work with lava",
    long_description = "Simple work with lava",
    license = "MIT Licence",
 
    url = "https://github.com/DephPhascow/py-graphql",
    author = AUTHOR,
    author_email = EMAIL,
 
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["requests"]
)