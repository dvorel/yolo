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

if __name__=="__main__":
    #get image and annotation names
    if TRAIN_DIR is not None:
        train_lbl = os.listdir(os.path.join(DIR, TRAIN_DIR, LBL_DIR))

    if TEST_DIR is not None:
        test_lbl = os.listdir(os.path.join(DIR, TEST_DIR, LBL_DIR))


    #train labels
    for label in tqdm(train_lbl):
        with open(os.path.join(DIR, TRAIN_DIR, LBL_DIR, label), 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()

            for line in lines:
                cls_num = int(line.split(" ")[0])
                if cls_num not in CLASSES:
                    fp.write(line)

    #test labels
    for label in tqdm(test_lbl):
        with open(os.path.join(DIR, TEST_DIR, LBL_DIR, label), 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()

            for line in lines:
                cls_num = int(line.split(" ")[0])
                if cls_num not in CLASSES:
                    fp.write(line)
