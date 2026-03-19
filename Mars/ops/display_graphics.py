import bpy
import gpu
from gpu_extras.batch import batch_for_shader
from bpy.types import Operator
from bpy.props import BoolProperty
from .. import utils

HANDLE = None

class MARS_OT_DisplayGraphics(Operator):
    bl_label = "Mars Display Graphics"
    bl_idname = "mars.display_graphics"
    bl_description = "Start or Stop graphics"


    start_graphics: BoolProperty(name="Start Graphics", default=False) #type:ignore


    def execute(self, context):
        global HANDLE

        if HANDLE is not None:
            bpy.types.SpaceView3D.draw_handler_remove(HANDLE, 'WINDOW')
            HANDLE = None
        #register
        if self.start_graphics:
            HANDLE = bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')
        

        context.area.tag_redraw()

        return {'FINISHED'}
    

coords = [(1, 1, 1), (-2, 0, 0), (-2, -1, 3), (0, 1, 1)]
batch = utils.graphics.create_points_batch(coords)

lines = [(0,0,0),(1,1,1)]
lines_batch = utils.graphics.create_lines_batch(lines)

tris = [(1, 1, 1), (-2, 0, 0), (-2, -1, 3), (0, 1, 1)]
indices = [(0, 1, 2), (1, 2, 3)]
tris_batch = utils.graphics.create_tris_batch(tris, indices)

def draw():
    utils.graphics.set_alpha(True)
    utils.graphics.draw_points_batch(batch, color=(1, 1, 0, 1), size=4)
    utils.graphics.draw_lines_batch(lines_batch, color=(0, 0, 1, 1), width=4.0)
    utils.graphics.draw_tris_batch(tris_batch, color=(1, 1, 1, 0.125))
    utils.graphics.set_alpha(False)


