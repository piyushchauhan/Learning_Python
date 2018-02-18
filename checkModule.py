import imp
nameOfModule='pywin32'
try:
    nameOfModule_info = imp.find_module(nameOfModule)
    nameOfModule = imp.load_module(nameOfModule, *nameOfModule_info)
    imp.find_module('eggs', nameOfModule.__path__) # __path__ is already a list
    found = True
except ImportError:
    found = False
print(found)