from package import *

def detectText(image):
	"""Read text from image using tesseract"""
	img = cv2.imread(image)

	kernel = np.ones((5,5),np.float32)/25
	img = cv2.filter2D(img,-1,kernel)
	laplacian = cv2.Laplacian(img,cv2.CV_64F)
	

	

	# img = cv2.cvtColor(laplacian,cv2.COLOR_BGR2GRAY)
	# gray = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	
	cv2.imshow('image',laplacian)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	

	result = pt.image_to_string(laplacian, lang="eng")
	print(result)
	# url_list=linkedinUrl.get_link(result)


if __name__ == "__main__":
	a = argparse.ArgumentParser()
	a.add_argument("--image", help= "path to image")
	args = a.parse_args()
	detectText(args.image)