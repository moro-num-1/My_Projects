import bpy

def del_objs():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

def add_cube(cube_name):
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.active_object
    cube.name = cube_name
    
def find_obj(obj_name):
    if len(bpy.data.objects) == 0:
        print("You don't have any objects")
    else:
        if obj_name not in bpy.data.objects:
            print(f"Object {obj_name} NOT Found!!")
        else:
            print(f"Object {obj_name} Found!!")
        

def rm_obj(obj_name):
    if obj_name not in bpy.data.objects:
            print(f"Object {obj_name} NOT Found!! It can't be deleted.")
    else:
        objs_list = [o.name for o in bpy.data.objects]
        obj_ind = objs_list.index(obj_name)
        bpy.data.objects.remove(bpy.data.objects[obj_ind])


def main():
    find_obj("Camera")
    rm_obj("Camera")
    find_obj("Camera")


if __name__ == "__main__":
    main()