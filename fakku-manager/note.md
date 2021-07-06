Fakku-manager.py aims to merge different images to one pdf.
usage:`python3 fakku-manager.py`

Feature:
1. Merge all png in _all.pdf alphabetically.
2. Store individual pdf in output folder.
3. Divide _all.pdf into separate documents at about 200 mb, so that Amazon Kindle can handle it without crashing.

In order to compress the pdf, use `python3 cpdf.py`.
By the way cpdf.py is forked from https://github.com/hkdb/cpdf.

Example:

Before:
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
└── fakku-manager.py
```
After:
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
├── fakku-manager.py
├── example_all.pdf
├── example_pt.1.pdf
├── fakku_manager.py
└── output
    ├── a1.pdf
    ├── a2.pdf
    └── a3.pdf
```

