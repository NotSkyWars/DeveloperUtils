import os
import shutil
import time
import tkinter
from tkinter import filedialog

import tkinterdnd2


def UploadAction(event=None):
    filepath = filedialog.askopenfilename()
    filename = filepath.split('/')[len(filepath.split('/')) - 1]
    path = os.path.join("C:\\Users\\Christian\\OneDrive\\Desktop\\Manager\\", filename)
    shutil.move(filepath, path)
    moveFiles()
    print("Success")


def createWindow():
    root = tkinter.Tk()
    root.geometry('200x200')
    button = tkinter.Button(root, text='Open', command=UploadAction)
    button.pack()
    root.mainloop()


def createFolder():
    path = "C:\\Users\\Christian\\OneDrive\\Desktop\\Manager\\"
    os.chdir(path)
    if not os.path.exists(os.path.join(path, 'Renders')):
        os.mkdir(os.path.join(path, 'Renders'))
    if not os.path.exists(os.path.join(path, 'Logos')):
        os.mkdir(os.path.join(path, 'Logos'))
    if not os.path.exists(os.path.join(path, 'Done')):
        os.mkdir(os.path.join(path, 'Done'))
    if not os.path.exists(os.path.join(path, 'trashbin')):
        os.mkdir(os.path.join(path, 'trashbin'))


def moveFiles():
    createFolder()
    path = "C:\\Users\\Christian\\OneDrive\\Desktop\\Manager\\"
    entries = os.listdir(path)
    for entry in entries:
        if os.path.isfile(os.path.join(path, entry)):
            if 'Render' in entry:
                ds = "C:\\Users\\Christian\\OneDrive\\Desktop\\Manager\\Renders"
                shutil.move(os.path.join(path, entry), os.path.join(ds, entry))
            elif 'done' in entry:
                ds = "C:\\Users\\Christian\\OneDrive\\Desktop\\Manager\\Done"
                shutil.move(os.path.join(path, entry), os.path.join(ds, entry))
            elif 'Logo' in entry:
                ds = "C:\\Users\\Christian\\OneDrive\\Desktop\\Manager\\Logos"
                shutil.move(os.path.join(path, entry), os.path.join(ds, entry))
            else:
                ds = "C:\\Users\\Christian\\OneDrive\\Desktop\\Manager\\trashbin"
                shutil.move(os.path.join(path, entry), os.path.join(ds, entry))
    print("sleep")
    time.sleep(5)


def main():
    createWindow()
    moveFiles()


if __name__ == '__main__':
    main()
