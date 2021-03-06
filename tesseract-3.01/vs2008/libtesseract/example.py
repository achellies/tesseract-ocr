# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_example', [dirname(__file__)])
        except ImportError:
            import _example
            return _example
        if fp is not None:
            try:
                _mod = imp.load_module('_example', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _example = swig_import_helper()
    del swig_import_helper
else:
    import _example
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


MAX_NUM_INT_FEATURES = _example.MAX_NUM_INT_FEATURES
class TessBaseAPI(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TessBaseAPI, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TessBaseAPI, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _example.new_TessBaseAPI()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _example.delete_TessBaseAPI
    __del__ = lambda self : None;
    __swig_getmethods__["Version"] = lambda x: _example.TessBaseAPI_Version
    if _newclass:Version = staticmethod(_example.TessBaseAPI_Version)
    def SetInputName(self, *args): return _example.TessBaseAPI_SetInputName(self, *args)
    def SetOutputName(self, *args): return _example.TessBaseAPI_SetOutputName(self, *args)
    def SetVariable(self, *args): return _example.TessBaseAPI_SetVariable(self, *args)
    def GetIntVariable(self, *args): return _example.TessBaseAPI_GetIntVariable(self, *args)
    def GetBoolVariable(self, *args): return _example.TessBaseAPI_GetBoolVariable(self, *args)
    def GetDoubleVariable(self, *args): return _example.TessBaseAPI_GetDoubleVariable(self, *args)
    def GetStringVariable(self, *args): return _example.TessBaseAPI_GetStringVariable(self, *args)
    def PrintVariables(self, *args): return _example.TessBaseAPI_PrintVariables(self, *args)
    def GetVariableAsString(self, *args): return _example.TessBaseAPI_GetVariableAsString(self, *args)
    def Init(self, *args): return _example.TessBaseAPI_Init(self, *args)
    def InitLangMod(self, *args): return _example.TessBaseAPI_InitLangMod(self, *args)
    def InitForAnalysePage(self): return _example.TessBaseAPI_InitForAnalysePage(self)
    def ReadConfigFile(self, *args): return _example.TessBaseAPI_ReadConfigFile(self, *args)
    def SetPageSegMode(self, *args): return _example.TessBaseAPI_SetPageSegMode(self, *args)
    def GetPageSegMode(self): return _example.TessBaseAPI_GetPageSegMode(self)
    def TesseractRect(self, *args): return _example.TessBaseAPI_TesseractRect(self, *args)
    def ClearAdaptiveClassifier(self): return _example.TessBaseAPI_ClearAdaptiveClassifier(self)
    def SetImage(self, *args): return _example.TessBaseAPI_SetImage(self, *args)
    def SetRectangle(self, *args): return _example.TessBaseAPI_SetRectangle(self, *args)
    def SetThresholder(self, *args): return _example.TessBaseAPI_SetThresholder(self, *args)
    def GetThresholdedImage(self): return _example.TessBaseAPI_GetThresholdedImage(self)
    def GetRegions(self, *args): return _example.TessBaseAPI_GetRegions(self, *args)
    def GetTextlines(self, *args): return _example.TessBaseAPI_GetTextlines(self, *args)
    def GetWords(self, *args): return _example.TessBaseAPI_GetWords(self, *args)
    def GetConnectedComponents(self, *args): return _example.TessBaseAPI_GetConnectedComponents(self, *args)
    def GetComponentImages(self, *args): return _example.TessBaseAPI_GetComponentImages(self, *args)
    def DumpPGM(self, *args): return _example.TessBaseAPI_DumpPGM(self, *args)
    def AnalyseLayout(self): return _example.TessBaseAPI_AnalyseLayout(self)
    def Recognize(self, *args): return _example.TessBaseAPI_Recognize(self, *args)
    def RecognizeForChopTest(self, *args): return _example.TessBaseAPI_RecognizeForChopTest(self, *args)
    def ProcessPages(self, *args): return _example.TessBaseAPI_ProcessPages(self, *args)
    def ProcessPage(self, *args): return _example.TessBaseAPI_ProcessPage(self, *args)
    def GetIterator(self): return _example.TessBaseAPI_GetIterator(self)
    def GetUTF8Text(self): return _example.TessBaseAPI_GetUTF8Text(self)
    def GetHOCRText(self, *args): return _example.TessBaseAPI_GetHOCRText(self, *args)
    def GetBoxText(self, *args): return _example.TessBaseAPI_GetBoxText(self, *args)
    def GetUNLVText(self): return _example.TessBaseAPI_GetUNLVText(self)
    def MeanTextConf(self): return _example.TessBaseAPI_MeanTextConf(self)
    def AllWordConfidences(self): return _example.TessBaseAPI_AllWordConfidences(self)
    def AdaptToWordStr(self, *args): return _example.TessBaseAPI_AdaptToWordStr(self, *args)
    def Clear(self): return _example.TessBaseAPI_Clear(self)
    def End(self): return _example.TessBaseAPI_End(self)
    def IsValidWord(self, *args): return _example.TessBaseAPI_IsValidWord(self, *args)
    def GetTextDirection(self, *args): return _example.TessBaseAPI_GetTextDirection(self, *args)
    def SetDictFunc(self, *args): return _example.TessBaseAPI_SetDictFunc(self, *args)
    def SetProbabilityInContextFunc(self, *args): return _example.TessBaseAPI_SetProbabilityInContextFunc(self, *args)
    def DetectOS(self, *args): return _example.TessBaseAPI_DetectOS(self, *args)
    def GetFeaturesForBlob(self, *args): return _example.TessBaseAPI_GetFeaturesForBlob(self, *args)
    __swig_getmethods__["FindRowForBox"] = lambda x: _example.TessBaseAPI_FindRowForBox
    if _newclass:FindRowForBox = staticmethod(_example.TessBaseAPI_FindRowForBox)
    def RunAdaptiveClassifier(self, *args): return _example.TessBaseAPI_RunAdaptiveClassifier(self, *args)
    def GetUnichar(self, *args): return _example.TessBaseAPI_GetUnichar(self, *args)
    def GetDawg(self, *args): return _example.TessBaseAPI_GetDawg(self, *args)
    def NumDawgs(self): return _example.TessBaseAPI_NumDawgs(self)
    def GetLastInitLanguage(self): return _example.TessBaseAPI_GetLastInitLanguage(self)
    __swig_getmethods__["MakeTessOCRRow"] = lambda x: _example.TessBaseAPI_MakeTessOCRRow
    if _newclass:MakeTessOCRRow = staticmethod(_example.TessBaseAPI_MakeTessOCRRow)
    __swig_getmethods__["MakeTBLOB"] = lambda x: _example.TessBaseAPI_MakeTBLOB
    if _newclass:MakeTBLOB = staticmethod(_example.TessBaseAPI_MakeTBLOB)
    __swig_getmethods__["NormalizeTBLOB"] = lambda x: _example.TessBaseAPI_NormalizeTBLOB
    if _newclass:NormalizeTBLOB = staticmethod(_example.TessBaseAPI_NormalizeTBLOB)
    def tesseract(self): return _example.TessBaseAPI_tesseract(self)
    def InitTruthCallback(self, *args): return _example.TessBaseAPI_InitTruthCallback(self, *args)
    def GetCubeRecoContext(self): return _example.TessBaseAPI_GetCubeRecoContext(self)
    def set_min_orientation_margin(self, *args): return _example.TessBaseAPI_set_min_orientation_margin(self, *args)
    def GetBlockTextOrientations(self, *args): return _example.TessBaseAPI_GetBlockTextOrientations(self, *args)
    def FindLinesCreateBlockList(self): return _example.TessBaseAPI_FindLinesCreateBlockList(self)
    __swig_getmethods__["DeleteBlockList"] = lambda x: _example.TessBaseAPI_DeleteBlockList
    if _newclass:DeleteBlockList = staticmethod(_example.TessBaseAPI_DeleteBlockList)
TessBaseAPI_swigregister = _example.TessBaseAPI_swigregister
TessBaseAPI_swigregister(TessBaseAPI)

def TessBaseAPI_Version():
  return _example.TessBaseAPI_Version()
TessBaseAPI_Version = _example.TessBaseAPI_Version

def TessBaseAPI_FindRowForBox(*args):
  return _example.TessBaseAPI_FindRowForBox(*args)
TessBaseAPI_FindRowForBox = _example.TessBaseAPI_FindRowForBox

def TessBaseAPI_MakeTessOCRRow(*args):
  return _example.TessBaseAPI_MakeTessOCRRow(*args)
TessBaseAPI_MakeTessOCRRow = _example.TessBaseAPI_MakeTessOCRRow

def TessBaseAPI_MakeTBLOB(*args):
  return _example.TessBaseAPI_MakeTBLOB(*args)
TessBaseAPI_MakeTBLOB = _example.TessBaseAPI_MakeTBLOB

def TessBaseAPI_NormalizeTBLOB(*args):
  return _example.TessBaseAPI_NormalizeTBLOB(*args)
TessBaseAPI_NormalizeTBLOB = _example.TessBaseAPI_NormalizeTBLOB

def TessBaseAPI_DeleteBlockList(*args):
  return _example.TessBaseAPI_DeleteBlockList(*args)
TessBaseAPI_DeleteBlockList = _example.TessBaseAPI_DeleteBlockList

# This file is compatible with both classic and new-style classes.


