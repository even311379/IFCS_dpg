import yaml

FrameCount = 0
EditorInit = {}
TimeToKill = -1


def save_editor_init():
    init = EditorInit
    with open('Config/Editor.ini', 'w') as f:
        yaml.dump(init, f, default_flow_style=False)
