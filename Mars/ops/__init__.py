import bpy

from .create_cube import MARS_OT_CreateCube
from .display_graphics import MARS_OT_DisplayGraphics

CLASSES = (
    MARS_OT_CreateCube,
    MARS_OT_DisplayGraphics,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)