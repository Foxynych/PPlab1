# Музыкальный редактор — пример слоистой архитектуры на Python

Минимальный консольный проект на Python 3.10+, без сторонних зависимостей.

## Запуск в PyCharm

1. Распакуйте архив.
2. В PyCharm выберите **File → Open** и папку `layered_music`.
3. Укажите Python 3.10 или новее как интерпретатор проекта.
4. Откройте `main.py` и нажмите **Run**.
5. Пользуйтесь меню; треки сохраняются в `tracks.json` рядом с `main.py`.

## Слои

```text
main.py                        Сборка зависимостей (composition root)
presentation/console.py        UI: input/print, меню и обработка ошибок
application/music_service.py   Бизнес-логика и проверки
domain/track.py                Сущность трека
domain/repository.py           Абстракция хранилища (контракт)
infrastructure/json_repository.py  Работа с JSON-файлом
tests/test_service.py          Unit-тесты сервиса с подменным репозиторием