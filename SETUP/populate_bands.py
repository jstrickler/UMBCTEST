import yaml

from bands.models import Band, Genre, Member

with open("../../../DATA/bands.yaml") as bands_in:
    bands_data = yaml.load(bands_in)

for s in bands_data:
    print("Adding", s['name'])

    # add genre
    genre_name = s['genre']
    results = Genre.objects.filter(name=genre_name)
    if results:
        genre = results[0]
    else:
        genre = Genre(name=s['genre'])
        genre.save()

    # add members
    members = []
    for member in s['members']:
        results = Member.objects.filter(name=member)
        if not results:
            e = Member(name=member)
            e.save()
            members.append(e)

    band = Band(
        name = s['name'],
        genre = genre,
    )

    band.save()

    for member in members:
        band.members.add(member)

    band.save()
