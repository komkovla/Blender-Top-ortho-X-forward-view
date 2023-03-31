import bpy

bl_info = {
    "name": "X-Forward View",
    "description": """Introducing "X-Forward View" - the Blender add-on that lets you quickly and easily change your viewport to the X-forward location!
Have you ever found yourself struggling to find the perfect angle for your model or scene? With X-Forward View, you can quickly and easily switch to the X-forward location, allowing you to view your work from a new perspective and make better decisions.This simple yet powerful add-on adds a new operator to the Viewport menu, making it easy to access and use. Simply select the X-forward View operator and your viewport will be instantly transformed. X-Forward View is perfect for 3D artists, designers, and anyone who wants to streamline their workflow and take their work to the next level. So why wait? Try X-Forward View today and start seeing your work in a whole new way!""",
    "author": "K3D",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > View > Top x forward",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object",
}

class Top_x_forward(bpy.types.Operator):
    """Top x forward"""
    bl_idname = "rotate3d_view.top_x"
    bl_label = "Rotate 3d view x top"

    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces[0].region_3d.view_rotation = (0.7071068, 0, 0, 0.7071068)
                area.spaces[0].region_3d.view_perspective = 'ORTHO'
                break
        return {'FINISHED'}

def menu_draw(self, context):
    self.layout.operator(Top_x_forward.bl_idname)

def register():
    bpy.utils.register_class(Top_x_forward)
    bpy.types.VIEW3D_MT_view.append(menu_draw)

def unregister():
    bpy.utils.unregister_class(Top_x_forward)
    bpy.types.VIEW3D_MT_view.remove(menu_draw)


if __name__ == "__main__":
    register()