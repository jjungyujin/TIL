from pathlib import Path

dir_path = Path('../data/StanfordDogs/Images')

for breed_dir in dir_path.iterdir():
  str_breed_dir = str(breed_dir).split('/')[-1]
  breed_name = str_breed_dir.split('-', 1)[1]
  breed_dir.rename(Path(f'../data/StanfordDogs/Images/{breed_name}'))

print("Successfully renamed all directory !")