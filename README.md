# ImageDimensionChecker

ImageDimensionChecker is a Python package designed to streamline the process of analyzing image datasets. It provides functions to check if images in a directory have the same dimensions, count the number of unique file extensions, and identify unique image dimensions.

# Features

Check Image Dimensions: Determine if all images in a directory have the same dimensions.

Count Unique File Extensions: Count the occurrences of each unique file extension in a directory.

Identify Unique Image Dimensions: Find the unique dimensions (width and height) of images in a directory.

# Installation

You can install ImageDimensionChecker via pip:

pip install ImageDimensionChecker

# Usage

Here's a quick guide on how to use ImageDimensionChecker:

# Check Image Dimensions

from ImageDimensionChecker import CheckImageDimension

<!-- Specify the path to the directory containing images -->
path = "/path/to/images"

CheckImageDimension(path)

# Count Unique File Extensions

from ImageDimensionChecker import unique_extension

<!-- Specify the path to the directory containing images -->
path = "/path/to/images"

unique_extension(path)

# Identify Unique Image Dimensions

from ImageDimensionChecker import unique_dimension

path = "/path/to/images"

unique_dimension(path)

# License

This project is licensed under the BSD License - see the LICENSE file for details.

# Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

# Acknowledgements

This package was inspired by the repetitive tasks involved in image dataset analysis during machine learning model development.