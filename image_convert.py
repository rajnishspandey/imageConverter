import cv2
import img2pdf
import io
import os

#conversion of image to greyscale
def img_to_greyscale(filename, operation,img):
    imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    newFilename = f"static/converted/{operation+'_'+filename}"
    cv2.imwrite(newFilename, imgProcessed)
    return newFilename

#conversion of image to webp
def img_to_webp(filename,operation,img):
    base_filename, extension = os.path.splitext(filename)
    newFilename = f"static/converted/{operation+'_'+base_filename}.webp"
    cv2.imwrite(newFilename, img)
    return newFilename

#conversion of image to jpg
def img_to_jpg(filename,operation,img):
    base_filename, extension = os.path.splitext(filename)
    newFilename = f"static/converted/{operation+'_'+base_filename}.jpg"
    cv2.imwrite(newFilename, img)
    return newFilename


#conversion of image to png
def img_to_png(filename,operation,img):
    base_filename, extension = os.path.splitext(filename)
    newFilename = f"static/converted/{operation+'_'+base_filename}.png"
    cv2.imwrite(newFilename, img)
    return newFilename

# conversion of image to pdf
def img_to_pdf(filename,operation, img):
    base_filename, extension = os.path.splitext(filename)
    newFilename = f"static/converted/{operation+'_'+base_filename}.pdf"
    img_bytes = cv2.imencode('.png', img)[1].tobytes()
    with io.BytesIO(img_bytes) as img_stream:
        pdf_data = img2pdf.convert(img_stream)
        with open(newFilename, 'wb') as pdf_file:
            pdf_file.write(pdf_data) 
    return newFilename
