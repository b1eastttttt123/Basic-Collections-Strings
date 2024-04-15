word = input('Название файла: ')

if set(word) & set('@№$%^&*()'):
  print('Ошибка: название начинается недопустимым символом.')
elif word.endswith('.txt') or word.endswith('.docx'):
  print('Файл назван верно.')
else:
  print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
