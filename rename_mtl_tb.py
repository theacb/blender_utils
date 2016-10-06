import bpy
import os
import random

tex_folder = os.path.normpath(r"E:/dump/projects/tb/vizitour/assets/context/bake/v03")
tex_file_format = "png"
tex_uv_channel_name = "UVChannel_3"

sel = bpy.context.selected_objects


def rename_mtl(objs, folder, file_format, uv_channel_name):
    for obj in objs:
        if obj.type == 'MESH':
            strip_mtls(obj)
            strip_uvs(obj, uv_channel_name)

            mtl = bpy.data.materials.new(obj.name)

            mtl.diffuse_color = rand_col(0.1, 1.0)

            obj.data.materials.append(mtl)

            mtl.use_shadeless = True

            img_name = "{0}.{1}".format(obj.name, file_format)

            img_path = os.path.join(folder, img_name)

            if os.path.isfile(img_path):
                img_file = bpy.data.images.load(img_path)

                img_file.use_alpha = False

                print("Assigning image texture: {0} to material: {1}".format(img_path, mtl.name))

                color_tex = bpy.data.textures.new(obj.name,
                                                  type='IMAGE'
                                                  )
                color_tex.image = img_file

                material_tex = mtl.texture_slots.add()

                material_tex.texture = color_tex
                material_tex.texture_coords = 'UV'
                material_tex.use_map_color_diffuse = True
                material_tex.mapping = 'FLAT'
                material_tex.uv_layer = uv_channel_name

            else:
                print("Texture file: {0} does not exist".format(img_path))


def strip_uvs(obj, to_keep):
    uv_textures = obj.data.uv_textures
    
    if len(to_keep) > 0 and to_keep in uv_textures:
        uv_textures[to_keep].active = True
    uv_textures = obj.data.uv_textures
    
    i = 0
    while len(uv_textures) > 1:
        if uv_textures[i].name != to_keep:
            uv_textures.remove(uv_textures[i])
        else:
            i = 1


def strip_mtls(obj):
    materials = obj.data.materials
    materials.clear(1)


def rand_col(min_col=0.0, max_col=1.0):
    return (random.uniform(min_col, max_col), 
            random.uniform(min_col, max_col), 
            random.uniform(min_col, max_col)
            )


rename_mtl(sel, tex_folder, tex_file_format, tex_uv_channel_name)
