#! python3
"""
I have a bad habit of transferring files from my digital camera to temporary folders somewhere on the hard
drive and then forgetting about these folders. It would be nice to write a program that could scan the entire
hard drive and find these leftover “photo folders.”

Write a program that goes through every folder on your hard drive and finds potential photo folders. Of course,
first you’ll have to define what you consider a “photo folder” to be; let’s say that it’s any folder where more
than half of the files are photos. And how do you define what files are photos?

First, a photo file must have the file extension .png or .jpg. Also, photos are large images; a photo file’s width
and height must both be larger than 500 pixels. This is a safe bet, since most digital camera photos are several
thousand pixels in width and height.

As a hint, here’s a rough skeleton of what this program might look like:
"""
#! python3
#Import modules and write comments to describe this program.
import os

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if TODO:
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.

        # Check if width & height are larger than 500.
        if TODO:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if TODO:
        print(TODO)