import bpy

from .view_3d_panel import MARS_PT_Operations

CLASSES = (
    MARS_PT_Operations,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)

 