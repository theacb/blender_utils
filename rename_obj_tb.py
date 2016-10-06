import bpy


def rename_obj():
    """
    Renames selected objects based on the names of their children
    :return:
    """
    sel = bpy.context.selected_objects

    for obj in sel:
        children = get_children(obj)
        if len(children) > 0:
            child_name = children[0].name
            print(child_name)
            n_loc = child_name.find('n')
            child_trunc = child_name[n_loc:]
            obj.name = child_trunc
        else:
            return


def get_children(my_object):
    """
    Finds an object's children, very inefficient
    :param my_object: The object to find from
    :return:
    """
    children = [] 
    for ob in bpy.data.objects: 
        if ob.parent == my_object:
            children.append(ob) 
    return children 

rename_obj()
