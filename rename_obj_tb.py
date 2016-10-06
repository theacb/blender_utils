import bpy

def rename_obj():
    sel = bpy.context.selected_objects

    for obj in sel:
        children = getChildren(obj)
        if len(children) > 0 :
            child_name = children[0].name
            print (child_name)
            n_loc = child_name.find('n')
            child_trunc = child_name[n_loc:]
            obj.name = child_trunc
        else:
            return
    
def getChildren(myObject): 
    children = [] 
    for ob in bpy.data.objects: 
        if ob.parent == myObject: 
            children.append(ob) 
    return children 

rename_obj()