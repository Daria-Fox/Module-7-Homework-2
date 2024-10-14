def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as f:
        strings_positions = {}
        line_number = 1
        for string in strings:
            start_positions = f.tell()
            f.write(string + '\n')
            strings_positions[(line_number, start_positions)] = string
            line_number += 1
        return strings_positions


info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)
