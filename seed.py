import random
from django_seed import Seed

from backlab.models import Category

seeder = Seed.seeder()

from backlab.models import Category
seeder.add_entity(Category, 5)

inserted_pks = seeder.execute()

# def generate_category_data():
#     seeder = Seed.seeder()
#     random.seed(42)


#     seeder.add_entity(Category, 10)

#     inserted_pks=seeder.execute()

#     print('Seed data generated successfully!')

# generate_category_data()


# print(100+81*11)