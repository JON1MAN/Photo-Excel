import os
import cv2
from img2table.document import Image
from img2table.ocr import TesseractOCR

def convert_to_gray_scale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresholding = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    return thresholding

ocr = TesseractOCR(n_threads=4)

# Paths
input_folder = "../main_script/input/"
output_excel = "../main_script/output/"
preprocessed_folder = '../main_script/preprocessed_images/'

if not os.path.exists(preprocessed_folder):
    os.makedirs(preprocessed_folder)

for i, filename in enumerate(os.listdir(input_folder)):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        thresholding = convert_to_gray_scale(img)

        processed_img_name = f"processed_file_{i}.png"
        cv2.imwrite(os.path.join(preprocessed_folder, processed_img_name), thresholding)

        preprocessed_img = Image(src=os.path.join(preprocessed_folder, processed_img_name))
        excel_name = f"table_{i}.xlsx"
        preprocessed_img.to_xlsx(os.path.join(output_excel, excel_name),
                                 ocr=ocr,
                                 min_confidence=50)