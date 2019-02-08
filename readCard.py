import argparse
import cv2
import pytesseract as pt
import linkedinUrl

def detectText(image):
	"""Read text from image using tesseract"""
	img = cv2.imread(image)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	# cv2.imshow("image",gray)
	# cv2.waitKey(0)
	result = pt.image_to_string(gray, lang="eng")
	print(result)
	url_list=linkedinUrl.get_link(result)


if __name__ == "__main__":
	a = argparse.ArgumentParser()
	a.add_argument("--image", help= "path to image")
	args = a.parse_args()
	detectText(args.image)