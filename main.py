import pytsk3


# Function to check if a file has a specific signature
def has_signature(file_entry):
    file_data = file_entry.read_random(0, len(signature))

    return file_data == signature


# Function to save a file to disk
def save_file(file_entry, output_dir):
    file_size = file_entry.info.meta.size
    file_data = file_entry.read_random(0, file_size)

    output_path = output_dir + '\\' + str(entry.info.name.name)[2:-1]
    with open(output_path, 'wb') as output_file:
        output_file.write(file_data)


image_file_path = "D:\\folder_image\\forensic.001"  # Replace with the actual path to the image file

# Open the image file as a handle
image_handle = pytsk3.Img_Info(image_file_path)

# Open the image file system
image_fs = pytsk3.FS_Info(image_handle)

# signature that we want to find
signature = b'\x50\x4B\x03\x04'

# Output directory to save the matching files
output_directory = 'C:\\Users\\user\\PycharmProjects\\forensic\\docs'

# Get the root directory of the image file system
root_directory = image_fs.open_dir(path='/')

# List all files and directories in the root directory
for entry in root_directory:
    # check if file is can handle
    if hasattr(entry.info.meta,
               "type") and entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_REG and entry.info.meta.size > 0:
        # Check if the file has the desired signature
        if has_signature(entry):
            # Save the matching file to disk
            save_file(entry, output_directory)
            print(f'PDF found and saved in: docs/{str(entry.info.name.name)[2:-1]}')
