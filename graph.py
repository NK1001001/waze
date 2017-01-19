from collections import namedtuple
import tools
import sys
# define class Link_traffic_params
# Some additional parameters for a link
Link_traffic_params = namedtuple('Link_traffic_params',
                                 ['cos_frequency',
                                  'sin_frequency',
                                  ])


# define class Junction
Junction = namedtuple('Junction',
                      ['index',  # int
                       'lat', 'lon',  # floats: latitude/longitude
                       'links',  # list of Link
                       ])

# define class Link
Link = namedtuple('Link',
                  ['source', 'target',  # int (junction indices)
                   'distance',  # float
                   'highway_type',  # int < len(road_info.ROAD_TYPES)
                   'link_params',  # a tuple of 2 floats.
                   ])

#class Roads(dict):


def make_link(i, link_str):
    link_params = [int(x) for x in link_str.split("@")]
    link = Link(i, *(link_params + [Link_traffic_params(*tools.generate_traffic_noise_params(i, link_params[0]))]))
            #Link(i, *(link_params + [Link_traffic_params(*tools.generate_traffic_noise_params(i, link_params[0]))]))
    print('link is: ', link)

def make_junction(ind_str, lat_str, long_str, *link_row):
    print('make_junction: ind_str: ', ind_str)
    print('make_junction, link_row: ', link_row)
    index, lat, long = int(ind_str), float(lat_str), float(long_str)

    try:
        links = tuple(make_link(index, lnk)
                      for lnk in link_row)
        #links = tuple(filter(lambda lnk: lnk.distance > 0, links))
    except ValueError:
        links = []
    junc = Junction(index, lat, long, links)
    print('junction is: ', junc)


@tools.timed
def load_map(filename, start=0, count=sys.maxsize):
    import csv
    from itertools import islice
    with tools.dbopen(filename, 'rt') as f:
        it = islice(f, start, min(start + count, sys.maxsize))
        cnt = 0d
        for row in csv.reader(it):
           # print(row)
            make_junction(*row)
            cnt += 1
            if cnt == 3:
                break

# list = {row[0]: make_junction(*row) for row in csv.reader(it)}

if __name__ == '__main__':
    load_map('israel.csv')
