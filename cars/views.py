import json
from django.shortcuts import render


def index(request):
    kars = [
        {
            'color': 'gold',
            'name': 'Chevrolet Trax',
            '2021': 22020,
            '2020': 19292,
            '2019': 17560,
            '2018': 16443,
            '2017': 15138,
            '2016': 12442,
        },
        {
            'color': 'gold',
            'name': 'Chevrolet Equinox',
            '2021': 28000,
            '2020': 22217,
            '2019': 21136,
            '2018': 20263,
            '2017': 17624,
            '2016': 15469,
        },
        {
            'color': 'gold',
            'name': 'Chevrolet Traverse',
            '2021': 35200,
            '2020': 33319,
            '2019': 30484,
            '2018': 29394,
            '2017': 21454,
            '2016': 18822,
        },
        {
            'color': 'blue',
            'name': 'Ford Edge',
            '2021': 34745,
            '2020': 26641,
            '2019': 23508,
            '2018': 20491,
            '2017': 18802,
            '2016': 15869,
        },
        {
            'color': 'blue',
            'name': 'Ford Escape',
            '2021': 27055,
            '2020': 24943,
            '2019': 22532,
            '2018': 19847,
            '2017': 17175,
            '2016': 15071,
        },
        {
            'color': 'blue',
            'name': 'Ford EcoSport',
            '2021': 21990,
            '2020': 16470,
            '2019': 16492,
            '2018': 16537,
        },
        {
            'color': 'black',
            'name': 'VW Tiguan',
            '2021': 26545,
            '2020': 22590,
            '2019': 20049,
            '2018': 18566,
            '2017': 15394,
            '2016': 12766,
        },
        {
            'color': 'darkred',
            'name': 'Mazda CX-5',
            '2021': 26770,
            '2020': 22606,
            '2019': 22432,
            '2018': 20852,
            '2017': 18175,
            '2016': 16592,
        },
        {
            'color': 'green',
            'name': 'Subaru Crosstrek',
            '2021': 23595,
            '2020': 22948,
            '2019': 22506,
            '2018': 21106,
            '2017': 18911,
            '2016': 16138,
        },
        {
            'color': 'green',
            'name': 'Subaru Outback',
            '2021': 26795,
            '2020': 25557,
            '2019': 23205,
            '2018': 21148,
            '2017': 18452,
            '2016': 16997,
        },
        {
            'color': 'green',
            'name': 'Subaru Ascent',
            '2021': 32295,
            '2020': 28839,
            '2019': 28229,
        },
        {
            'color': 'green',
            'name': 'Subaru Forrester',
            '2021': 24795,
            '2020': 24531,
            '2019': 21808,
            '2018': 20847,
            '2017': 18279,
            '2016': 14948,
        },
        {
            'color': 'red',
            'name': 'Toyota Rav4',
            '2021': 27650,
            '2020': 26438,
            '2019': 25166,
            '2018': 21558,
            '2017': 19704,
            '2016': 17883,
        },
        {
            'color': 'red',
            'name': 'Toyota Rav4 Hybrid',
            '2021': 28800,
            '2020': 25701,
            '2019': 25719,
            '2018': 22834,
            '2017': 19504,
        },
        {
            'color': 'purple',
            'name': 'Kia Sorento',
            '2021': 31190,
            '2020': 25959,
            '2019': 24479,
            '2018': 21980,
            '2017': 19500,
            '2016': 17883,
        },
        {
            'color': 'purple',
            'name': 'Kia Sportage',
            '2021': 25590,
            '2020': 20753,
            '2019': 19880,
            '2018': 18471,
            '2017': 17175,
            '2016': 14306,
        },
        {
            'color': 'lightblue',
            'name': 'Hyundai Santa Fe',
            '2021': 28700,
            '2020': 24820,
            '2019': 23810,
            '2018': 23976,
            '2017': 20866,
            '2016': 16954,
        },
        {
            'color': 'lightblue',
            'name': 'Hyundai Tuscon',
            '2021': 25100,
            '2020': 22102,
            '2019': 20970,
            '2018': 19201,
            '2017': 17784,
            '2016': 16384,
        },
        {
            'color': 'gray',
            'name': 'Honda CR-V',
            '2021': 26850,
            '2020': 24421,
            '2019': 23843,
            '2018': 21681,
            '2017': 19983,
            '2016': 17035,
        },
        {
            'color': 'gray',
            'name': 'Honda HR-V',
            '2021': 22720,
            '2020': 20542,
            '2019': 19551,
            '2018': 18157,
            '2017': 16707,
            '2016': 15369,
        },
    ]
    context = []
    for kar in kars:
        car = {}
        car['label'] = kar['name']
        price_data_by_year = [kar['2021'], kar['2020'], kar['2019']]
        if '2018' in kar:
            price_data_by_year.append(kar['2018'])
        if '2017' in kar:
            price_data_by_year.append(kar['2017'])
        if '2016' in kar:
            price_data_by_year.append(kar['2016'])
        car['data'] = price_data_by_year
        car['color'] = kar['color']
        context.append(car)
    return render(request, 'cars/index.html', {'datasets': context})


