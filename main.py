import pytsk3

def has_signature(file_entry):
    file_data = file_entry.read_random(0, len(signature))

    return file_data == signature


def save_file(file_entry, output_dir):
    file_size = file_entry.info.meta.size
    file_data = file_entry.read_random(0, file_size)

    output_path = output_dir + '\\' + str(entry.info.name.name)[2:-1]
    with open(output_path, 'wb') as output_file:
        output_file.write(file_data)


image_file_path = "D:\\folder_image\\forensic.001"

image_handle = pytsk3.Img_Info(image_file_path)

image_fs = pytsk3.FS_Info(image_handle)

signature = b'\x50\x4B\x03\x04'

output_directory = 'C:\\Users\\user\\PycharmProjects\\forensic\\docs'

root_directory = image_fs.open_dir(path='/')

for entry in root_directory:

    if hasattr(entry.info.meta,
               "type") and entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_REG and entry.info.meta.size > 0:

        if has_signature(entry):

            save_file(entry, output_directory)
            print(f'DOCX found and saved in: docx/{str(entry.info.name.name)[2:-1]}')
