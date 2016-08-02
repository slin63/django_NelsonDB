from collections import OrderedDict
from lab.models import ObsTracker, Measurement
from applets import packet_generator


class MeasStruct(object):
    def __init__(self, polli_count, polli_type, obs):
        self.polli_count = polli_count
        self.polli_type = polli_type
        self.obs = obs


def generate_packets(request, experiment_id):
    self_polli = Measurement.objects.filter(
       measurement_parameter__parameter='Self Pollination', obs_tracker__experiment_id=experiment_id
    )
    cross_polli = Measurement.objects.filter(
       measurement_parameter__parameter='Cross Pollination', obs_tracker__experiment_id=experiment_id
    )
    polli_objs = []
    # Get plots and their pollination measurements
    for meas in list(self_polli) + list(cross_polli):
        obs = meas.obs_tracker
        polli_type = meas.measurement_parameter.parameter_type
        polli_count = meas.value
        if meas.value != 0:
            polli_objs.append(MeasStruct(polli_count, polli_type, obs))
        else:
            pass

    seed_list = packet_generator.seed_list_make(polli_objs)
    csv_response = packet_generator.seed_list_to_csv(exp_id=experiment_id, seed_list=seed_list)

    return csv_response


