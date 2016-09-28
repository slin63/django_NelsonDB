from collections import OrderedDict
from lab.models import ObsTracker, Measurement, Experiment, StockPacket, Stock
from pandas import DataFrame, concat, merge
from applets import packet_generator
from PedigreeGen import pedigen
from numpy import nan as NULL
import csv

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from lab.forms import PacketGenForm


EAR_COUNT_SELF_SIB = 'Self/Sib Pollination Ears'
EAR_QUAL_SELF_SIB = 'Self/Sib Ear Quality'
EAR_COUNT_CROSS = 'Cross Pollination Ears'
EAR_QUAL_CROSS = 'Cross Ear Quality'
RESEARCHER = 'Jamann Lab'
EMPTY_DF = DataFrame()


def packet_menu(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict['logged_in_user'] = request.user.username
    view = None

    if request.method == 'POST':
        form = PacketGenForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['confirm'] is True:
                exp = form.cleaned_data['exp']
                choice = form.cleaned_data['packet_choice']
                if choice == 'generate_labels':
                    view = download_labels(request, exp)
                elif choice == 'preview_packets':
                    view = preview_packets(request, exp)
                elif choice == 'create_packets':
                    success = create_packets(request, exp)
                    if not success:
                        context_dict['errors'] = "Failed to create packets"
                        context_dict['form'] = PacketGenForm()
                        view = render_to_response("lab/packet_gen/packet_gen_form.html", context_dict, context)
                    if success:
                        context_dict['success'] = "Successfully created {} packets!".format(success)
                        context_dict['form'] = PacketGenForm()
                        view = render_to_response("lab/packet_gen/packet_gen_form.html", context_dict, context)
            else:
                context_dict['errors'] = "Did not confirm!"
                context_dict['form'] = PacketGenForm()
                view = render_to_response("lab/packet_gen/packet_gen_form.html", context_dict, context)
        else:
            context_dict['errors'] = "Incomplete Form"
            context_dict['form'] = PacketGenForm()
            view = render_to_response("lab/packet_gen/packet_gen_form.html", context_dict, context)

    elif request.method == 'GET':
        form = PacketGenForm()
        context_dict['form'] = form
        view = render_to_response("lab/packet_gen/packet_gen_form.html", context_dict, context)

    return view


def download_labels(request, exp):
    csv_string = generate_packet_dataframe(request, exp.id)
    file_name = "{}_seed_labels.csv".format(exp.name)
    return string_to_csv_response(csv_string, file_name)


def preview_packets(request, exp):
    packet_df = generate_packet_dataframe(request, exp.id, df_return=True, processing=True)
    if packet_df.empty:
        packet_df = EMPTY_DF
    else:
        packet_df = extract_packet_info(packet_df)

    csv_string = packet_df.to_csv(index=False, index_label=False)
    file_name = "{}_packet_preview.csv".format(exp.name)
    return string_to_csv_response(csv_string, file_name)


def create_packets(request, exp):
    success = False
    packet_df = generate_packet_dataframe(request, exp.id, df_return=True, processing=True)


    if packet_df.empty:
        success = False
    else:
        packet_df = extract_packet_info(packet_df)
        packet_count = 0

        for index, row in packet_df.iterrows():
            try:
                sp = StockPacket.objects.create(
                    stock=Stock.objects.get(seed_id=row['Maternal_ID']),
                    location_id=1,
                    seed_id=row['seed_ID'],
                    gen=row['seed_gen'],
                    pedigree=row['Pedigree']
                )
                sp.save()

                packet_count += 1
                print "Created PACKET: [ID:{}]-[GEN:{}]-[PED:{}]".format(sp.seed_id, sp.gen, sp.pedigree)
            except (IntegrityError, Stock.DoesNotExist) as e:
                print("Packet Error: %s %s" % (e.message, e.args))
                pass



    return packet_count


def extract_packet_info(df):
    packet_df = df[['seed_ID', 'seed_gen', 'Pedigree', 'source_ID', 'Maternal_ID']]
    return packet_df


def generate_packet_dataframe(request, experiment_id, df_return=False, processing=True):
    self_polli = Measurement.objects.filter(measurement_parameter__parameter=EAR_COUNT_SELF_SIB, obs_tracker__experiment_id=experiment_id)
    cross_polli = Measurement.objects.filter(measurement_parameter__parameter=EAR_COUNT_CROSS, obs_tracker__experiment_id=experiment_id)
    males = ObsTracker.objects.filter(experiment_id=experiment_id, obs_entity_type='plot', obs_plot__is_male=True)
    exp_name = Experiment.objects.filter(id=experiment_id).values_list('name', flat=True)[0]
    quality_count_dict = quality_count_pair(list(self_polli) + list(cross_polli))

    seed_df = DataFrame()
    view = None
    # Get plots and their pollination measurements
    for meas in list(self_polli) + list(cross_polli) + list(males):
        df_dict = {}

        if isinstance(meas, ObsTracker):
            obs = meas
            plot = obs.obs_plot
            stock = obs.stock
            df_dict['earq_cross'] = df_dict['earno_cross'] = 0
            df_dict['earno_self'] = 0
            df_dict['earq_self'] = 0

        else:

            obs = meas.obs_tracker
            plot = obs.obs_plot
            stock = obs.stock
            if meas.measurement_parameter.parameter == EAR_COUNT_SELF_SIB:
                df_dict['earq_cross'] = df_dict['earno_cross'] = 0
                df_dict['earno_self'] = meas.value
                df_dict['earq_self'] = quality_count_dict[meas]
            elif meas.measurement_parameter.parameter == EAR_COUNT_CROSS:
                df_dict['earno_self'] = df_dict['earq_self'] = 0
                df_dict['earno_cross'] = meas.value
                df_dict['earq_cross'] = quality_count_dict[meas]

        df_dict['Row'] = split_id(plot.plot_id, 'row')
        df_dict['Plot_ID'] = split_id(plot.plot_id, 'row')
        df_dict['Pedigree'] = stock.pedigree
        df_dict['Source ID'] = stock.seed_id
        df_dict['Maternal_ID'] = stock.seed_id
        df_dict['Seed Name'] = stock.seed_name
        df_dict['Gen'] = plot.gen
        df_dict['is_male'] = plot.is_male
        df_dict['cross_target'] = plot.cross_target
        df_dict['Poll_Type'] = plot.polli_type
        df_dict['Researcher'] = RESEARCHER

        df_dict['shell'] = plot.get_shell_type(pedigen=True)

        if str(df_dict['earno_self']) == '0' and str(df_dict['earno_cross']) == '0':
            continue

        else:
            if isinstance(meas, Measurement):
                if meas.value != 0: # Making sure we got corn from this ear
                    buffer_df = DataFrame(df_dict, index=[0])
                    seed_df = concat([seed_df, buffer_df])
                else:
                    pass
            else:
                buffer_df = DataFrame(df_dict, index=[0])
                seed_df = concat([seed_df, buffer_df])


    # If empty and requesting a processed DF
    if seed_df.empty and processing and df_return:
        view = EMPTY_DF
    # If empty and requesting a processed CSV string
    elif seed_df.empty and processing:
        view = EMPTY_DF.to_csv()
    # Not empty and requesting a processed CSV string
    elif processing:
        view = pedigen.process_dataframes(seed_df, exp_name, df_return)
    # Not empty and requesting a non-processed CSV string
    elif not seed_df.empty and not processing:
        view = seed_df.to_csv()
    else:
        view = EMPTY_DF


    return view


def string_to_csv_response(string, file_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
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
