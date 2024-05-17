import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ImageDimensionChecker',
    version='1.4.3',
    author="Anurupa Karmakar",
    author_email="anurupakarmakar.dgp18@gmail.com",
    description="Checking dimension of multiple images during Image processing",
    long_description=long_description,  # Include README contents here
    long_description_content_type="text/markdown",  
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
    ],
)
