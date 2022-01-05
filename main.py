import tkinter as tk
import io, sys, zlib
from tkinter import messagebox

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

labelInputLink = tk.Label(root, text='Original Link: ')
canvas.create_window(200, 150, window=labelInputLink)

entryInputLink = tk.Entry(root)
canvas.create_window(300, 150, window=entryInputLink)


def generateLink():
    link = entryInputLink.get()
    print(link)
    linklen = len(link)
    for i in range(linklen - 1):
        if (link[i] == '/' and link[i + 1] == '/') or (i > 0 and link[i] == '/' and link[i - 1] == '/'):
            continue

        elif link[i] == '/':
            trimlink = link[i + 1:]
            break
    print(trimlink)

    labelGeneratedLink = tk.Label(root, text='Generated Link: ')
    canvas.create_window(200, 250, window=labelGeneratedLink)

    newlink = "Dummy value"
    txtGeneratedLink = tk.Text(root, height=1, width=20)
    canvas.create_window(325, 250, window=txtGeneratedLink)
    txtGeneratedLink.insert(tk.END, trimlink)
    # txtGeneratedLink.config(state='readonly')

    hashedlink = zlib.adler32(trimlink.encode('utf-8'))
    print(hashedlink)
    print(bytes(hashedlink).decode('utf-8'))


btnGenerateLink = tk.Button(root, text='Generate Link', command=generateLink)
canvas.create_window(200, 200, window=btnGenerateLink)

root.mainloop()