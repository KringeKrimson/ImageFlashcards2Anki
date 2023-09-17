import genanki
import os

# Name for the flashcards
_name_ = input("Name of flashcards:\n")
directory = os.getcwd()  # Gets the directory of this Python file
list_of_images_in_dir = []

my_model = genanki.Model(
    121212,
    'Basic',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{Back}}',
        },
    ])

my_deck = genanki.Deck(
    121213,  # Use a fixed deck ID for simplicity
    _name_)

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            list_of_images_in_dir.append(filename)

total_images = len(list_of_images_in_dir)
list_of_images_in_dir = sorted(list_of_images_in_dir, key=lambda x: int(x.split('.')[0]))

if total_images % 2 != 0:
    print('Please ensure you have an even number of images for front and back of cards.')
else:
    for c in range(0, len(list_of_images_in_dir), 2):
        front_image = list_of_images_in_dir[c]
        back_image = list_of_images_in_dir[c+1]
        print(front_image, back_image)
        my_note = genanki.Note(
            model=my_model,
            fields=[f'<img src={front_image}>', f'<img src={back_image}>'])
        my_deck.add_note(my_note)
        print("Card added:", front_image, "and", back_image)

    print("Total Cards Added:", total_images // 2)

    my_package = genanki.Package(my_deck)
    my_package.media_files = list_of_images_in_dir

    output_file = f'{_name_}.apkg'
    my_package.write_to_file(output_file)
    print(f"Deck saved as '{output_file}'")

input("Press Enter to Close Window...")
