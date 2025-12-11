import requests
class MyFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self._check()
    def _check(self):
        modes = ['read', 'write', 'append', 'url']
        if self.mode not in modes:
            raise ValueError(f"Недопустимый режим. Допустимые режимы: {modes}")
    def read(self):
        if self.mode != 'read':
            raise PermissionError("Режим чтения файла не активирован.")
        try:
            with open(self.name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.name} не найден")
        except Exception as e:
            raise Exception(f"Ошибка: {str(e)}")
    def write(self, text):
        if self.mode not in ['write', 'append']:
            raise PermissionError("Режим записи в файл не активирован.")
        try:
            mode = 'w' if self.mode == 'write' else 'a'
            with open(self.name, mode, encoding='utf-8') as file:
                file.write(text)
        except Exception as e:
            raise Exception(f"Ошибка: {str(e)}")
    def read_url(self):
        if self.mode != 'url':
            raise PermissionError("Режим работы с URL не активирован.")
        try:
            with requests.get(self.name, timeout=10) as response:
                response.raise_for_status()
                return response.text
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Ошибка при загрузке URL: {str(e)}")
    def count_urls(self):
        if self.mode != 'url':
            raise PermissionError("Режим работы с URL не активирован.")
        file_content = self.read_url()
        count = 0
        count += file_content.count('href="')
        count += file_content.count("href='")
        count += file_content.count('src="')
        count += file_content.count("src='")
        return count
    def write_urls(self, file):
        if self.mode != 'url':
            raise PermissionError("Режим работы с URL не активирован.")
        try:
            content = self.read_url()
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            raise Exception(f"Ошибка: {str(e)}")

            
