import dearpygui.dearpygui as dpg
import os
import yaml
import layout
import globals




def init_editor():
    # font setup...
    # register static images...
    if not os.path.isdir('Config'):
        os.mkdir('Config')
    if os.path.isfile('Config/Editor.ini'):
        with open('Config/Editor.ini', 'r') as f:
            globals.EditorInit = yaml.load(f.read(), yaml.FullLoader)
    else:
        globals.EditorInit['theme'] = 'grey'
        globals.EditorInit['app_size'] = 'FHD'
        globals.EditorInit['global_font_scale'] = 1.0
        globals.EditorInit['project_path'] = ''
        with open('Config/Editor.ini', 'w') as f:
            yaml.dump(globals.EditorInit, f, default_flow_style=False)
    dpg.configure_app(docking=True, docking_space=True)
    if 'active_workspace' in globals.EditorInit:
        dpg.configure_app(init_file=f"Config/{globals.EditorInit['active_workspace']}.ini")


def post_init_editor():
    layout.create_menu()
    layout.create_test_windows()


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
    # if frame_count == 0:
    #     init_editor()
    # if frame_count == 1:
    #     post_init_editor()
    if frame_count > 1 and frame_count % 10 == 0:
        global_tick()
    if frame_count == globals.TimeToKill:
        dpg.stop_dearpygui()
    globals.FrameCount = frame_count + 1


if __name__ == '__main__':
    dpg.create_context()
    init_editor()
    dpg.create_viewport(title='IFCS', width=1920, height=1080, resizable=False)

    # layout.create_menu()
    post_init_editor()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.start_dearpygui()
    if not dpg.is_viewport_ok():
        raise RuntimeError("Viewport not ready")
    while dpg.is_dearpygui_running():
        loop()
        dpg.render_dearpygui_frame()
    dpg.destroy_context()
    globals.save_editor_init()
