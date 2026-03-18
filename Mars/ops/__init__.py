import bpy

from .create_cube import MARS_OT_CreateCube

CLASSES = (
    MARS_OT_CreateCube,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)