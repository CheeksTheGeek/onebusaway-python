# setup.py
from setuptools import setup

setup(
    name="onebusaway",
    version="0.1",
    description="The OneBusAway Python Client is a Python library for interacting with the OneBusAway API. It provides a simple and convenient way to access real-time transit data, schedules, and other information from various transit agencies.",
    author="Chaitanya Sharma",
    url="https://github.com/CheeksTheGeek/onebusaway-python",
    license="MIT",
    py_modules=["onebusaway"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
