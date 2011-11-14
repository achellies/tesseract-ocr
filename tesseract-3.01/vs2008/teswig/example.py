import leptonica
from leptonica import *
import tesseract
import Image
import ctypes
api = tesseract.TessBaseAPI()
api.SetOutputName("outputName");
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)

im = Image.open("eurotext.tif")
pix = PILImageToPix(im)

api.ProcessPagesWrapper("eurotext.tif")
api.ProcessPagesBuffer(pix._address_.value)
