# Businnescard_Reader

A library to read business card images and provide a google search.

**requirements.txt**:
Necessary libraries
```
pip3 install -r requirements.txt 

```

**readCard.py**:
Python code to read text in an image using tesseract

**linkedinUrl.py**
A Simple python script to fetch linkedUrl, called from readCard.py file.

**text_detection.py**
This script uses EAST algorithm. Orginal source code -  [pyimagesearch](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/) <br>
To run:
```
python3 text_detection.py --image  images/card2.png  --east model/frozen_east_text_detection.pb 

```
