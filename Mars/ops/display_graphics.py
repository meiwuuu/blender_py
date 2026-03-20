import bpy
from bpy.types import Operator,Context
from bpy.props import BoolProperty
from datetime import datetime
from .. import utils

HANDLE_POST_VIEW = None
HANDLE_POST_PIXEL = None

class MARS_OT_DisplayGraphics(Operator):
    bl_label = "Mars Display Graphics"
    bl_idname = "mars.display_graphics"
    bl_description = "Start or Stop graphics"


    start_graphics: BoolProperty(name="Start Graphics", default=False) #type:ignore


    def execute(self, context):
        global HANDLE_POST_VIEW,HANDLE_POST_PIXEL

        if HANDLE_POST_VIEW is not None:
            bpy.types.SpaceView3D.draw_handler_remove(HANDLE_POST_VIEW, 'WINDOW')
            HANDLE_POST_VIEW = None

        if HANDLE_POST_PIXEL is not None:
            bpy.types.SpaceView3D.draw_handler_remove(HANDLE_POST_PIXEL, 'WINDOW')
            HANDLE_POST_PIXEL = None


        #register
        if self.start_graphics:
            HANDLE_POST_VIEW = bpy.types.SpaceView3D.draw_handler_add(draw_post_view, (), 'WINDOW', 'POST_VIEW')
            args =(context,)
            HANDLE_POST_PIXEL = bpy.types.SpaceView3D.draw_handler_add(draw_post_pixel, args, 'WINDOW', 'POST_PIXEL')

        context.area.tag_redraw()

        return {'FINISHED'}
    

coords = [(1, 1, 1), (-2, 0, 0), (-2, -1, 3), (0, 1, 1)]
batch = utils.graphics.create_points_batch(coords)

lines = [(0,0,0),(1,1,1)]
lines_batch = utils.graphics.create_lines_batch(lines)

tris = [(1, 1, 1), (-2, 0, 0), (-2, -1, 3), (0, 1, 1)]
indices = [(0, 1, 2), (1, 2, 3)]
tris_batch = utils.graphics.create_tris_batch(tris, indices)

def draw_post_view():
    utils.graphics.set_alpha(True)
    utils.graphics.draw_points_batch(batch, color=(1, 1, 0, 1), size=4)
    utils.graphics.draw_lines_batch(lines_batch, color=(0, 0, 1, 1), width=4.0)
    utils.graphics.draw_tris_batch(tris_batch, color=(1, 1, 1, 0.125))
    utils.graphics.set_alpha(False)


def draw_post_pixel(context:Context):
    area = context.area
    area_height = area.height
    area_width = area.width

    pad = 20 * utils.graphics.screen_factor()
    decender = utils.graphics.measure_decender(size=16)

    now = datetime.now()
    text = f"Day:{now.day} ,Hour{now.hour}, Minutes{now.minute}, Second{now.second}"
    text_width, text_height = utils.graphics.measure_text(text, size=16)

    x=(area_width - text_width) / 2
    y=(area_height - text_height) / 2


    lines = [(x, y - decender),(x + text_width, y - decender)]
    lines_batch = utils.graphics.create_lines_batch(lines)
    utils.graphics.draw_lines_batch(lines_batch, color=(.5, .5, .5, 1), width=1.0)


    utils.graphics.draw_text(
        text=text, 
        position=(x, y), 
        size=16, 
        color=(0, 0, 0, 1)
        )
    
    obj = bpy.context.object
    y -= pad
    
    if isinstance(obj, bpy.types.Object):
        utils.graphics.draw_text(
            text=obj.name, 
            position=(x,y), 
            size=16, 
            color=(0, 0, 0, 1)
            )