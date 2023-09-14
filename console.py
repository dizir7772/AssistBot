import shutil
import sys
import os



def hide_cursor():
    """ Ховає текстовий курсор """
    print("\033[?25l", end="", flush=True)


def show_cursor():
    """ ВІдновлює текстовий курсор """
    print("\033[?25h", end="", flush=True)


def clear_console():
    """ Очищає консоль """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_console_size():
    """ Повертає поточні розміри консолі """
    columns, rows = shutil.get_terminal_size()
    return rows, columns


def move_cursor(row, col):
    """ Переміщає курсор на вказане місце """
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()


def gap(width_line, width_sub):
    """ Вираховує відступ для відображення по центру """
    return (width_line - width_sub) // 2
