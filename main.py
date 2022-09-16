import dearpygui.dearpygui as dpg
from dearpygui import demo
from dearpygui_ext import themes
import os
import yaml

import colors
import layout
import globals
import styles


def init_editor():
    # font setup...
    # register static images...
    if not os.path.isdir('Config'):
        os.mkdir('Config')
    if os.path.isfile('Config/Editor.ini'):
        with open('Config/Editor.ini', 'r') as f:
            globals.EditorInit = yaml.load(f.read(), yaml.FullLoader)
    else:
        globals.EditorInit['theme'] = 'light'
        globals.EditorInit['app_size'] = 'FHD'
        globals.EditorInit['global_font_scale'] = 1.0
        globals.EditorInit['project_path'] = ''
        with open('Config/Editor.ini', 'w') as f:
            yaml.dump(globals.EditorInit, f, default_flow_style=False)
    dpg.configure_app(docking=True, docking_space=True, load_init_file=f"Config/{globals.EditorInit['active_workspace']}.ini")
    # if 'active_workspace' in globals.EditorInit:
    #     dpg.configure_app(init_file=f"Config/{globals.EditorInit['active_workspace']}.ini")
    # if globals.EditorInit['theme'] == 'light':
    #     dpg.bind_theme(themes.create_theme_imgui_light())


def global_tick():
    pass
    # print('tick not working??')
    # global TickImpl
    # exec(dpg.get_value("tick_impl"))


def pend_to_stop(n):
    globals.TimeToKill = globals.FrameCount + n
    print(globals.TimeToKill, globals.FrameCount)


def loop():
    frame_count = globals.FrameCount
    # create layout at frame 1 can make center things work
    # however, this will make loading init file fail
    if frame_count == 0:
        dpg.bind_theme(styles.create_theme(globals.EditorInit['theme']))
    if frame_count == 1:
        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, colors.GRAY300, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, colors.GRAY200, category=dpg.mvThemeCat_Core)
            with dpg.theme_component(dpg.mvInputInt):
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, colors.GRAY300, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, colors.GRAY200, category=dpg.mvThemeCat_Core)
        dpg.bind_item_theme("test1", global_theme)
        dpg.bind_item_theme("test2", global_theme)
        dpg.bind_item_theme("test3", global_theme)

        # dpg.set_primary_window("BG", True)
    if frame_count > 1:
        global_tick()
    if frame_count == globals.TimeToKill:
        dpg.stop_dearpygui()
    globals.FrameCount = frame_count + 1


if __name__ == '__main__':
    dpg.create_context()
    init_editor()
    with dpg.window(label="BG", tag="BG"):
        dpg.add_text('   ')
    layout.create_menu()
    layout.create_test_windows()
    dpg.show_style_editor()
    # dpg.show_tool(dpg.mvTool_Debug)
    # dpg.show_imgui_demo()
    # demo.show_demo()

    dpg.create_viewport(title='IFCS', width=1920, height=1080, resizable=False, x_pos=0, y_pos=0)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.start_dearpygui()
    while dpg.is_dearpygui_running():
        loop()
        dpg.render_dearpygui_frame()
    dpg.destroy_context()
    globals.save_editor_init()
