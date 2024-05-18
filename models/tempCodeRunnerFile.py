 ob1.to_dict()
print(obj_dict)
new_obj = BaseModel(**obj_dict)
print(new_obj)