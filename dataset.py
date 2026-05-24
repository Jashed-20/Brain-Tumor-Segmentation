!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d mateuszbuda/lgg-mri-segmentation

!unzip lgg-mri-segmentation.zip

import os
import cv2
import matplotlib.pyplot as plt

dataset_path = "/content/lgg-mri-segmentation/kaggle_3m"

image_paths = []
mask_paths = []

for patient_folder in os.listdir(dataset_path):

    patient_path = os.path.join(dataset_path, patient_folder)

    if os.path.isdir(patient_path):

        for file in os.listdir(patient_path):

            full_path = os.path.join(patient_path, file)

            if "mask" in file:
                mask_paths.append(full_path)

            elif file.endswith(".tif"):
                image_paths.append(full_path)

image_paths = sorted(image_paths)
mask_paths = sorted(mask_paths)

print("Images:", len(image_paths))
print("Masks:", len(mask_paths))

for i in range(2):

    image = cv2.imread(image_paths[i])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    mask = cv2.imread(mask_paths[i], 0)

    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.imshow(image)
    plt.title("MRI Image")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(mask, cmap='gray')
    plt.title("Tumor Mask")
    plt.axis("off")

    plt.show()

