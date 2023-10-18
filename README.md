# PDF Converter

![python](https://img.shields.io/badge/python-3.10-blue.svg)


## pdf-unitter.exe
![build](https://github.com/mo-mo-666/pdf-converter/workflows/unitter-build/badge.svg)
![release](https://img.shields.io/github/v/release/mo-mo-666/pdf-converter?include_prereleases)

同じページ数のPDFを交互に結合するプログラム．
たとえば，

- 1.pdf: A1 A2 A3 A4 A5 ...
- 2.pdf: B1 B2 B3 B4 B5 ...

と並んでいるpdfを

A1 B1 A2 B2 A3 B3 ...

とできる．たとえば，2つのpdfを両面印刷したいときなどに便利．

### 必要な情報
結合したいpdfがあるフォルダと同じところにプログラムを置く．

- 一つ目のpdfのファイル名（またはファイルへのパス）
- 二つ目のpdfのファイル名（またはファイルへのパス）
- 出力ファイル名（またはファイルへのパス）

ファイル名を入力する際，".pdf"は省略してもよい．

### 注意点
PDFが同じページ数でないと動かない．
