import bpy
from bpy.types import Panel

class MARS_PT_Operations(Panel):
    bl_label       = "Mars"
    bl_space_type  ="VIEW_3D"
    bl_region_type = "UI"         #region写错写成ragion了
    bl_category    = "Mars"
    bl_options     = {'HEADER_LAYOUT_EXPAND'}

    #第一次写错把方法写到类外面去了
    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout

        layout.operator("mars.create_cube")
        
        props = layout.operator("mars.display_graphics",text="Start Graphics")
        props.start_graphics = True

        props = layout.operator("mars.display_graphics",text="Stop Graphics")
        props.start_graphics = False

