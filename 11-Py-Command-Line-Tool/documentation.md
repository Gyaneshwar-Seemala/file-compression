# PyCompress - File Compression Utility Documentation
**-Gyaneshwar Rao**

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
    1. [Compress Files](#compress-files)
    2. [Decompress Files](#decompress-files)
5. [Code Explanation](#code-explanation)
    1. [Importing Required Libraries](#importing-required-libraries)
    2. [Compress Files Function](#compress-files-function)
    3. [Decompress Files Function](#decompress-files-function)
    4. [Main Execution Block](#main-execution-block)
6. [Conclusion](#conclusion)

## 1. Introduction <a name="introduction"></a>
PyCompress is a Python program designed to provide a simple and efficient file compression utility. It allows users to compress and decompress files and directories. This documentation explains how to use the application, its prerequisites, and the structure of the code.

## 2. Prerequisites <a name="prerequisites"></a>
Before using PyCompress, ensure you have the following:
- Python 3.x installed on your system.

## 3. Getting Started <a name="getting-started"></a>
To start using PyCompress, follow these steps:
- Ensure Python 3.x is installed on your system.
- Save the Python code to a file, for example, `pycompress.py`.
- Open a terminal or command prompt and navigate to the directory where the code file is located.
- Run the application by executing the following command:
  ```bash
  python pycompress.py
  ```
  
## 4. Usage <a name="usage"></a>
PyCompress provides two main operations: compressing and decompressing files.

### Compress Files <a name="compress-files"></a>
1. Choose the compress operation by entering 'c' when prompted.
2. Provide the output location and filename for the compressed archive.
3. Enter the file(s) or directory(ies) to compress, separated by spaces.

### Decompress Files <a name="decompress-files"></a>
1. Choose the decompress operation by entering 'd' when prompted.
2. Enter the compressed file to decompress.
3. Enter the output directory for decompressed files.

## 5. Code Explanation <a name="code-explanation"></a>
The PyCompress code is structured into components and functions. Here's an overview:

### Importing Required Libraries <a name="importing-required-libraries"></a>
The code begins by importing the necessary libraries:
- `os`: Provides a way to interact with the operating system.
- `argparse`: Parses command-line arguments.
- `zipfile`: Enables compression and decompression of files.

### Compress Files Function <a name="compress-files-function"></a>
The `compress_files` function compresses files and directories. It handles different cases, such as single files, directories, and errors during the compression process.

### Decompress Files Function <a name="decompress-files-function"></a>
The `decompress_files` function decompresses a zip file and extracts its contents to a specified output path.

### Main Execution Block <a name="main-execution-block"></a>
The `main` function sets up an argument parser, prompts the user for the compression or decompression operation, and handles user inputs accordingly.

## 6. Conclusion <a name="conclusion"></a>
PyCompress is a versatile file compression utility that provides a straightforward interface for compressing and decompressing files and directories. This documentation serves as a guide for users, detailing the application's features and providing insights into the code structure. Feel free to customize and use PyCompress based on your file compression needs.