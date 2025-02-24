Изометрическая сетка на листе А4

Этот проект позволяет генерировать изометрическую сетку на листе формата А4 с возможностью выбора размера ячейки и ориентации страницы (альбомная или книжная). Сетка сохраняется в формате PNG и может быть использована для печати или дальнейшей обработки.
Особенности

    Генерация изометрической сетки с заданным размером ячейки.

    Поддержка двух ориентаций страницы: альбомная и книжная.

    Оси X, Y и Z, обозначенные в левом нижнем углу, совпадают с гранями ромбов сетки.

    Сохранение результата в формате PNG с высоким качеством.

Требования

Для работы проекта необходимы следующие библиотеки:

    matplotlib>=3.5.0

    numpy>=1.21.0

Установите зависимости с помощью команды:
bash
Copy

pip install -r requirements.txt

Использование

    Клонируйте репозиторий:
    bash
    Copy

    git clone https://github.com/ваш-username/изометрическая-сетка.git
    cd изометрическая-сетка

    Запустите скрипт:
    bash
    Copy

    python generate_isometric_grid.py

    Следуйте инструкциям на экране:

        Введите размер ячейки в миллиметрах (например, 10, 20, 30).

        Выберите ориентацию страницы:

            1 — Альбомная ориентация.

            2 — Книжная ориентация.

    Результат будет сохранен в файл с именем isometric_grid_a4_<размер>mm_<ориентация>.png.

Примеры
Книжная ориентация (размер ячейки 10 мм)

![image](https://github.com/user-attachments/assets/3e3c8b3c-dc71-4c50-a5ce-0eb02b54f8b2)


Альбомная ориентация (размер ячейки 20 мм)

![image](https://github.com/user-attachments/assets/259e08a5-9fdc-4ff9-a435-7e33088f17a0)


Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.
