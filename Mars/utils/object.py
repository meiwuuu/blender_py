import bpy
from bpy.types import Context, Object, Mesh


def create_mesh(name:str="Object"):
    mesh = bpy.data.meshes.new(f"{name}_mesh")
    obj = bpy.data.objects.new(name, mesh)
    return obj


def remove_mesh(obj:Object):
    if isinstance(obj, Object):
        if isinstance(obj.data, Mesh):
            if obj.name in bpy.data.objects:
                mesh = obj.data
                bpy.data.objects.remove(obj)
                bpy.data.meshes.remove(mesh)
                return True 
    return False