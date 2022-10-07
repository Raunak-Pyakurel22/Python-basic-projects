# this library will help us to create qr codes
import pyqrcode

# first store the information you need in qr code in a variable
data_in_qr = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# then create another variable which will store the qr code
final_qr = pyqrcode.create(data_in_qr)

# this will export the qr code in png format in the current directory of the python file
final_qr.svg("first_qr.png", scale=8)
