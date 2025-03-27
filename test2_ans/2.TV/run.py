import os

def rename_jpg_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):  # Kiểm tra file có đuôi .jpg
            old_path = os.path.join(folder_path, filename)
            new_filename = filename[:-4] + ".JPG"  # Thay .jpg thành .JPG
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Thay "your_folder_path" bằng đường dẫn đến thư mục cần đổi tên
folder_path = "C:/Users/TGDD/Downloads/test2_ans/2.TV"
rename_jpg_files(folder_path)
