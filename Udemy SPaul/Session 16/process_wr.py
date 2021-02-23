import csv

with open('wr.csv', 'r') as file_object:
    # first creating the DictReader object
    csv_dict_reader = csv.DictReader(file_object)
    # fieldnames = csv_dict_reader.fieldnames
    # print(fieldnames)

    with open('track.csv', 'w', newline='') as ft_object:
        with open('road.csv', 'w', newline='') as fr_object:

            fieldnames = ['', 'distance', 'place', 'time', 'date']

            ft_writer = csv.DictWriter(ft_object, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            ft_writer.writeheader()
            fr_writer = csv.DictWriter(fr_object, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            fr_writer.writeheader()

            track_rec = 1
            road_rec = 1

            for rec in csv_dict_reader:
                if rec['road_or_track'] == 'track':
                    ft_writer.writerow({'': track_rec, 'distance': rec['distance'], 'place': rec['place'], 'time': rec['time'],
                                        'date': rec['date']})
                    track_rec += 1
                else:
                    fr_writer.writerow(
                        {'': road_rec, 'distance': rec['distance'], 'place': rec['place'], 'time': rec['time'],
                         'date': rec['date']})

                    road_rec += 1
