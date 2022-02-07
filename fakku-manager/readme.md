This script is capable to merge different images to one pdf and compress the files if necessary.
usage:`python3 main.py`

 ## Feature:
1. Merge all png in one pdf alphabetically.
2. Compress the files at about half the size of original files.
3. Screen the books you don't want.

 ## Example:

 ### Before:
```
.
├── a1
│   ├── 01.png
│   ├── 02.png
│   └── 03.png
├── a2
│   ├── 01.png
│   └── 02.png
├── a3
│   ├── 01.png
│   ├── 02.png
│   └── 03.png
└── main.py
```
 ### After:
```
.
├── a1
│   ├── 01.png
│   ├── 02.png
│   └── 03.png
├── a2
│   ├── 01.png
│   └── 02.png
├── a3
│   ├── 01.png
│   ├── 02.png
│   └── 03.png
├── main.py
└── output
    ├── a1.pdf
    ├── a2.pdf
    └── a3.pdf
```

 ## Update log:
 ### v1: 
 - Realizing fundamental features.

 ### v1.2:
 - Merge three .py into one.
 - Add compression tool.
