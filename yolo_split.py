import os
from random import sample
from tqdm import tqdm
import shutil


DIR = "./yolo/train"
OUT_DIR = "./yolo/splitted"
PERCENTAGE = 20

IMG_DIR = "images"
LBL_DIR = "labels"

if __name__=="__main__":
    #get image and annotation names
    images = os.listdir(os.path.join(DIR, IMG_DIR))
    annotations = os.listdir(os.path.join(DIR, LBL_DIR))
    
    #check if len-s are same
    if len(images) != len(annotations):
        print("Dataset corrupted!")
        quit()

    #make all dirs
    os.makedirs(os.path.join(OUT_DIR, "train", LBL_DIR), exist_ok=True)
    os.makedirs(os.path.join(OUT_DIR, "train", IMG_DIR), exist_ok=True)
    os.makedirs(os.path.join(OUT_DIR, "test", LBL_DIR), exist_ok=True)
    os.makedirs(os.path.join(OUT_DIR, "test", IMG_DIR), exist_ok=True)


    #define split
    num = len(images)
    test_num = int(num*(PERCENTAGE/100))
    train_num = num-test_num

    test_rnd = sample(range(num), train_num)

    for i in tqdm(range(num)):
        if i in test_rnd:
            shutil.copy(os.path.join(DIR, IMG_DIR, images[i]),
                            os.path.join(OUT_DIR, "test", IMG_DIR)
            )

            shutil.copy(os.path.join(DIR, LBL_DIR, annotations[i]),
                            os.path.join(OUT_DIR, "test", LBL_DIR)
            )
        else:
            shutil.copy(os.path.join(DIR, IMG_DIR, images[i]),
                            os.path.join(OUT_DIR, "train", IMG_DIR)
            )

            shutil.copy(os.path.join(DIR, LBL_DIR, annotations[i]),
                            os.path.join(OUT_DIR, "train", LBL_DIR)
            )
