#! python3
# Add text or a website URL to images.
# Add a mostly transparent watermark to an image to prevent others from copying it.
import os
from PIL import Image, ImageDraw, ImageFont


def check_image_with_pil(path):
    try:
        Image.open(path)
    except:
        return False
    return True


# Declare the folder and the logo
text = 'Awesome'  # something that needs to be added to each image
FolderPath = 'C:\MyPythonScripts\Images'
os.chdir(FolderPath)

# Read Files and check whether they are image file
fileData = {file: check_image_with_pil(file) for file in os.listdir(FolderPath)}

for fileName in fileData.keys():
    if fileData[fileName] is False:
        continue

    # Get Dimensions of the Image File
    ImageObj = Image.open(fileName)
    width, height = ImageObj.size

    # Resize text relative to the Image
    img_fraction = 0.25
    fontsize = 1  # starting font size
    font = ImageFont.truetype("arial.ttf", fontsize)
    while font.getsize(text)[0] < img_fraction * ImageObj.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("arial.ttf", fontsize)
    # textW, textH = ImageDraw.Draw(ImageObj).textsize(text)
    textW, textH = font.getsize(text)

    # Append Text at a corner
    draw = ImageDraw.Draw(ImageObj)
    draw.text((width - textW-1, height - textH-1), text, fill='grey')

    # Save and Close file
    ImageObj.save(os.path.splitext(fileName)[0] + '_with_text_logo' + os.path.splitext(fileName)[1])
