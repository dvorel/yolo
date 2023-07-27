import os
from random import sample
from tqdm import tqdm
import shutil

#define class numbers to remove
CLASSES = [1, 2, 3]

#paths
DIR = "./yolo/splitted"
TRAIN_DIR = "train"
TEST_DIR = "test"

LBL_DIR = "labels"
IMG_DIR = "images"


if __name__=="__main__":
    #get image and annotation names
    if TRAIN_DIR is not None:
        train_lbl = os.listdir(os.path.join(DIR, TRAIN_DIR, LBL_DIR))
        train_img = os.listdir(os.path.join(DIR, TRAIN_DIR, IMG_DIR))

    if TEST_DIR is not None:
        test_lbl = os.listdir(os.path.join(DIR, TEST_DIR, LBL_DIR))
        test_img = os.listdir(os.path.join(DIR, TEST_DIR, IMG_DIR))


    #train labels
    for i in tqdm(range(len(train_lbl))):
        lines = []
        with open(os.path.join(DIR, TRAIN_DIR, LBL_DIR, train_lbl[i]), 'r+') as fp:
            lines = fp.readlines()

        if len(lines) == 0:
            os.remove(os.path.join(DIR, TRAIN_DIR, LBL_DIR, train_lbl[i]))
            os.remove(os.path.join(DIR, TRAIN_DIR, IMG_DIR, train_img[i]))

    #test labels
    for i in tqdm(range(len(test_lbl))):
        lines = []
        with open(os.path.join(DIR, TEST_DIR, LBL_DIR, test_lbl[i]), 'r+') as fp:
            lines = fp.readlines()

        if len(lines) == 0:
            os.remove(os.path.join(DIR, TEST_DIR, LBL_DIR, test_lbl[i]))
            os.remove(os.path.join(DIR, TEST_DIR, IMG_DIR, test_img[i]))
