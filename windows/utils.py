import dearpygui.dearpygui as dpg
import os, sys
import subprocess

import main


def save_workspace():
    workspace_name = dpg.get_value("input_txt_workspace")
    dpg.save_init_file(f"Config/{workspace_name}.ini")


def load_workspace():
    workspace_name = dpg.get_value("input_txt_workspace")


def test_move():
    dpg.set_item_pos("util", [50, 50])


def restart_app():
    os.execv(sys.executable, ['python'] + sys.argv)


def util_window():
    with dpg.window(label="util", tag="util"):
        dpg.add_button(label="save workspace layout", callback=save_workspace)
        dpg.add_input_text(label="workspace name", tag='input_txt_workspace')
        dpg.add_text("I guess I can't just load workspace so easily, but I need to dev it...")
        dpg.add_button(label="load workspace", callback=load_workspace)
        dpg.add_button(label="Test move", callback=test_move)
        dpg.add_separator()
        dpg.add_button(label="Restart", width=400, height=100, callback=restart_app)
