import matplotlib.pyplot as plt
import numpy as np

def draw_isometric_grid(ax, spacing, color='lightgray', orientation=2):
    # Размеры листа A4 в миллиметрах
    if orientation == 2:  # Книжная ориентация
        width, height = 210, 297
    else:  # Альбомная ориентация
        width, height = 297, 210

    # Рассчитываем количество ячеек по ширине и высоте
    cols = int(width / (spacing * 0.5)) + 2  # Количество ячеек по ширине
    rows = int(height / (spacing * 0.5)) + 2  # Количество ячеек по высоте

    # Смещение для центрирования сетки
    offset_x = width / 2
    offset_y = height / 2

    # Рисуем сетку
    for x in range(-cols, cols):
        for y in range(-rows, rows):
            # Координаты для изометрической проекции
            x_iso = (x - y) * spacing / 2 + offset_x
            y_iso = (x + y) * spacing / 4 + offset_y

            # Рисуем квадраты
            square = np.array([
                [x_iso, y_iso],
                [x_iso + spacing / 2, y_iso + spacing / 4],
                [x_iso + spacing, y_iso],
                [x_iso + spacing / 2, y_iso - spacing / 4],
                [x_iso, y_iso]
            ])
            ax.plot(square[:, 0], square[:, 1], color=color, linestyle='dotted', linewidth=0.5)

def draw_axes(ax, spacing, orientation=2):
    # Размеры листа A4 в миллиметрах
    if orientation == 2:  # Книжная ориентация
        width, height = 210, 297
    else:  # Альбомная ориентация
        width, height = 297, 210

    # Начальная точка для осей (левый нижний угол)
    start_x, start_y = 10, 10  # Отступ от края

    # Длина осей (2 см)
    axis_length = 20

    # Ось X (горизонтальная)
    end_x_x = start_x + axis_length
    end_y_x = start_y
    ax.plot([start_x, end_x_x], [start_y, end_y_x], color='red', linewidth=1, linestyle='solid')
    ax.text(end_x_x + 5, end_y_x, 'X', color='red', fontsize=10)

    # Ось Y (вертикальная)
    end_x_y = start_x
    end_y_y = start_y + axis_length
    ax.plot([start_x, end_x_y], [start_y, end_y_y], color='green', linewidth=1, linestyle='solid')
    ax.text(end_x_y, end_y_y + 5, 'Y', color='green', fontsize=10)

    # Ось Z (диагональная, совпадает с направлением сетки)
    angle = np.arctan2(spacing / 4, spacing / 2)  # Угол наклона граней ромбов
    end_x_z = start_x + axis_length * np.cos(angle)
    end_y_z = start_y + axis_length * np.sin(angle)
    ax.plot([start_x, end_x_z], [start_y, end_y_z], color='blue', linewidth=1, linestyle='solid')
    ax.text(end_x_z + 5, end_y_z, 'Z', color='blue', fontsize=10)

def main():
    # Запрашиваем у пользователя размер ячейки в мм
    spacing = input("Введите размер ячейки в мм (например, 10, 20, 30): ")
    
    # Проверяем ввод пользователя
    try:
        spacing = float(spacing)  # Преобразуем ввод в число с плавающей запятой
        if spacing <= 0:
            raise ValueError("Размер должен быть положительным числом.")
    except ValueError as e:
        print(f"Неверный ввод: {e}")
        return

    # Запрашиваем у пользователя ориентацию страницы
    orientation = input("Введите ориентацию страницы (1 — альбомная, 2 — книжная): ").strip()
    if orientation not in ['1', '2']:
        print("Ориентация должна быть 1 (альбомная) или 2 (книжная).")
        return
    orientation = int(orientation)  # Преобразуем в число

    # Определяем размеры фигуры в дюймах (1 дюйм = 25.4 мм)
    if orientation == 2:  # Книжная ориентация
        figsize = (8.27, 11.69)  # Книжная ориентация (210x297 мм в дюймах)
    else:  # Альбомная ориентация
        figsize = (11.69, 8.27)  # Альбомная ориентация (297x210 мм в дюймах)

    # Создаем фигуру и оси
    fig, ax = plt.subplots(figsize=figsize)
    
    # Устанавливаем границы осей в соответствии с размерами листа A4
    if orientation == 2:  # Книжная ориентация
        ax.set_xlim(0, 210)  # Ширина A4 в мм
        ax.set_ylim(0, 297)  # Высота A4 в мм
    else:  # Альбомная ориентация
        ax.set_xlim(0, 297)  # Ширина A4 в мм
        ax.set_ylim(0, 210)  # Высота A4 в мм

    ax.set_aspect('equal')

    # Отключаем оси
    ax.axis('off')

    # Рисуем сетку для выбранного размера
    draw_isometric_grid(ax, spacing=spacing, color='lightgray', orientation=orientation)

    # Рисуем оси X, Y, Z
    draw_axes(ax, spacing=spacing, orientation=orientation)

    # Сохраняем изображение
    plt.savefig(f'isometric_grid_a4_{spacing}mm_{"альбомная" if orientation == 1 else "книжная"}.png', dpi=300, bbox_inches='tight')
    plt.close(fig)  # Закрываем фигуру, чтобы не показывать результат

    print(f"Изометрическая сетка сохранена в файл isometric_grid_a4_{spacing}mm_{'альбомная' if orientation == 1 else 'книжная'}.png")

if __name__ == "__main__":
    main()