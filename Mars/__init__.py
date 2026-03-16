# bl_info 是你在开发 Blender 插件时，必须放在脚本最开头的插件“身份证”。
# 简单来说，它是一个 Python 字典，包含了这个插件的所有关键元信息，
# 比如名字、作者、版本、适用于哪个 Blender 版本等 。
# 当你在 Blender 的偏好设置里浏览插件列表时，看到的所有名称、描述、分类等信息，
# 都是 Blender 从这个 bl_info 字典里读取并展示出来的 。


bl_info={
    "name" : "Mars",
    "discription" : "Mesh editing tools",
    "author" :"m5",
    "blender" : "view3D",
    "category" : "3D view",
}

def register():
    from . import utils
    utils.register()
    from . import props
    props.register()
    from . import ops
    ops.register()
    from . import interfaces
    interfaces.register()


def unregister():
    from . import interfaces
    interfaces.unregister()
    from . import ops
    ops.unregister()
    from . import props
    props.unregister()
    from . import utils
    utils.unregister()

