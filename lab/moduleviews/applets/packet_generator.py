# Generates a CSV with label info when passed a dictionary formatted {plot: pollination_string}
# www.github.com/slin63
# slin63@illinois.edu

from django.http import HttpResponse
from lab.models import ObsPlot, Experiment, ObsTracker
import csv

HEADER = ['Seed ID', 'Pedigree', 'Researcher', 'Plot ID', 'Plot Name', 'Plot', 'Block', 'Rep', 'Kernel Num', 'Planting Date', 'Harvest Date']


class SeedPacket(object):
    def __init__(self, seed_id, pedigree, trailing_info):
        self.seed_id = seed_id
        self.pedigree = pedigree
        self.trailing_info = trailing_info

    def get_values(self):
        return (self.seed_id, self.pedigree) + self.trailing_info

    def __repr__(self):
        return self.seed_id + ' ' + self.trailing_info


def seed_list_make(polli_objs):
    seed_list = []
    for e in polli_objs:
        polli_type = e.polli_type
        polli_range = e.polli_count
        seed_pedigree = get_pedigree('#TODO')
        researcher = ObsTracker.objects.values_list('user__first_name', 'user__last_name').get(id=e.obs.id)
        trailing_info = (' '.join(researcher),)
        trailing_info += ObsPlot.objects.values_list('plot_id', 'plot_name', 'plot', 'block', 'rep', 'kernel_num', 'planting_date', 'harvest_date').get(id=e.obs.obs_plot.id)

        for num in xrange(1, int(polli_range) + 1):
            seed_id = seed_name_make(plot_id=e.obs.obs_plot.plot_id, num=num, polli_type=polli_type)
            seed_list.append(SeedPacket(seed_id=seed_id, pedigree=seed_pedigree, trailing_info=trailing_info))

    return seed_list


def get_pedigree(seed_id):
    return '##TODO'


def seed_name_make(plot_id, num, polli_type):
    if polli_type.lower() == 'cross':
        polli_type = 'b'
    else:
        polli_type = 's'

    if num < 10:
        num_str = "{}_00{}{}".format(plot_id, num, polli_type)
    else:
        num_str = "{}_0{}{}".format(plot_id, num, polli_type)

    return num_str


def seed_list_to_csv(exp_id, seed_list):
    exp_name = Experiment.objects.get(id=exp_id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}_seed_labels.csv"'.format(exp_name)
    writer = csv.writer(response)
    writer.writerow(HEADER)
    for row in seed_list:
        writer.writerow(row.get_values())

    return response

