import dearpygui.dearpygui as dpg


def save_workspace():
    workspace_name = dpg.get_value("input_txt_workspace")
    dpg.save_init_file(f"Config/{workspace_name}.ini")


def load_workspace():
    workspace_name = dpg.get_value("input_txt_workspace")


def test_move():
    dpg.set_item_pos("util", [50, 50])


def util_window():
    with dpg.window(label="util", tag="util"):
        dpg.add_button(label="save workspace layout", callback=save_workspace)
        dpg.add_input_text(label="workspace name", tag='input_txt_workspace')
        dpg.add_text("I guess I can't just load workspace so easily, but I need to dev it...")
        dpg.add_button(label="load workspace", callback=load_workspace)
        dpg.add_button(label="Test move", callback=test_move)


def test_window1():
    with dpg.window(label="test1", tag="test1", no_resize=True, no_background=True):
        dpg.add_text("test1")
        dpg.add_text("test1")
        dpg.add_text("test1")
        dpg.add_text("test1")
        dpg.add_text("test1")


def test_window2():
    with dpg.window(label="test2", tag="test2", no_resize=True, no_move=True):
        dpg.add_text("test2")
        dpg.add_text("test2")
        dpg.add_text("test2")
        dpg.add_text("test2")
        dpg.add_text("test2")


def test_window3():
    with dpg.window(label="test3", tag="test3", no_resize=True, no_move=True):
        dpg.add_text("test3")
        dpg.add_text("test3")
        dpg.add_text("test3")
        dpg.add_text("test3")
        dpg.add_text("test3")


def test_window4():
    with dpg.window(label="test4", tag="test4", no_resize=True, no_move=True):
        dpg.add_text("test4")
        dpg.add_text("test4")
        dpg.add_text("test4")
        dpg.add_text("test4")
        dpg.add_text("test4")
