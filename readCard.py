"""This script reads a Business Card and returns the text detected"""
from package import *

def detectText(image):
    """Read text from image using tesseract"""

    img = image
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    config = ('-l eng --oem 1 --psm 3')
    result = pt.image_to_string(img) #, lang="eng")
    #print result
    print "******************************"
    #print "Url output"
    url_list = linkedinUrl.get_link(result.replace(" ", ""))
    return result, url_list

# if __name__ == "__main__":
#     a = argparse.ArgumentParser()
#     a.add_argument("--image", help= "path to image")
#     args = a.parse_args()
#     detectText(args.image)
