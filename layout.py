import os
import sys

import dearpygui.dearpygui as dpg

import globals
from windows import utils, window_test


def load_workspace(sender, app_data, user_data):
    globals.EditorInit['active_workspace'] = user_data
    globals.save_editor_init()
    os.execv(sys.executable, ['python'] + sys.argv)




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
        dpg.add_spacer(width=200)
        dpg.add_menu_item(label="Annotate", callback=load_workspace, user_data="Annotate")
        dpg.add_menu_item(label="Train", callback=load_workspace, user_data="Train")
        dpg.add_menu_item(label="Predict", callback=load_workspace, user_data="Predict")
        dpg.add_menu_item(label="+")


def create_test_windows():
    dpg.show_debug()
    utils.util_window()
    window_test.test_window1()
    window_test.test_window2()
    window_test.test_window3()
    window_test.test_window4()
    # test_window

    # then add lots of windows?


