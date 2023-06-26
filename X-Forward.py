import bpy
from bpy.types import AddonPreferences, Operator
from bpy.props import StringProperty
 
# Add-on info ------------------------------

bl_info = {
    "name": "X-Forward View",
    "description": "Rotate 3d view to the top view x forward",
    "author": "Vladislav Komkov",
    "version": (1, 1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > View > Top x forward",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View",
}

# Operator ------------------------------

class Top_x_forward(Operator):
    """Top x forward"""
    bl_idname = "wm.rotate3d_view_top_x"
    bl_label = "Rotate 3d view x top"

    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        region_3d = space.region_3d
                        # Top x forward
                        region_3d.view_rotation = (-0.7071068, 0, 0, 0.7071068)

                        # Orthographic view
                        region_3d.view_perspective = 'ORTHO'
                        region_3d.is_orthographic_side_view = True
                        region_3d.is_perspective = False
                        break
        return {'FINISHED'}

def menu_draw(self, context):
    self.layout.operator(Top_x_forward.bl_idname)

# Register and unregister functions ------------------------------

def register():
    bpy.utils.register_class(Top_x_forward)
    bpy.utils.register_class(ShortcutInfoAddonPreferences)
    bpy.types.VIEW3D_MT_view.append(menu_draw)

def unregister():
    bpy.utils.unregister_class(Top_x_forward)
    bpy.types.VIEW3D_MT_view.remove(menu_draw)


if __name__ == "__main__":
    register()

# Helpers ------------------------------

# Define the add-on preferences
class ShortcutInfoAddonPreferences(AddonPreferences):
    bl_idname = __name__

    info_text: StringProperty(name="Shortcut Info", default="""
    To assign a shortcut to the "Top x forward" command:
    3D Viewport - View - Right-mouse-click - assign shortcut
    """)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Shortcut:")
        for line in self.info_text.splitlines():
            layout.label(text=line)
