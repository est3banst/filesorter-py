import os, shutil

path = r'C:/Users/esteb/Downloads'
print(os.listdir(path))
my_files = os.listdir(path)

for file in my_files:
    name, ext = os.path.splitext(file)

    ext = ext[1:]
    if ext == '':
        continue

    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext)

    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext)


if __name__ == 'main':
    print("Works")




