# ---- Link --------------------------- 
IMGaffine.so:  IMGaffine_c.o
	gcc -shared IMGaffine_c.o -o IMGaffine.so

# ---- gcc C compile ------------------
IMGaffine_c.o:  IMGaffine_c.c C_arraytest.h
	gcc  -c -fPIC IMGaffine_c.c -I/usr/include/python2.7 -I/usr/lib/python2.7/dist-packages/numpy/core/include/numpy
