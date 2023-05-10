import string
from typing import List
from PIL import Image
import numpy as np
import os


def start_preprocessing(images: np.ndarray[string], directory: string):
    pre_processed_images = []
    resized_images = []
    for i in range(len(images)):
        image = Image.open(directory+images[i])
        resized_images.append(avg_pooling(image, 3))
    for i in range(len(resized_images)):
        different_images = three_different_images(resized_images[i])
        pre_processed_images.extend(different_images)
    print(len(pre_processed_images))


def avg_pooling(image: Image, block_size):
    img = np.array(image)
    h, w, c = img.shape
    new_h = h // block_size
    new_w = w // block_size
    new_img = np.zeros((new_h, new_w, c), dtype=np.uint8)
    for i in range(new_h):
        for j in range(new_w):
            block = img[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size, :]
            new_img[i, j, :] = np.rint(np.mean(block, axis=(0, 1)))
    return Image.fromarray(new_img)


def three_different_images(image: Image):
    horizontal = np.flip(image, axis=1)
    vertical = np.flip(image, axis=0)
    return image, Image.fromarray(horizontal), Image.fromarray(vertical)
