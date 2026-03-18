import bpy
from bpy.types import Context,Object


def link_object_to_collection(context:Context,obj:Object):
    if isinstance(context,Context):
        if isinstance(obj,Object):
            scene = context.scene
            scene.collection.objects.link(obj)
            return True
    return False