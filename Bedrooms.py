import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import column




def B_1():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year
    dfsq1 = State_time_series.groupby(State_time_series['year'])[
        'MedianListingPricePerSqft_1Bedroom'].mean().dropna().to_frame().reset_index()
    sq1lst = dfsq1['year'].to_list()
    price1 = dfsq1['MedianListingPricePerSqft_1Bedroom'].to_list()

    p = figure(title="Median Listing Prices Per Sqft W.r.t Number of Bedrooms", plot_width=700,
               plot_height=500)

    p.xaxis.axis_label = 'Year'

    # name of the y-axis
    p.yaxis.axis_label = 'Median Listing Prices Per Sqft'

    x_axis_coordinates = np.array(sq1lst)
    y_axis_coordinates = np.array(price1)
    color = "brown"
    legend_label = "1 Bedroom"
    p.line(x_axis_coordinates,
           y_axis_coordinates,
           color=color,
           legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p


def B_2():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year
    dfsq2 = State_time_series.groupby(State_time_series['year'])[
        'MedianListingPricePerSqft_2Bedroom'].mean().dropna().reset_index()

    sq2lst = dfsq2['year'].to_list()

    price2 = dfsq2['MedianListingPricePerSqft_2Bedroom'].to_list()

    p = figure(title="Median Listing Prices Per Sqft W.r.t Number of Bedrooms", plot_width=700,
               plot_height=500)

    p.xaxis.axis_label = 'Year'

    # name of the y-axis
    p.yaxis.axis_label = 'Median Listing Prices Per Sqft'

    x_axis_coordinates = np.array(sq2lst)
    y_axis_coordinates = np.array(price2)
    color = "blue"
    legend_label = "2 Bedroom"
    p.line(x_axis_coordinates,
           y_axis_coordinates,
           color=color,
           legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def B_3():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    df_3B = State_time_series.groupby(State_time_series['year'])[
        'MedianRentalPricePerSqft_3Bedroom'].mean().dropna().to_frame().reset_index()

    y_3b = df_3B["year"].to_list()

    price_3b = df_3B['MedianRentalPricePerSqft_3Bedroom']

    p = figure(title="Real Estate Rental Prices Per SquareFoot", plot_width=700, plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

    x_axis_coordinates = np.array(y_3b)
    y_axis_coordinates = np.array(price_3b)
    color = "orange"
    legend_label = '3 Bedroom'

    p.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p


def B_4():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year
    dfsq4 = State_time_series.groupby(State_time_series['year'])[
        'MedianListingPricePerSqft_4Bedroom'].mean().dropna().reset_index()

    sq4lst = dfsq4['year'].to_list()

    price4 = dfsq4['MedianListingPricePerSqft_4Bedroom'].to_list()

    p = figure(title="Median Listing Prices Per Sqft W.r.t Number of Bedrooms", plot_width=700,
               plot_height=500)

    p.xaxis.axis_label = 'Year'

    # name of the y-axis
    p.yaxis.axis_label = 'Median Listing Prices Per Sqft'

    x_axis_coordinates = np.array(sq4lst)
    y_axis_coordinates = np.array(price4)
    color = "yellow"
    legend_label = "MedianListingPricePerSqft_4Bedroom"
    p.line(x_axis_coordinates,
           y_axis_coordinates,
           color=color,
           legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def B_5():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year
    dfsq5 = State_time_series.groupby(State_time_series['year'])[
        'MedianListingPricePerSqft_5BedroomOrMore'].mean().dropna().reset_index()

    sq5lst = dfsq5['year'].to_list()

    price5 = dfsq5['MedianListingPricePerSqft_5BedroomOrMore'].to_list()

    p = figure(title="Median Listing Prices Per Sqft W.r.t Number of Bedrooms", plot_width=700,
               plot_height=500)

    p.xaxis.axis_label = 'Year'

    # name of the y-axis
    p.yaxis.axis_label = 'Median Listing Prices Per Sqft'

    x_axis_coordinates = np.array(sq5lst)
    y_axis_coordinates = np.array(price5)
    color = "deeppink"
    legend_label = "5 Bedroom"
    p.line(x_axis_coordinates,
           y_axis_coordinates,
           color=color,
           legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p


def DT():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    dfsqDT = State_time_series.groupby(State_time_series['year'])[
        'MedianListingPricePerSqft_DuplexTriplex'].mean().dropna().reset_index()

    sqDTlst = dfsqDT['year'].to_list()

    priceDT = dfsqDT['MedianListingPricePerSqft_DuplexTriplex'].to_list()

    p = figure(title="Median Listing Prices Per Sqft W.r.t Number of Bedrooms", plot_width=700,
               plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Listing Prices Per Sqft'

    x_axis_coordinates = np.array(sqDTlst)
    y_axis_coordinates = np.array(priceDT)
    color = "seagreen"
    legend_label = "Duplex-Triplex"
    p.line(x_axis_coordinates,
           y_axis_coordinates,
           color=color,
           legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def SFR():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    dfsqSFR = State_time_series.groupby(State_time_series['year'])[
        'MedianListingPricePerSqft_SingleFamilyResidence'].mean().dropna().reset_index()

    sqSFRlst = dfsqSFR['year'].to_list()

    priceSFR = dfsqSFR['MedianListingPricePerSqft_SingleFamilyResidence'].to_list()

    p = figure(title="Median Listing Prices Per Sqft W.r.t Number of Bedrooms", plot_width=700,
               plot_height=500)

    p.xaxis.axis_label = 'Year'

    # name of the y-axis
    p.yaxis.axis_label = 'Median Listing Prices Per Sqft'

    x_axis_coordinates = np.array(sqSFRlst)
    y_axis_coordinates = np.array(priceSFR)
    color = "magenta"
    legend_label = "Single Family Residence"

    p.line(x_axis_coordinates,
           y_axis_coordinates,
           color=color,
           legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def B_1_RP():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    df_1B = State_time_series.groupby(State_time_series['year'])[
        'MedianRentalPricePerSqft_1Bedroom'].mean().dropna().to_frame().reset_index()

    y_1b = df_1B["year"].to_list()

    price_1b = df_1B['MedianRentalPricePerSqft_1Bedroom']

    p = figure(title="Real Estate Rental Prices Per SquareFoot", plot_width=700, plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

    x_axis_coordinates = np.array(y_1b)
    y_axis_coordinates = np.array(price_1b)
    color = "brown"
    legend_label = '1 Bedroom'

    p.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def B_2_RP():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    df_2B = State_time_series.groupby(State_time_series['year'])[
        'MedianRentalPricePerSqft_2Bedroom'].mean().dropna().to_frame().reset_index()

    y_2b = df_2B["year"].to_list()

    price_2b = df_2B['MedianRentalPricePerSqft_2Bedroom']

    p = figure(title="Real Estate Rental Prices Per SquareFoot", plot_width=700, plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

    x_axis_coordinates = np.array(y_2b)
    y_axis_coordinates = np.array(price_2b)
    color = "blue"
    legend_label = '2 Bedroom'

    p.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def B_3_RP():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    df_3B = State_time_series.groupby(State_time_series['year'])[
        'MedianRentalPricePerSqft_3Bedroom'].mean().dropna().to_frame().reset_index()

    y_3b = df_3B["year"].to_list()

    price_3b = df_3B['MedianRentalPricePerSqft_3Bedroom']

    p = figure(title="Real Estate Rental Prices Per SquareFoot", plot_width=700, plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

    x_axis_coordinates = np.array(y_3b)
    y_axis_coordinates = np.array(price_3b)
    color = "orange"
    legend_label = '3 Bedroom'

    p.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def B_4_RP():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    df_4B = State_time_series.groupby(State_time_series['year'])[
        'MedianRentalPricePerSqft_4Bedroom'].mean().dropna().to_frame().reset_index()

    y_4b = df_4B["year"].to_list()

    price_4b = df_4B['MedianRentalPricePerSqft_4Bedroom']

    p = figure(title="Real Estate Rental Prices Per SquareFoot", plot_width=700, plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

    x_axis_coordinates = np.array(y_4b)
    y_axis_coordinates = np.array(price_4b)
    color = "yellow"
    legend_label = '4 Bedroom'

    p.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def B_5_RP():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    df_5B = State_time_series.groupby(State_time_series['year'])[
        'MedianRentalPricePerSqft_5BedroomOrMore'].mean().dropna().to_frame().reset_index()

    y_5b = df_5B["year"].to_list()

    price_5b = df_5B['MedianRentalPricePerSqft_5BedroomOrMore']

    p = figure(title="Real Estate Rental Prices Per SquareFoot", plot_width=700, plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

    x_axis_coordinates = np.array(y_5b)
    y_axis_coordinates = np.array(price_5b)
    color = "deeppink"
    legend_label = '5 Bedroom'

    p.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def DT_RP():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    df_dt = State_time_series.groupby(State_time_series['year'])[
        'MedianRentalPricePerSqft_DuplexTriplex'].mean().dropna().to_frame().reset_index()

    y_dt = df_dt["year"].to_list()

    price_dt = df_dt['MedianRentalPricePerSqft_DuplexTriplex']

    p = figure(title="Real Estate Rental Prices Per SquareFoot", plot_width=700, plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

    x_axis_coordinates = np.array(y_dt)
    y_axis_coordinates = np.array(price_dt)
    color = "seagreen"
    legend_label = 'Duplex-Triplex'

    p.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p

def SFR_RP():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year

    df_sfr = State_time_series.groupby(State_time_series['year'])[
        'MedianRentalPricePerSqft_SingleFamilyResidence'].mean().dropna().to_frame().reset_index()

    y_sfr = df_sfr["year"].to_list()

    price_str = df_sfr['MedianRentalPricePerSqft_SingleFamilyResidence']

    p = figure(title="Real Estate Rental Prices Per SquareFoot", plot_width=700, plot_height=500)

    p.xaxis.axis_label = 'Year'

    p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

    x_axis_coordinates = np.array(y_sfr)
    y_axis_coordinates = np.array(price_str)
    color = "magenta"
    legend_label = 'Single Family Residence'

    p.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

    p.legend.click_policy = "hide"
    p.legend.label_text_font_size = "7pt"
    p.left[0].formatter.use_scientific = False
    p.add_layout(p.legend[0], 'right')
    return p


