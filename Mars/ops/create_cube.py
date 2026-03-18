import bpy
import bmesh
from bpy.types import Operator
from bpy.props import FloatProperty,StringProperty,BoolProperty,IntProperty
from .. import utils


class MARS_OT_CreateCube(Operator):
    bl_label = "Mars Create Cube"
    bl_idname = "mars.create_cube"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Create a mesh cube"

    name: StringProperty(name="Name", default="Boxy") #type:ignore
    size: FloatProperty(name="Size", default=1.0, min=0.01) #type:ignore
    offset: FloatProperty(name="Bevel Offset", default=0.125, min=0) #type:ignore    
    bevel: BoolProperty(name="Use Bevel", default=True) #type:ignore
    segments: IntProperty(name="Bevel Segments", default=3, min=0) #type:ignore

    def execute(self, context):
        # import time
        # print(f"\n=== {time.time()} 开始执行操作符 ===")
        #     # 记录执行前的物体
        # before_objs = set(bpy.data.objects[:])
        # before_names = [obj.name for obj in before_objs]
        # print("执行前物体:", before_names)


        # print("=== 开始创建立方体 ===")  #
        obj = utils.object.create_mesh(name=self.name)
        # print(f"物体类型: {type(obj)}")  #
        # print(f"物体名称: {obj.name}")   #
        # print(f"网格名称: {obj.data.name}")   #
        # print(f"创建前网格顶点数: {len(obj.data.vertices)}")   #
        utils.mesh.create_cube(
            context,
            mesh=obj.data,
            size=self.size, 
            bevel=self.bevel,
            offset=self.offset,
            segments=self.segments
            )
        # print(f"创建后网格顶点数: {len(obj.data.vertices)}")  #
        linked = utils.scene.link_object_to_collection(context, obj)
        print(f"链接结果: {linked}")   


        # # 记录执行后的物体
        # after_objs = set(bpy.data.objects[:])
        # after_names = [obj.name for obj in after_objs]
        # print("执行后物体:", after_names)

        # # 找出新增的物体
        # new_objs = after_objs - before_objs
        # print(f"新增物体数量: {len(new_objs)}")
        # for new_obj in new_objs:
        #     print(f"  新增物体: {new_obj.name} (类型: {new_obj.type})")


        if not linked:
            utils.object.remove_mesh(obj)
            return {'CANCELLED'}
        # print("=== 完成 ===")   #
        return {'FINISHED'}
    


    def draw(self, context):
        layout = self.layout
        layout.prop(self, "name")
        layout.prop(self, "size")
        layout.prop(self, "bevel",text="Use Bevel")
        if self.bevel:
            layout.prop(self, "offset")
            layout.prop(self, "segments")