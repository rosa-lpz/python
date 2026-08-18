# Zipfile
The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file. 
This module does not handle multipart ZIP files. It can handle ZIP files that use the ZIP64 extensions (that is ZIP files that are more than 4 GiB in size). It supports decryption of encrypted files in ZIP archives, but it cannot create an encrypted file. Decryption is extremely slow as it is implemented in native Python rather than C.

## Example 1


```python
import zipfile
import os

# Define the zip file path (your zip file location)
zip_file_path = 'path/to/your/file.zip'

# Get the current working directory (current folder where the script is running)
extract_to_folder = os.getcwd()

try:
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
    print(f"Extracted all files to {extract_to_folder}")
except FileNotFoundError:
    print(f"Error: The file {zip_file_path} was not found.")
except zipfile.BadZipFile:
    print(f"Error: The file {zip_file_path} is not a valid zip file.")
except PermissionError:
    print(f"Error: Permission denied when accessing {zip_file_path} or {extract_to_folder}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```


How it works:

* The script will now extract the contents of data.zip to the same folder where the script is running. If you run the script in the /home/user/myproject directory, it will extract the files there.


# References
* https://docs.python.org/3/library/zipfile.html