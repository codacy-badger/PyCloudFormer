import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-cloud-former",
    version="0.1",
    author="DirkScgm",
    author_email="dirkscgm@gmail.com",
    description="Cloud Formation Program that generates AWS CloudFormation scripts in YAML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DirksCGM/PyCloudFormer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
)
