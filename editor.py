# write your code here
available_formatters = ['plain', 'bold', 'italic', 'header', 'link',
                        'inline-code', 'ordered-list', 'unordered-list', 'new-line']

result_string = ''


def formatter_header(level, text):
    out = '#' * level
    return f'{out} {text}\n'


def formatter_plain(text):
    return text


def formatter_new_line():
    return '\n'


def formatter_link(label, url):
    return '[{}]({})'.format(label, url)


def formatter_bold(text):
    return '**{}**'.format(text)


def formatter_italic(text):
    return '*{}*'.format(text)


def formatter_inline(text):
    return '`{}`'.format(text)


def read_number_of_rows():
    while True:
        rows = int(input('Number of rows: '))
        if rows > 0:
            return rows
        else:
            print('The number of rows should be greater than zero')


def read_rows(n):
    res_str = []
    for i in range(1, n + 1):
        res_str.append(input('Row #' + str(i) + ': '))
    return res_str


def save_and_exit(string):
    f = open('output.md', 'w', encoding='utf-8')
    f.write(string)
    f.close()
    exit()


def process_format(formatter, prv):
    if formatter == 'header':
        # level = int(input('Level: '))

        while True:
            level = int(input('Level: '))

            if level > 6 or level < 1:
                print('The level should be within the range of 1 to 6')
                continue
            else:
                return formatter_header(level, input('Text: '))

            break

    elif formatter == 'plain':
        return formatter_plain(input('Text: '))
    elif formatter == 'new-line':
        return formatter_new_line()
    elif formatter == 'link':
        return formatter_link(input('Label: '), input('URL: '))
    elif formatter == 'bold':
        return formatter_bold(input('Text: '))
    elif formatter == 'italic':
        return formatter_italic(input('Text: '))
    elif formatter == 'inline-code':
        return formatter_inline(input('Text: '))
    elif formatter == 'ordered-list':
        number_of_rows = read_number_of_rows()
        res = read_rows(number_of_rows)
        # formatted = list(map(lambda x, y: str(x) + '. ' + y, enumerate(res)))
        formatted = [str(i + 1) + '. ' + s for i, s in enumerate(res)]
        formatted_str = '\n'.join(formatted)
        if prv and prv[-1] != '\n':
            formatted_str = '\n' + formatted_str
        return formatted_str + '\n'
    elif formatter == 'unordered-list':
        number_of_rows = read_number_of_rows()
        res = read_rows(number_of_rows)
        formatted = list(map(lambda x: '* ' + x, res))
        formatted_str = '\n'.join(formatted)
        if prv and prv[-1] != '\n':
            formatted_str = '\n' + formatted_str
        return formatted_str + '\n'


while True:
    income = input('Choose a formatter: ')
    if income == '!help':
        print('Available formatters: ' + ' '.join(available_formatters))
        print('Special commands: !help !done')
    elif income == '!done':
        save_and_exit(result_string)
    elif income in available_formatters:
        result_string += process_format(income, result_string)
        print(result_string)
    else:
        print('Unknown formatting type or command')