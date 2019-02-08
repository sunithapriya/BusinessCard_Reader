# Businnescard_Reader

A library to read business card images and provide a google search.

**requirements.txt**:
You can find the all the necessary library to install
```
pip3 install -r requirements.txt 

```

**readCard.py**:
Python code to read text in an image using tesseract

**linkedinUrl.py**
A Simple python script to fetech the linkedUrl depend upon the readCard.py file.

**text_detection.py**
This script depend upon EAST algorithm. You can find orginal source code in [pyimagesearch](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/)
To run
```
python3 text_detection.py --image  images/card2.png  --east model/frozen_east_text_detection.pb 

```