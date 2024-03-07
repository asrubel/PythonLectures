import json

movies_dict = {
  "movies": [
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010
    },
    {
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "director": "Peter Jackson",
      "year": 2001
    },
    {
      "title": "Parasite",
      "director": "Bong Joon Ho",
      "year": 2019
    }
  ]
}

with open("movies.json", "w") as json_file:
    json.dump(movies_dict, json_file, indent=4)

json_str = json.dumps(movies_dict, indent=4)
print(json_str)

with open("example.json", "r") as json_file:
    movies_dict_from_json = json.load(json_file)

print(movies_dict_from_json)

print(type(json.loads(json_str)))
