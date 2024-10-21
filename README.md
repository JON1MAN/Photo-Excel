# Photo-Excel
## App for converting table from image to .xlsx format

Hi, my name is Aliaks and I study Electronics and Telecommunication. I and my colleagues have a lot of labs, where we do researches with a different hardware. After classes we need to make report about our research, so we need to have our measurements to perform some excel work. And here is a problem: some hardware (oscyloscopes and etc.) don't have an option to write measurements to .csv, so we need to take a picture on our phone and then rewrite it to excel, you will say "maaan wtf, it's just wasting of time", but yeah, there some cases where we can't do it in different way.

## So that's why

I decided to use my programming skills and create such app (right now it is a simple script) on python to help us.
I've made a research and found great library img2table:
[Link to this library][df1]

## How it works 

## Using TesseractOCR

There are few steps, to understand how this script works
1) we need to take an image
   ![img_1](https://github.com/user-attachments/assets/820b023e-c913-4cbf-9a41-046b0272b08e)

```sh
img = cv2.imread(img_path)
```

2) then we need to convert this image to gray scale and replace bright pixels with black color and dark pixels to white (so then TesseractOCR be able to process it more easily and accurately.)
   ![processed_file_0](https://github.com/user-attachments/assets/ce12c0ae-b2a8-465b-bea8-395c94a60a5e)


```sh
def convert_to_gray_scale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresholding = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    return thresholding

thresholding = convert_to_gray_scale(img)
```

3) write processed_image 
```sh
cv2.imwrite(os.path.join(preprocessed_folder, processed_img_name), thresholding)
```

4) reading table from image and writing it to .xlsx file
   
   <img width="464" alt="Screenshot 2024-10-20 at 02 59 25" src="https://github.com/user-attachments/assets/e7f25100-5999-46b4-9ac0-bfb27802ef51">
as you can see it doesn't read properly (1st version of this script), need to test another models
```sh
preprocessed_img.to_xlsx(os.path.join(output_excel, excel_name),
                                 ocr=ocr,
                                 min_confidence=50)
```

## Using paddleOCR
image from our camera
![img](https://github.com/user-attachments/assets/5b41b256-68a5-42f0-bbb2-81dc98aec927)
processed image
![processed_file_7](https://github.com/user-attachments/assets/3c4c70a4-290c-4a44-a528-3a5f3eed761c)
table

<img width="515" alt="Screenshot 2024-10-20 at 19 49 10" src="https://github.com/user-attachments/assets/43c6562d-8580-4353-89b2-59da79b5e971">

as we can see paddleOCR has better perfomance

## Installation of packages

If you want to test by yourself, then you need to be sure that you have installed following packages:
```sh
brew install tesseract
pip install opencv-contrib-python
```

   [df1]: <https://github.com/xavctn/img2table>
