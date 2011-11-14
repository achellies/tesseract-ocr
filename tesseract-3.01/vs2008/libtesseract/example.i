/* File : example.i */
%module example

%{
#include "../../api/baseapi.h"
%}

/* Let's just grab the original header file here */
%include "../../api/baseapi.h"
