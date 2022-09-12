import dearpygui.dearpygui as dpg
from windows import annotation


def create_menu():
    with dpg.viewport_menu_bar():
        with dpg.menu(label="Project"):
            dpg.add_menu_item(label="New Project")
            dpg.add_menu_item(label="Open")
            dpg.add_separator()
            dpg.add_menu_item(label="Exit")
        with dpg.menu(label="Setting"):
            dpg.add_menu_item(label="test")
            dpg.add_menu_item(label="test")
            dpg.add_menu_item(label="test")
        with dpg.menu(label="Window"):
            dpg.add_menu_item(label="window1", check=True)
            dpg.add_menu_item(label="window2", check=True)
            dpg.add_menu_item(label="window3", check=True)
            dpg.add_menu_item(label="window4", check=True)
        dpg.add_menu_item(label="          ")
        dpg.add_menu_item(label="workspace 1")
        dpg.add_menu_item(label="workspace 2")
        dpg.add_menu_item(label="+")


def create_test_windows():
    annotation.util_window()
    annotation.test_window1()
    annotation.test_window2()
    annotation.test_window3()
    annotation.test_window4()

    # then add lots of windows?


