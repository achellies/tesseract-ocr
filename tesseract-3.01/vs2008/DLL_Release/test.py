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
mstr = ctypes.create_string_buffer('\000' * 3200)
api.ProcessPage(ctypes.pointer(pix.data), 0, None, None, 0, mstr)
