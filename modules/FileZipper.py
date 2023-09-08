import zipfile as zip
import pathlib

def archive_maker(filepaths,directory):
    dest_dir = pathlib.Path(directory,"compressed.zip")
    with zip.ZipFile(dest_dir,'w') as arch:
        for file in filepaths:
            file = pathlib.Path(file)
            arch.write(file, arcname=file.name)


if __name__ == "__main__" :
    file = ["../bonus/bonus1.py","../bonus/bonus2.py"]
    dir = "../bonus/dest"

    archive_maker(file, dir)
