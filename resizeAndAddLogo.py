#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.
import os
from PIL import Image
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        # skip non-image files and the logo file itself
        continue
    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

    # Resize the image.
    print('Resizing %s...' % (filename))
    im = im.resize((width, height))

    # Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))
# TODO:
'''Modify resizeAndAddLogo.py so that the image must be at least twice the 
width and height of the logo image before the logo is pasted. 
Other wise, it should skip adding the logo.'''
# TODO:
'''
The resizeAndAddLogo.py program works with PNG and JPEG files, 
but Pillow supports many more formats than just these two. Extend resizeAndAddLogo.py 
to process GIF and BMP images as well.
'''
# TODO:
'''
the program modifies PNG and JPEG files only if their file extensions are set in 
lowercase. For example, it will process zophie.png but not zophie.PNG. Change the 
code so that the file extension check is case insensitive.
'''