# first import required libraries
import os
import argparse
import zipfile

# creating a function to compress files
def compress_files(input_paths, output_path):
    try:
        if os.path.isdir(output_path):
            output_path = os.path.join(output_path, 'output.zip')

        with zipfile.ZipFile(output_path, 'w') as zip_file:
            for input_path in input_paths:
                if os.path.isfile(input_path):
                    zip_file.write(input_path, os.path.basename(input_path))
                elif os.path.isdir(input_path):
                    for root, _, files in os.walk(input_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            zip_file.write(file_path, os.path.relpath(file_path, input_path))
                else:
                    raise ValueError(f"Invalid input: {input_path}. Please provide valid file(s) or directory(ies).")

        print(f"Compression successful. Output saved to {output_path}")

    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error.filename}. Please provide a valid file or directory.")
    except IsADirectoryError as isdir_error:
        print(f"Invalid input: {isdir_error.filename} is a directory. Please provide a valid file or directory.")
    except Exception as e:
        print(f"Compression failed: {str(e)}")

# a function to decompress files
def decompress_files(input_path, output_path):
    try:
        with zipfile.ZipFile(input_path, 'r') as zip_file:
            zip_file.extractall(output_path)

        print(f"Decompression successful. Files extracted to {output_path}")

    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error.filename}. Please provide a valid compressed file.")
    except Exception as e:
        print(f"Decompression failed: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="PyCompress - File Compression Utility")

    parser.add_argument('-o', '--output', help='Output location and filename for the compressed or decompressed archive')
    args = parser.parse_args()

    try:
        # Ask the user whether they want to compress or decompress files
        operation = input("Do you want to compress or decompress files? (c/d): ").lower()

        if operation == 'c':
            if args.output:
                output_path = args.output
            else:
                output_path = input("Enter output location and filename for the compressed archive: ")

            input_paths = input("Enter file(s) or directory(ies) to compress (space-separated): ").split()
            compress_files(input_paths, output_path)

        elif operation == 'd':
            input_path = input("Enter the compressed file to decompress: ")
            output_path = input("Enter the output directory for decompressed files: ")
            decompress_files(input_path, output_path)

        else:
            print("Invalid operation. Please enter 'c' for compress or 'd' for decompress.")

    except Exception as main_error:
        print(f"An unexpected error occurred: {str(main_error)}")

if __name__ == "__main__":
    main()