def value_lost(request):
    kars = [
        {
            'color': 'gold',
            'name': 'Chevrolet Trax',
            '2021': 0,
            '2020': -2508,
            '2019': -5240,
            '2018': -6057,
            '2017': -7362,
            '2016': -9358,
        },
        {
            'color': 'gold',
            'name': 'Chevrolet Equinox',
            '2021': 0,
            '2020': -7179,
            '2019': -6464,
            '2018': -7037,
            '2017': -9636,
            '2016': -11691,
        },
        {
            'color': 'gold',
            'name': 'Chevrolet Traverse',
            '2021': 0,
            '2020': -1581,
            '2019': -4416,
            '2018': -5206,
            '2017': -11846,
            '2016': -14383,
        },
        {
            'color': 'blue',
            'name': 'Ford Edge',
            '2021': 0,
            '2020': -6454,
            '2019': -8482,
            '2018': -13554,
            '2017': -14983,
            '2016': -17416,
        },
        {
            'color': 'blue',
            'name': 'Ford Escape',
            '2021': 0,
            '2020': -1442,
            '2019': -5468,
            '2018': -7203,
            '2017': -9825,
            '2016': -11979,
        },
        {
            'color': 'blue',
            'name': 'Ford EcoSport',
            '2021': 0,
            '2020': -5120,
            '2019': -5098,
            '2018': -5053,
        },
        {
            'color': 'black',
            'name': 'VW Tiguan',
            '2021': 0,
            '2020': -3655,
            '2019': -5546,
            '2018': -7329,
            '2017': -11576,
            '2016': -14099,
        },
        {
            'color': 'darkred',
            'name': 'Mazda CX-5',
            '2021': 0,
            '2020': -3984,
            '2019': -3318,
            '2018': -4598,
            '2017': -7170,
            '2016': -7853,
        },
        {
            'color': 'green',
            'name': 'Subaru Crosstrek',
            '2021': 0,
            '2020': -547,
            '2019': -389,
            '2018': -1689,
        },
        {
            'color': 'green',
            'name': 'Subaru Outback',
            '2021': 0,
            '2020': -1088,
            '2019': -3140,
            '2018': -4747,
            '2017': -7193,
            '2016': -7998,
        },
        {
            'color': 'green',
            'name': 'Subaru Forrester',
            '2021': 0,
            '2020': 36,
            '2019': -2487,
            '2018': -2948,
            '2017': -5316,
            '2016': -8447,
        },
        {
            'color': 'red',
            'name': 'Toyota Rav4',
            '2021': 0,
            '2020': -912,
            '2019': -1884,
            '2018': -4502,
            '2017': -6106,
            '2016': -7687,
        },
        {
            'color': 'red',
            'name': 'Toyota Rav4 Hybrid',
            '2021': 0,
            '2020': -2649,
            '2019': -2131,
            '2018': -4551,
            '2017': -7526,
        },
        {
            'color': 'purple',
            'name': 'Kia Sorento',
            '2021': 0,
            '2020': -3931,
            '2019': -4971,
            '2018': -8010,
            '2017': -9200,
            '2016': -10317,
        },
        {
            'color': 'purple',
            'name': 'Kia Sportage',
            '2021': 0,
            '2020': -4737,
            '2019': -5370,
            '2018': -6629,
            '2017': -7525,
            '2016': -9344,
        },
        {
            'color': 'lightblue',
            'name': 'Hyundai Santa Fe',
            '2021': 0,
            '2020': -3155,
            '2019': -3640,
            '2018': -8624,
            '2017': -11684,
            '2016': -15196,
        },
        {
            'color': 'lightblue',
            'name': 'Hyundai Tuscon',
            '2021': 0,
            '2020': -2848,
            '2019': -3780,
            '2018': -4749,
            '2017': -6316,
            '2016': -7716,
        },
        {
            'color': 'gray',
            'name': 'Honda CR-V',
            '2021': 0,
            '2020': -2229,
            '2019': -2007,
            '2018': -3969,
            '2017': -5362,
            '2016': -8110,
        },
        {
            'color': 'gray',
            'name': 'Honda HR-V',
            '2021': 0,
            '2020': -1878,
            '2019': -2469,
            '2018': -3713,
            '2017': -4858,
            '2016': -5946,
        },
    ]
    context = []
    for kar in kars:
        car = {}
        car['label'] = kar['name']
        price_data_by_year = [kar['2021'], kar['2020'], kar['2019']]
        if '2018' in kar:
            price_data_by_year.append(kar['2018'])
        if '2017' in kar:
            price_data_by_year.append(kar['2017'])
        if '2016' in kar:
            price_data_by_year.append(kar['2016'])
        car['data'] = price_data_by_year
        car['color'] = kar['color']
        context.append(car)
    return render(request, 'cars/index.html', {'datasets': context})


