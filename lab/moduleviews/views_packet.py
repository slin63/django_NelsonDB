from collections import OrderedDict
from lab.models import ObsTracker, Measurement
from applets import packet_generator

def generate_packets(request, experiment_id):
    measurements = Measurement.objects.filter(
       measurement_parameter__parameter='Pollinations', obs_tracker__experiment_id=experiment_id
    )
    poll_dict = OrderedDict({})
    # Get plots and their pollination measurements
    for meas in measurements:
        # plot = meas.obs_tracker.obs_plot
        plot = meas.obs_tracker
        polli = meas.value
        poll_dict[plot] = polli

    seed_list = packet_generator.seed_list_make(poll_dict)
    csv_response = packet_generator.seed_list_to_csv(exp_id=experiment_id, seed_list=seed_list)

    return csv_response


