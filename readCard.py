from package import *

def detectText(image):
    """Read text from image using tesseract"""
    img = cv2.imread(image)

    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)


    # kernel = np.ones((5,5),np.float32)/25
    # img = cv2.filter2D(img,-1,kernel)
    # laplacian = cv2.Laplacian(img,cv2.CV_64F)
    # img = cv2.cvtColor(laplacian,cv2.COLOR_BGR2GRAY)
    # gray = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    

    result = pt.image_to_string(img, lang="eng")
    print(result)
    print("******************************")
    print("Url output")
    url_list=linkedinUrl.get_link(result.replace(" ",""))


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--image", help= "path to image")
    args = a.parse_args()
    detectText(args.image)