from CRUD_алхимия import CRUDCategory

CRUDCategory.add(name="Стейки", parent_id=1)
CRUDCategory.add(name="Роллы", parent_id=2)
for category in CRUDCategory.get_all():
    print(category.name)
    print(category.__dict__)



