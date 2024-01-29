import qrcode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#the data we wish to make a qr code:
data = input("Enter the data you wish to convert to a QR code:")

#the make function will turn the data into a QR code
qr_img = qrcode.make(data)

#Ask user for file name
filename = (input("Please choose the file name you with to give your QR code: ") + ".png")

# Saving as an image file
qr_img.save(filename)

#display QR code

img = mpimg.imread(filename)
imgplot = plt.imshow(img)
plt.show()