def value_lost_plus_gas(request):
    kars = [
        {
            'color': 'gold',
            'name': 'Chevrolet Trax',
            '2021': 0,
            '2020': -3579,
            '2019': -7383,
            '2018': -9271,
            '2017': -11648,
            '2016': -14530,
        },
        {
            'color': 'gold',
            'name': 'Chevrolet Equinox',
            '2021': 0,
            '2020': -6754,
            '2019': -8607,
            '2018': -10251,
            '2017': -14436,
            '2016': -17460,
        },
        {
            'color': 'gold',
            'name': 'Chevrolet Traverse',
            '2021': 0,
            '2020': -3010,
            '2019': -7273,
            '2018': -9492,
            '2017': -18513,
            '2016': -22716,
        },
        {
            'color': 'blue',
            'name': 'Ford Edge',
            '2021': 0,
            '2020': -7704,
            '2019': -11091,
            '2018': -17304,
            '2017': -19983,
            '2016': -23666,
        },
        {
            'color': 'blue',
            'name': 'Ford Escape',
            '2021': 0,
            '2020': -2442,
            '2019': -7968,
            '2018': -10953,
            '2017': -14825,
            '2016': -17979,
        },
        {
            'color': 'blue',
            'name': 'Ford EcoSport',
            '2021': 0,
            '2020': -6191,
            '2019': -7241,
            '2018': -8267
        },
        {
            'color': 'black',
            'name': 'VW Tiguan',
            '2021': 0,
            '2020': -4855,
            '2019': -7946,
            '2018': -11079,
            '2017': -17031,
            '2016': -20621,
        },
        {
            'color': 'darkred',
            'name': 'Mazda CX-5',
            '2021': 0,
            '2020': -5055,
            '2019': -5461,
            '2018': -7931,
            '2017': -11614,
            '2016': -13025,
        },
        {
            'color': 'green',
            'name': 'Subaru Crosstrek',
            '2021': 0,
            '2020': -1747,
            '2019': -2458,
            '2018': -4792,
            '2017': -4615,
            '2016': -5769,
        },
        {
            'color': 'green',
            'name': 'Subaru Outback',
            '2021': 0,
            '2020': -2122,
            '2019': -5283,
            '2018': -7961,
            '2017': -11479,
            '2016': -13355,
        },
        {
            'color': 'green',
            'name': 'Subaru Forrester',
            '2021': 0,
            '2020': -998,
            '2019': -4556,
            '2018': -6162,
            '2017': -9602,
            '2016': -14003,
        },
        {
            'color': 'red',
            'name': 'Toyota Rav4',
            '2021': 0,
            '2020': -1912,
            '2019': -3884,
            '2018': -8102,
            '2017': -10906,
            '2016': -13687,
        },
        {
            'color': 'red',
            'name': 'Toyota Rav4 Hybrid',
            '2021': 0,
            '2020': -3399,
            '2019': -3631,
            '2018': -7364,
            '2017': -11276
        },
        {
            'color': 'purple',
            'name': 'Kia Sorento',
            '2021': 0,
            '2020': -5131,
            '2019': -7371,
            '2018': -11760,
            '2017': -14200,
            '2016': -16567,
        },
        {
            'color': 'purple',
            'name': 'Kia Sportage',
            '2021': 0,
            '2020': -5891,
            '2019': -7770,
            '2018': -10229,
            '2017': -12325,
            '2016': -15594,
        },
        {
            'color': 'lightblue',
            'name': 'Hyundai Santa Fe',
            '2021': 0,
            '2020': -4355,
            '2019': -6040,
            '2018': -12910,
            '2017': -17398,
            '2016': -22339,
        },
        {
            'color': 'lightblue',
            'name': 'Hyundai Tuscon',
            '2021': 0,
            '2020': -4048,
            '2019': -6088,
            '2018': -8211,
            '2017': -10931,
            '2016': -13485,
        },
        {
            'color': 'gray',
            'name': 'Honda CR-V',
            '2021': 0,
            '2020': -3229,
            '2019': -4229,
            '2018': -7302,
            '2017': -9806,
            '2016': -13666,
        },
        {
            'color': 'gray',
            'name': 'Honda HR-V',
            '2021': 0,
            '2020': -2878,
            '2019': -4469,
            '2018': -6616,
            '2017': -8729,
            '2016': -10785,
        },
    ]
    context = []
    for kar in kars:
        car = {}
        car['label'] = kar['name']
        price_data_by_year = [kar['2021'], kar['2020'], kar['2019']]
        if '2018' in kar:
            price_data_by_year.append(kar['2018'])
        if '2017' in kar:
            price_data_by_year.append(kar['2017'])
        if '2016' in kar:
            price_data_by_year.append(kar['2016'])
        car['data'] = price_data_by_year
        car['color'] = kar['color']
        context.append(car)
    return render(request, 'cars/index.html', {'datasets': context})


