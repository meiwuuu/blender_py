import bpy
import bmesh
import math
from bmesh.types import BMesh
from mathutils import *
from bpy.types import Context ,Mesh



def create_cube(context:Context, mesh:Mesh ,size:float=1.,bevel=True,offset:float=0.125,segments:int=3):
    if not isinstance(context, Context): return False
    if not isinstance(mesh, Mesh): return False
    if not isinstance(size, float): return False

    if context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    

    bm = bmesh.new(use_operators=True)
    bmesh.ops.create_cube(bm, size=size, matrix=Matrix.Identity(4), calc_uvs=True)

    if bevel:
        bevel_edges(bm, offset, segments)

    bm.to_mesh(mesh)
    bm.free()

    return True


def bevel_edges(bm:BMesh,offset=0.125,segments=3):
    if not isinstance(bm, BMesh): return False
    if not bm.is_valid: return False

    bmesh.ops.bevel(
        bm, 
        geom=bm.edges, 
        offset=offset, 
        offset_type='OFFSET', 
        profile_type='SUPERELLIPSE', 
        segments=segments, 
        profile=0.5, 
        affect='EDGES', 
        clamp_overlap=False, 
        material=0, 
        loop_slide=False, 
        mark_seam=False, 
        mark_sharp=False, 
        harden_normals=False, 
        face_strength_mode='NONE', 
        miter_outer='SHARP', 
        miter_inner='SHARP', 
        spread=0, 
        vmesh_method='ADJ'
        )