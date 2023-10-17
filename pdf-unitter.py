from pypdf import PdfReader, PdfWriter
import datetime
import time
import os
from typing import Tuple


def pdf_cross_unitter(pdf1_path: str, pdf2_path: str, output_path: str) -> bool:
    reader1 = PdfReader(pdf1_path)
    reader2 = PdfReader(pdf2_path)
    if len(reader1.pages) != len(reader2.pages):
        print('ページ数が異なります。ページ数が等しいpdfしか結合できません')
        return False

    # １ページずつ交互に新しいファイルに書き込む
    writer = PdfWriter()
    for r1, r2 in zip(reader1.pages, reader2.pages):
        writer.add_page(r1)
        writer.add_page(r2)
    with open(output_path, 'wb') as f:
        writer.write(f)
    return True


def read_args() -> Tuple[str, str, str]:
    NOW = datetime.datetime.now()
    NOW = f"{NOW.year}{NOW.month:02}{NOW.day:02}{NOW.hour:02}{NOW.minute:02}{NOW.second:02}"

    while True:
        pdf1_path = input(
             f"一つ目のpdfのパスを指定してください\n:"
        )
        if pdf1_path:
            ext1 = os.path.splitext(pdf1_path)[1]
            if ext1 != ".pdf":
                pdf1_path = f"{pdf1_path}.pdf"
            if os.path.exists(pdf1_path):
                break
            print(f"{pdf1_path}が存在しません。正しいパスを指定してください。")
    while True:
        pdf2_path = input(
             f"二つ目のpdfのパスを指定してください\n:"
        )
        if pdf2_path:
            ext2 = os.path.splitext(pdf2_path)[1]
            if ext2 != ".pdf":
                pdf2_path = f"{pdf2_path}.pdf"
            if os.path.exists(pdf2_path):
                break
            print(f"{pdf2_path}が存在しません。正しいパスを指定してください。")

    output_path_d = f"{NOW}.pdf"
    while True:
        output_path = input(
            f"出力ファイル名を指定してください。単にエンターを押した場合，{output_path_d}になります\n:"
        )
        if output_path:
            ext_out = os.path.splitext(output_path)[1]
            if ext_out != ".pdf":
                output_path = f"{output_path}.pdf"
            if os.path.exists(output_path):
                yn = input("既に存在するパスを指定しています。データは上書きされますが、よろしいですか？(y/n):")
                if yn != "y":
                    continue
        else:
            output_path = output_path_d
        break

    return pdf1_path, pdf2_path, output_path

def main():
    pdf1_path, pdf2_path, output_path = read_args()
    start = time.time()
    process = pdf_cross_unitter(pdf1_path, pdf2_path, output_path)
    end = time.time()  # end time
    exetime = end - start
    if process:
        print(f"正常に処理が終了しました．時間: {exetime} s")
    time.sleep(3)


if __name__ == "__main__":
    main()
