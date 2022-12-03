from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Code to enable the use of the gaussian and the binomial distributions'
LONG_DESCRIPTION = 'A package that allows to create and manipulate gaussian and binomial distributions based on the statistics theory'

# Setting up
setup(
    name="gauss_binomial_statdist",
    version=VERSION,
    author="Oumayma EL-FAHSI",
    author_email="<oumayma.elfahsi@ump.ac.ma>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['matplotlib'],
    keywords=['python', 'gaussian', 'binomial', 'distributions', 'mean', 'standard deviation' ,'statistics'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)