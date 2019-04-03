# Настройка проекта
 
- В корне проекта создаем необходимые директории:

```bash
mkdir var && cd var && mkdir static && mkdir maedia && python3 -m venv venv && cd ..
```

- Активируем виртуальное окружение:
```bash
. var/venv/bin/activate
```

- Устанавливаем зависимости:
```bash
pip install -Ur freeze.txt 
```

- Если возникает ошибка: failed with error code 1 in /tmp/pip-build-rcx2e_an/rcssmin/
```bash
pip install rcssmin --install-option="--without-c-extensions"
pip install rjsmin --install-option="--without-c-extensions"
pip install django-compressor --upgrade
```

- Создаем базу в postgresql

- Выполняем миграции
