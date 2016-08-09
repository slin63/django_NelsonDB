from collections import OrderedDict
from lab.models import ObsTracker, Measurement
from applets import packet_generator

# Data structs
class MeasStruct(object):
    def __init__(self, polli_count, polli_type, obs):
        self.polli_count = polli_count
        self.polli_type = polli_type
        self.obs = obs

class PlotStruct(object):
    def __init__(self, plot_id, stock_id, gen, poll_type, polli_count):
        self.plot_id = plot_id
        self.stock_id = stock_id
        self.gen = gen
        self.poll_type = poll_type
        self.row = split_id('row')
        self.exp = split_id('exp')
        self.polli_count = polli_count

    def split_id(self, type):
        zero_index = self.plot_id.find('0')
        ret = ''
        if type == 'row':
            ret = int(self.plot_id[4:])
        if type == 'exp':
            ret =  self.plot_id[:4]
        return ret
            

def generate_packets(request, experiment_id):
    self_polli = Measurement.objects.filter(
       measurement_parameter__parameter='Self/Sib Pollination', obs_tracker__experiment_id=experiment_id
    )
    cross_polli = Measurement.objects.filter(
       measurement_parameter__parameter='Cross Pollination', obs_tracker__experiment_id=experiment_id
    )
    polli_objs = []
    plot_objs = []
    # Get plots and their pollination measurements
    for meas in list(self_polli) + list(cross_polli):
        obs = meas.obs_tracker
        polli_type = meas.measurement_parameter.parameter_type
        polli_count = meas.valu
        plot_id = obs.obs_plot.plot_id
        stock_id = obs.stock.seed_id
        gen = obs.obs_plot.gen
        
        if meas.value != 0:
            polli_objs.append(MeasStruct(polli_count, polli_type, obs))
            plot_objs.append(PlotStruct(plot_id, stock_id, gen, polli_type, polli_count))
        else:
            pass

    seed_list = packet_generator.seed_list_make(polli_objs)
    csv_response = packet_generator.seed_list_to_csv(exp_id=experiment_id, seed_list=seed_list)

    return csv_response



