class File:
    def __new__(cls, *args, **kwargs):
        file_type = kwargs.get("file_name").split(".")[-1]

        if file_type == "txt":
            for i in cls.__subclasses__():
                if i.__name__ == "TextFile":
                    return super().__new__(i)
        elif file_type in ["jpg", "png", "jpeg"]:
            for i in cls.__subclasses__():
                if i.__name__ == "ImageFile":
                    return super().__new__(i)
        else:
            return super().__new__(File)

    def __init__(self, file_name=""):
        self.file_name = file_name


class ImageFile(File):
    def __init__(self, *args, **kwargs):
        self.height = kwargs.get("height")
        self.width = kwargs.get("width")

    def __str__(self):
        return f"Image File of || Width : {self.width} , Height : {self.height}"


class TextFile(File):
    def __init__(self, *args, **kwargs):
        self.file_size = kwargs.get("file_size")

    def __str__(self):
        return f"Text File of || Size : {self.file_size}"


text_file = File(file_name="imagefile.png", height=100, width=100)
image_file = File(file_name="testfile.txt", file_size=500)
other_file = File(file_name="video_file.mp4")

print(text_file)
print(image_file)
print(other_file)
