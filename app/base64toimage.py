import base64 
import numpy as np
import io
from PIL import Image
import cv2 as cv
# from base64 import decodestring

imagestr = "data:image/jpeg;base64,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"



# image = Image.fromstring('RGB',("500","500"),decodestring(imagestr))
# image.save("foo.png")





# Take in base64 string and return cv image

# def save(encoded_data, filename):
#     nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
#     img = cv.imdecode(nparr, cv.IMREAD_ANYCOLOR)
#     return cv.imwrite(filename, img)
# # save(imagestr, 'testfile.png')


imagestr = imagestr.replace('data:image/png;base64,', '')
# img_ascii = imagestr.encode('ascii')
# img_bytes = base64.b64decode(img_ascii)
# decoded = img_bytes.decode('ascii')
# print(decoded)

# with open("media/images/imageToSave.png", "rb") as fh:
#     fh.write(base64.decodebytes(imagestr))
img_bytes = bytes(imagestr, 'utf-8')
print(img_bytes)
b = base64.decodebytes(img_bytes)
print(b)
data = img_bytes.decode('utf-8')
print(type(data))

# imgdata = base64.b64decode(imagestr)
# imgdata = base64.decodebytes(imgdata)
filename = 'media/images/some_image.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(b)