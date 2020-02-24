from pathlib import Path

with open('referat.txt', 'r', encoding='utf-8') as f:
    line = f.read()
    print('Длина строки:', len(line), 'символов.')

print('Слов в тексте:', len(set(Path(r'referat.txt').read_text(encoding='utf-8').split())))

with open ('referat.txt', 'r', encoding='utf-8') as f:
    old_data = f.read()
    new_data = old_data.replace('.', '!')
with open ('referat2.txt', 'w', encoding='utf-8') as f:
    f.write(new_data)
print('В исходном файле "." заменили на "!" и записали результат в referat2.txt. ')
