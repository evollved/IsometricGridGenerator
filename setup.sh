#!/bin/bash

# Путь к виртуальному окружению
VENV_DIR="$HOME/python_venvs/IsometricGridGenerator"

# Создание виртуального окружения, если оно не существует
if [ ! -d "$VENV_DIR" ]; then
    echo "Создание виртуального окружения в $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Виртуальное окружение уже существует в $VENV_DIR."
fi

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source "$VENV_DIR/bin/activate"

# Установка зависимостей
echo "Установка зависимостей из requirements.txt..."
pip install -r requirements.txt

# Создание скрипта для быстрого запуска start.sh
echo "Создание скрипта для быстрого запуска start.sh..."
cat <<EOL > start.sh
#!/bin/bash
source "$VENV_DIR/bin/activate"
python generate_isometric_grid.py
EOL

# Делаем start.sh исполняемым
chmod +x start.sh

echo "Настройка завершена. Для запуска программы используйте команду: ./start.sh"