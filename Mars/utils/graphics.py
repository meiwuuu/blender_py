import bpy
import gpu
import blf
import math
from gpu.types import GPUBatch
from gpu_extras.batch import batch_for_shader
from mathutils import(
    Vector, 
    Matrix,
    Color
)
#------------------------------------------------------------------------------------------- Screen
def screen_factor():
    return bpy.context.preferences.system.ui_scale



#------------------------------------------------------------------------------------------- Geometry

SHADER_UNIFORM_POINT = gpu.shader.from_builtin('POINT_UNIFORM_COLOR')
SHADER_UNIFORM_LINE = gpu.shader.from_builtin('POLYLINE_UNIFORM_COLOR')
SHADER_UNIFORM_TRI = gpu.shader.from_builtin('UNIFORM_COLOR')

def create_points_batch(coords:list[tuple]) -> GPUBatch:
    batch = batch_for_shader(SHADER_UNIFORM_POINT, 'POINTS', {"pos": coords})
    return  batch

def draw_points_batch(batch:GPUBatch, color:tuple, size:float=4.0):
    SHADER_UNIFORM_POINT.uniform_float("color", color)
    gpu.state.point_size_set(size)
    batch.draw(SHADER_UNIFORM_POINT)



def create_lines_batch(coords:list[tuple]) -> GPUBatch:
    batch = batch_for_shader(SHADER_UNIFORM_LINE, 'LINES', {"pos": coords})
    return batch

def draw_lines_batch(batch:GPUBatch, color:tuple, width:float):
    SHADER_UNIFORM_LINE.uniform_float("viewportSize", gpu.state.viewport_get()[2:])
    SHADER_UNIFORM_LINE.uniform_float("lineWidth", width)
    SHADER_UNIFORM_LINE.uniform_float("color", color)
    batch.draw(SHADER_UNIFORM_LINE)



def create_tris_batch(coords:list[tuple], indices:list[tuple]) -> GPUBatch:
    batch = batch_for_shader(SHADER_UNIFORM_TRI, 'TRIS', {"pos": coords}, indices=indices)
    return batch

def draw_tris_batch(batch:GPUBatch, color:tuple):
    SHADER_UNIFORM_TRI.uniform_float("color", color)
    batch.draw(SHADER_UNIFORM_TRI)

def set_alpha(enable:bool = True):
    if enable:
        gpu.state.blend_set('ALPHA')
    else:
        gpu.state.blend_set('NONE')


#------------------------------------------------------------------------------------------- Font


def draw_text(text:str="", position:tuple=(0,0), size:float=16,color:tuple=(0,0,0,1)):
    factor = screen_factor()
    blf.position(0, *position, 0)
    blf.size(0, size * factor)
    blf.color(0, *color)
    blf.draw(0, text)

def measure_text(text:str="", size:float=16) -> tuple[float, float]:
    factor = screen_factor()
    blf.size(0, size * factor)
    x, y = blf.dimensions(0, text)
    return x, y


def measure_decender(size:float=16) -> float:
    factor = screen_factor()
    blf.size(0, size * factor)
    x, y = blf.dimensions(0, "Klgy`")
    return round(y * 0.25)