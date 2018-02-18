"""
Write a program that scans through your email account, finds all
the unsubscribe links in all your emails, and automatically opens
them in a browser. This program will have to log in to your email
provider’s IMAP server and download all of your emails. You can use
BeautifulSoup (covered in Chapter 11) to check for any instance
where the word unsubscribe occurs within an HTML link tag.

Once you have a list of these URLs, you can use webbrowser.open()
to automatically open all of these links in a browser.

You’ll still have to manually go through and complete any additional
steps to unsubscribe yourself from these lists. In most cases,
this involves clicking a link to confirm.

But this script saves you from having to go through all of your
emails looking for unsubscribe links. You can then pass this script
along to your friends so they can run it on their email accounts.
(Just make sure your email password isn’t hardcoded in the source code!)
"""