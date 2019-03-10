import glob
from shutil import copyfile

DST = r"Images/"


def copy(path):
    for src in glob.glob(path + "/*"):
        name = src.split("\\")[2]
        copyfile(src, DST+name)
        print(name)


def main():
    for file in glob.glob('Images_original/*'):
        # print(file)
        name = file.split("\\")[1]
        copy(file)


    print('Successfully copied to location.')


main()