def percent_value_retained(request):
    kars = [
        {'color': 'gold', 'name': 'Chevrolet Trax', '2021': 1, '2020': 0.84, '2019': 0.70, '2018': 0.64, '2017': 0.57, '2016':	0.46},
        {'color': 'gold', 'name': 'Chevrolet Equinox', '2021': 1, '2020': 0.77, '2019': 0.71, '2018': 0.66, '2017': 0.55, '2016':	0.47},
        {'color': 'gold', 'name': 'Chevrolet Traverse', '2021': 1, '2020': 0.92, '2019': 0.81, '2018': 0.76, '2017': 0.54, '2016':	0.45},
        {'color': 'blue', 'name': 'Ford Edge', '2021': 1, '2020': 0.78, '2019': 0.68, '2018': 0.54, '2017': 0.48, '2016':	0.40},
        {'color': 'blue', 'name': 'Ford Escape', '2021': 1, '2020': 0.91, '2019': 0.74, '2018': 0.64, '2017': 0.54, '2016':	0.46},
        {'color': 'blue', 'name': 'Ford EcoSport', '2021': 1, '2020': 0.73, '2019': 0.69, '2018': 0.67},
        {'color': 'black', 'name': 'VW Tiguan', '2021': 1, '2020': 0.82, '2019': 0.72, '2018': 0.63, '2017': 0.47, '2016':	0.38},
        {'color': 'darkred', 'name': 'Mazda CX-5', '2021': 1, '2020': 0.82, '2019': 0.80, '2018': 0.72, '2017': 0.61, '2016':	0.56},
        {'color': 'green', 'name': 'Subaru Crosstrek', '2021': 1, '2020': 0.93, '2019': 0.90, '2018': 0.81},
        {'color': 'green', 'name': 'Subaru Outback', '2021': 1, '2020': 0.92, '2019': 0.81, '2018': 0.73, '2017': 0.62, '2016':	0.56},
        {'color': 'green', 'name': 'Subaru Forester', '2021': 1, '2020': 0.96, '2019': 0.83, '2018': 0.77, '2017': 0.66, '2016':	0.52},
        {'color': 'red', 'name': 'Toyota Rav4', '2021': 1, '2020': 0.93, '2019': 0.87, '2018': 0.73, '2017': 0.64, '2016':	0.57},
        {'color': 'red', 'name': 'Toyota Rav4 Hybrid', '2021': 1, '2020': 0.88, '2019': 0.88, '2018': 0.76, '2017': 0.63},
        {'color': 'purple', 'name': 'Kia Sorento', '2021': 1, '2020': 0.83, '2019': 0.77, '2018': 0.65, '2017': 0.58, '2016':	0.52},
        {'color': 'purple', 'name': 'Kia Sportage', '2021': 1, '2020': 0.78, '2019': 0.72, '2018': 0.64, '2017': 0.58, '2016':	0.48},
        {'color': 'lightblue', 'name': 'Hyundai Santa Fe', '2021': 1, '2020': 0.85, '2019': 0.80, '2018': 0.65, '2017': 0.55, '2016':	0.43},
        {'color': 'lightblue', 'name': 'Hyundai Tucson', '2021': 1, '2020': 0.85, '2019': 0.78, '2018': 0.70, '2017': 0.62, '2016':	0.55},
        {'color': 'gray', 'name': 'Honda CR-V', '2021': 1, '2020': 0.88, '2019': 0.85, '2018': 0.75, '2017': 0.67, '2016':	0.55},
        {'color': 'gray', 'name': 'Honda HR-V', '2021': 1, '2020': 0.88, '2019': 0.81, '2018': 0.73, '2017': 0.66, '2016':	0.59},
    ]
    context = []
    for kar in kars:
        car = {}
        car['label'] = kar['name']
        price_data_by_year = [kar['2021'], kar['2020'], kar['2019']]
        if '2018' in kar:
            price_data_by_year.append(kar['2018'])
        if '2017' in kar:
            price_data_by_year.append(kar['2017'])
        if '2016' in kar:
            price_data_by_year.append(kar['2016'])
        car['data'] = price_data_by_year
        car['color'] = kar['color']
        context.append(car)
    return render(request, 'cars/index.html', {'datasets': context})
