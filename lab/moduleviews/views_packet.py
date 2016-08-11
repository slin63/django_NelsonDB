from collections import OrderedDict
from lab.models import ObsTracker, Measurement, Experiment
from pandas import DataFrame, concat
from applets import packet_generator
from PedigreeGen import pedigen
from django.http import HttpResponse
from numpy import nan as NULL
import csv


EAR_COUNT_SELF_SIB = 'Self/Sib Pollination Ears'
EAR_QUAL_SELF_SIB = 'Self/Sib Ear Quality'
EAR_COUNT_CROSS = 'Cross Pollination Ears'
EAR_QUAL_CROSS = 'Cross Ear Quality'


def generate_packets(request, experiment_id):
    self_polli = Measurement.objects.filter(measurement_parameter__parameter=EAR_COUNT_SELF_SIB, obs_tracker__experiment_id=experiment_id)
    cross_polli = Measurement.objects.filter(measurement_parameter__parameter=EAR_COUNT_CROSS, obs_tracker__experiment_id=experiment_id)
    exp_name = Experiment.objects.filter(id=experiment_id).values_list('name', flat=True)[0]
    quality_count_dict = quality_count_pair(list(self_polli) + list(cross_polli))

    seed_df = DataFrame()

    # Get plots and their pollination measurements
    for meas in list(self_polli) + list(cross_polli):
        obs = meas.obs_tracker
        plot = obs.obs_plot
        stock = obs.stock
        df_dict = {}
        df_dict['Row'] = split_id(plot.plot_id, 'row')
        df_dict['Plot_ID'] = split_id(plot.plot_id, 'row')
        df_dict['Pedigree'] = stock.pedigree
        df_dict['Source ID'] = stock.seed_id
        df_dict['Seed Name'] = stock.seed_name
        df_dict['Gen'] = plot.gen
        df_dict['Poll_Type'] = plot.polli_type
        df_dict['Researcher'] = "Jamann Lab"
        if meas.measurement_parameter.parameter == EAR_COUNT_SELF_SIB:
            df_dict['earno_self'] = meas.value
            df_dict['earq_self'] = quality_count_dict[meas]
            df_dict['earq_cross'] = df_dict['earno_cross'] = 0
        elif meas.measurement_parameter.parameter == EAR_COUNT_CROSS:
            df_dict['earno_self'] = df_dict['earq_self'] = 0
            df_dict['earno_cross'] = meas.value
            df_dict['earq_self'] = quality_count_dict[meas]
        df_dict['shell'] = plot.get_shell_type(pedigen=True)

        if meas.value != 0: # Making sure we got corn from this ear
            buffer_df = DataFrame(df_dict, index=[0])
            seed_df = concat([seed_df, buffer_df])
        else:
            pass

    if seed_df.empty:
        return HttpResponse("No data!")

    csv_string = pedigen.process_dataframes(seed_df, exp_name)

    return string_to_csv_response(csv_string, exp_name)


def string_to_csv_response(string, exp_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}_seed_labels.csv"'.format(exp_name)
    writer = csv.writer(response)
    buffer_l = string.split("\n") # Just using some bs to convert a CSV-format string to a CSV-format list
    csv_l = [e.split(',') for e in buffer_l]
    for row in csv_l:
        writer.writerow(row)

    return response


def quality_count_pair(meas_count_objs):
    # Returns {ear count: ear quality} dict for measurements
    cnt_to_qlty = {}
    for meas in meas_count_objs:
        obs = meas.obs_tracker
        if meas.measurement_parameter.parameter == EAR_COUNT_SELF_SIB:
            try:
                cnt_to_qlty[meas] = Measurement.objects.get(measurement_parameter__parameter=EAR_QUAL_SELF_SIB, obs_tracker=obs).value
            except Measurement.DoesNotExist:
                cnt_to_qlty[meas] = 0
        elif meas.measurement_parameter.parameter == EAR_COUNT_CROSS:
            try:
                cnt_to_qlty[meas] = Measurement.objects.get(measurement_parameter__parameter=EAR_QUAL_CROSS, obs_tracker=obs).value
            except Measurement.DoesNotExist:
                cnt_to_qlty[meas] = 0

    return cnt_to_qlty


def split_id(plot_id, type):
        zero_index = plot_id.find('0')
        ret = ''
        if type == 'row':
            ret = int(plot_id[4:])
        if type == 'exp':
            ret =  plot_id[:4]
        return ret
