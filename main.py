from pre_processing import *


if __name__ == '__main__':
    directory = "Images/"
    images = np.array(os.listdir(directory))
    start_preprocessing(images, directory)

