from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Catalog, Base, Item, User
import json


engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



# Create dummy user
User1 = User(name="Gerald Nah", email="starhubber81@gmail.com",
             picture='https://www.linkedin.com/mpr/mpr/p/7/005/00a/1a6/14f8485.jpg')
session.add(User1)
session.commit()

# Menu for UrbanBurger
catalog = Catalog(user_id=1, name="Electronics")

session.add(catalog)
session.commit()

category_json = json.loads("""{
  "all_categories": [
    {
      "name": "Books",
      "description": "ANGELS & DEMONS"
    },
    {
      "name": "Camping",
      "description": "SURIVIVAL STUFF"
    },
    {
      "name": "Kitchenware",
      "description": "FLYING UTENSILS CAN KILL"
    },
    {
      "name": "Laptops",
      "description": "LENOVO THINKPADS"
    }
  ]
}""")

for e in category_json['all_categories']:
    category_input = Item(
        name=str(e['name']),
        description=str(e['description']),
        catalog=catalog,
        user_id=1
    )
    session.add(category_input)
    session.commit()


# Menu for Super Stir Fry
catalog2 = Catalog(user_id=1, name="Super Stir Fry")

session.add(catalog2)
session.commit()

category_json2 = json.loads("""{
  "all_categories": [
    {
      "name": "MOVIES",
      "description": "Marvel Super Heroes"
    },
    {
      "name": "Camping",
      "description": "SURIVIVAL STUFF FOR THE FITTEST"
    },
    {
      "name": "Kitchenware",
      "description": "FLYING UTENSILS CAN KILL 2"
    },
    {
      "name": "Laptops",
      "description": "ALIENWARE"
    }
  ]
}""")

for e in category_json2['all_categories']:
    category_input = Item(
        name=str(e['name']),
        description=str(e['description']),
        catalog=catalog2,
        user_id=1
    )
    session.add(category_input)
    session.commit()


Item1 = Item(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
             catalog=catalog2)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Peking Duck",
             description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. "
                         "The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat,"
                         " sliced in front of the diners by the cook", catalog=catalog2)

session.add(Item2)
session.commit()

print("added items catalog!")
