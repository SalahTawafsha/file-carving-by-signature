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


# disk image path
disk_image_path = "D:\\folder_image\\forensic.001"

# Open the image file as a handle
image_handle = pytsk3.Img_Info(disk_image_path)

# Open the image file system
ad1_fs = pytsk3.FS_Info(image_handle)

# select file signature that we want to get all files that has it
signature = b'\x50\x4B\x03\x04'

# Output directory to save the matching files
output_directory = 'C:\\Users\\user\\PycharmProjects\\forensic\\docs'

# Get the root directory of the .ad1 file system
root_directory = ad1_fs.open_dir(path='/')

# List all files and directories in the root directory
for entry in root_directory:
    # print entry name
    if hasattr(entry.info.meta,
               "type") and entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_REG and entry.info.meta.size > 0:
        # Check if the file has the desired signature
        if has_signature(entry):
            # Save the matching file to disk
            save_file(entry, output_directory)
            print(f'PDF found and saved in: docs/{str(entry.info.name.name)[2:-1]}')
