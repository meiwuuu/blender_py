import bpy
import bmesh
import math
from mathutils import *
from bpy.types import Context ,Mesh



def create_cube(context:Context, mesh:Mesh ,size:float=1.0):
    if not isinstance(context, Context): return False
    if not isinstance(mesh, Mesh): return False
    if not isinstance(size, float): return False
    
    if context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    

    bm = bmesh.new(use_operators=True)
    bmesh.ops.create_cube(bm, size=size, matrix=Matrix.Identity(4), calc_uvs=True)
    bm.to_mesh(mesh)
    bm.free()

    return True