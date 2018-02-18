#! python3
# webl.py - Launches a site in the browser using an abbrivaited name from the
# command line or clipboard.
import pyperclip
import sys
import webbrowser

SiteData = {
    'fb': 'https://www.facebook.com',
    'g': 'https://www.google.com',
    'pin': 'https://in.pinterest.com/',
    'goodreads': 'https://www.goodreads.com/',
    'quora': 'https://www.quora.com/',
}
if len(sys.argv) > 1:
    # Get name of site from command line.
    SiteAbv = str(sys.argv[1])
    if SiteAbv in list(SiteData.keys()):
        webbrowser.open(SiteData.get(SiteAbv))
    elif pyperclip.paste():
        # Get address from clipboard.
        webbrowser.open(pyperclip.paste())
    else:
        print('Sorry nothing to search for')
