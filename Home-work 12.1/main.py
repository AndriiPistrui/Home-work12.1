import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text_without_tags = re.sub(r'<[^>]*>', '', html)

    lines = text_without_tags.splitlines()

    cleaned_lines = [line for line in lines if line.strip()]


    with codecs.open(result_file, 'w', 'utf-8') as file:
        for line in cleaned_lines:
            file.write(line + '\n')

    print(f"Очищений текст записано у файл {result_file}")


delete_html_tags('draft.html')
