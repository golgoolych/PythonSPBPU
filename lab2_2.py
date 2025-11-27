

class MyFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.content = None
        self._check()
    def _check(self):
        modes = ['read', 'write', 'append', 'url']
        if self.mode not in modes:
            raise ValueError(f"Недопустимый режим. Допустимые режимы: {', '.join(modes)}")
    def read(self):
        if self.mode != 'read':
            raise PermissionError("Режим чтения файла не активирован.")
        try:
            with open(self.name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.name} не найден.")
        except Exception as e:
            raise Exception(f"Ошибка при чтении файла: {str(e)}")
q = MyFile('a_and_p.txt', 'write')
text = q.read()
print(text)