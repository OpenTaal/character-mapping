./preprocess.py
SRC=character-mapping
dot -Tpng $SRC.gv -o$SRC.png
dot -Tsvg $SRC.gv -o$SRC.svg
