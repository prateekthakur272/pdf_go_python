from pypdf import PdfReader, PdfMerger


class PdfGo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = PdfReader(file_path)

    def content(self):
        pages = self.reader.pages
        pages = list(map(lambda page: page.extract_text(),pages))
        return pages

    def merge(self, other, output_path):
        merger = PdfMerger()
        merger.append(self.file_path)
        merger.append(other.file_path)
        merger.write(output_path)
        merger.close()
        return PdfGo(output_path)

    def __len__(self):
        return len(self.reader.pages)


if __name__ == '__main__':
    print('Welcome to PDF-Go')
    path = input('Enter pdf path: ')
    try:
        pdf = PdfGo(path)
        choice = input('1. read content\n2. merge another pdf\n3. Quit\n')
        match choice:
            case '1':
                for page in pdf.content():
                    print(page)
            case '2':
                path_other = input('Enter path to another pdf: ')
                try:
                    pdf_other = PdfGo(path_other)
                    path_output = input('Enter output path: ')
                    pdf.merge(pdf_other, path_output)
                except FileNotFoundError as e:
                    print(f'file \'{path_other}\' does not exist')
                except IsADirectoryError as e:
                    print(f'\'{path_other}\' is a directory')
            case _:
                print('Exit')
    except FileNotFoundError as e:
        print(f'file \'{path}\' does not exist')
    except IsADirectoryError as e:
        print(f'\'{path}\' is a directory')
