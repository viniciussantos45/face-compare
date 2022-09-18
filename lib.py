import os
import os.path


def getImages(path="/images"):

    imgs = []
    valid_images = [".jpg", ".png", ".jpeg"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append((os.path.join(path, f)))

    return imgs
