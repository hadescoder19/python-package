import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="olympus-hadescoder19", # Replace with your own username
    version="0.0.1",
    author="hadescoder19",
    author_email="ealex3@yahoo.com",
    description="test package",
    long_description=long_description,
    long_description_content_type="test package",
    url="https://github.com/hadescoder19/python-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
