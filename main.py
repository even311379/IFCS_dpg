import dearpygui.dearpygui as dpg
import os
import yaml
import layout

FrameCount = 0
EditorInit = {}


def init_editor():
    global EditorInit
    # font setup...
    # register static images...
    if not os.path.isdir('Config'):
        os.mkdir('Config')
    if os.path.isfile('Config/Editor.ini'):
        with open('Config/Editor.ini', 'r') as f:
            EditorInit = yaml.load(f.read(), yaml.FullLoader)
    else:
        EditorInit['theme'] = 'grey'
        EditorInit['app_size'] = 'FHD'
        EditorInit['global_font_scale'] = 1.0
        EditorInit['project_path'] = ''
        with open('Config/Editor.ini', 'w') as f:
            yaml.dump(EditorInit, f, default_flow_style=False)


def post_init_editor():
    layout.create_menu()
    layout.create_test_windows()


def global_tick():
    pass
    # global TickImpl
    # exec(dpg.get_value("tick_impl"))


def loop():
    global FrameCount
    if FrameCount == 0:
        init_editor()
    # if FrameCount == 1:
    #     post_init_editor()
    if FrameCount > 1 and FrameCount % 10 == 0:
        global_tick()
    FrameCount += 1


if __name__ == '__main__':
    dpg.create_context()
    dpg.create_viewport(title='IFCS', width=1920, height=1080, resizable=False, x_pos=1920, y_pos=0)
    dpg.configure_app(docking=True, docking_space=True)
    dpg.configure_app(load_init_file="Config/test.ini")
    # layout.create_menu()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    init_editor()
    post_init_editor()
    # dpg.start_dearpygui()
    if not dpg.is_viewport_ok():
        raise RuntimeError("Viewport not ready")
    while dpg.is_dearpygui_running():
        loop()
        dpg.render_dearpygui_frame()
    dpg.destroy_context()
