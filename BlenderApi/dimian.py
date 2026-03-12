bl_info = {
    "name": "地面对齐",
    "author": "m5",
    "version": (1, 0),
    "blender": (3, 4, 1),
    "location": "f3",
    "description": "地面对齐",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy

class dimianOP(bpy.types.Operator):
    bl_idname="obj.dimian"
    bl_label="地面对齐"
    
    def execute(self,context):
        bpy.ops.object.align(align_mode='OPT_1', relative_to='OPT_1', align_axis={'Z'})
        return{'FINISHED'}

class m5Tools(bpy.types.Header):
    
    bl_space_type='INFO'

    def draw(self,context):
        self.layout.operator("obj.dimian")


def register():
    bpy.utils.register_class(dimianOP)
    bpy.utils.register_class(m5Tools)

def unregister():
    bpy.utils.unregister_class(dimianOP)
    bpy.utils.unregister_class(m5Tools)
    
if __name__ == "__main__":
    register()
