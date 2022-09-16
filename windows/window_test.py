import dearpygui.dearpygui as dpg


def test_window1():
    with dpg.window(label="test1", tag="test1", no_resize=True):
        dpg.add_text("test1")
        dpg.add_text("test1")
        dpg.add_text("test1")
        dpg.add_text("test1")
        dpg.add_text("test1")
    # dpg.show_item_debug("test1")


def test_window2():
    with dpg.window(label="test2", tag="test2", no_resize=True):
        dpg.add_text("test2")
        dpg.add_text("test2")
        dpg.add_text("test2")
        dpg.add_text("test2")
        dpg.add_text("test2")


def test_window3():
    with dpg.window(label="test3", tag="test3", no_resize=True):
        dpg.add_text("test3")
        dpg.add_text("test3")
        dpg.add_text("test3")
        dpg.add_text("test3")
        dpg.add_text("test3")


def test_window4():
    with dpg.window(label="test4", tag="test4", no_resize=True):
        dpg.add_text("test4")
        dpg.add_text("test4")
        dpg.add_text("test4")
        dpg.add_text("test4")
        dpg.add_text("test4")
