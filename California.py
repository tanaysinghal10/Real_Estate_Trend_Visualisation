import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import column

def California():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year
    states = set(State_time_series[
                     ~State_time_series['ZHVI_AllHomes'].isnull() &
                     ~State_time_series['Sale_Prices'].isnull()
                     ]['RegionName'].values)

    State_time_series_year = State_time_series[State_time_series['RegionName'].isin(states)].copy()
    highest_cost_states = State_time_series_year[['RegionName', 'ZHVI_AllHomes']].groupby(
        'RegionName').max().sort_values(by=['ZHVI_AllHomes'], ascending=False)[:5].index.values.tolist()
    State_time_series_year = State_time_series_year[
        State_time_series_year.RegionName.isin(highest_cost_states)]
    State_time_series_year.year = State_time_series_year.Date.dt.year
    States_year_SalePrices = \
        State_time_series_year.groupby([State_time_series_year.year, State_time_series_year.RegionName])[
            'ZHVI_AllHomes'].mean().dropna().reset_index(name='SoldPrice')

    p = figure(title="House Median Sale Prices from 1996 to 2017 in the US states", plot_width=700,
               plot_height=500)
    # x_axis_type = "datetime"
    # name of the x-axis
    p.xaxis.axis_label = 'Year'

    # name of the y-axis
    p.yaxis.axis_label = 'SoldPrice'
    grp_1 = States_year_SalePrices[States_year_SalePrices["RegionName"] == "California"]

    cal_year = grp_1['year'].tolist()
    cal_sp = grp_1['SoldPrice'].tolist()

    x_axis_coordinates = np.array(cal_year)
    y_axis_coordinates = np.array(cal_sp)
    color = "brown"
    legend_label = "California"
    p.left[0].formatter.use_scientific = False
    p.line(x_axis_coordinates,
           y_axis_coordinates,
           color=color,
           legend_label=legend_label)
    return p

def Cal_4():
    State_time_series = pd.read_csv("State_time_series.csv", parse_dates=True)
    State_time_series.Date = pd.to_datetime(State_time_series.Date)
    State_time_series['year'] = State_time_series.Date.dt.year
    states = set(State_time_series[
                     ~State_time_series['ZHVI_AllHomes'].isnull() &
                     ~State_time_series['Sale_Prices'].isnull()
                     ]['RegionName'].values)

    State_time_series_year = State_time_series[State_time_series['RegionName'].isin(states)].copy()
    highest_cost_states = State_time_series_year[['RegionName', 'ZHVI_AllHomes']].groupby(
        'RegionName').max().sort_values(by=['ZHVI_AllHomes'], ascending=False)[:5].index.values.tolist()
    State_time_series_year = State_time_series_year[
        State_time_series_year.RegionName.isin(highest_cost_states)]
    State_time_series_year.year = State_time_series_year.Date.dt.year
    States_year_SalePrices = \
    State_time_series_year.groupby([State_time_series_year.Date, State_time_series_year.RegionName])[
        'Sale_Prices'].mean().dropna().reset_index(name='Sale_Prices')
    PriceDF = States_year_SalePrices.pivot(index='Date', columns='RegionName',
                                           values='Sale_Prices').dropna()  # .plot(figsize=(15,8))#, color=colors, legend=False)

    t0 = PriceDF.index
    t1 = pd.date_range(pd.to_datetime('30/01/2009'), pd.to_datetime('2017-08-31'), freq='A')
    t2 = pd.date_range(pd.to_datetime('30/01/2009', dayfirst=True),
                       pd.to_datetime('2016-08-31', dayfirst=True), freq='M')
    t3 = pd.date_range(pd.to_datetime('30/01/2009', dayfirst=True),
                       pd.to_datetime('2015-08-31', dayfirst=True), freq='Q')

    df1 = PriceDF.reindex(index=t0, columns=highest_cost_states).reset_index()
    df2 = PriceDF.reindex(index=t1, columns=highest_cost_states).reset_index()
    df3 = PriceDF.reindex(index=t2, columns=highest_cost_states).reset_index()
    df4 = PriceDF.reindex(index=t3, columns=highest_cost_states).reset_index()

    time_daily = df1["Date"].to_list()
    time_yearly = df2["index"].to_list()
    time_monthly = df3["index"].to_list()
    time_quarterly = df4["index"].to_list()

    year = time_daily
    per = df1["California"].to_list()
    color = "orange"
    legend = 'California'

    p1 = figure(title="Increase in House SalePrice for Top US states as shown by Time Frequency",
                x_axis_type="datetime", width=600, plot_height=200)

    p1.xaxis.axis_label = 'time'

    p1.yaxis.axis_label = 'Saleprice Daily'

    # year, price, color, legend
    x_axis_coordinates = np.array(year)
    y_axis_coordinates = np.array(per)
    color = color
    legend_label = legend

    p1.line(x_axis_coordinates, y_axis_coordinates,
            color=color, legend_label=legend_label)

    p1.legend.click_policy = "hide"
    p1.legend.label_text_font_size = "7pt"
    p1.left[0].formatter.use_scientific = False
    p1.add_layout(p1.legend[0], 'right')

    year = time_yearly
    per = df2["California"].to_list()
    color = "orange"
    legend = 'California'

    p2 = figure(x_axis_type="datetime", width=600, plot_height=200, title=None)

    p2.xaxis.axis_label = 'time'

    p2.yaxis.axis_label = 'Saleprice Yearly'

    x_axis_coordinates = np.array(year)
    y_axis_coordinates = np.array(per)
    color = color
    legend_label = legend

    p2.line(x_axis_coordinates, y_axis_coordinates,
            color=color, legend_label=legend_label)

    p2.legend.click_policy = "hide"
    p2.legend.label_text_font_size = "7pt"
    p2.left[0].formatter.use_scientific = False
    p2.add_layout(p2.legend[0], 'right')

    year = time_monthly
    per = df3["California"].to_list()
    color = "orange"
    legend = 'California'

    p3 = figure(x_axis_type="datetime", width=600, plot_height=200, title=None)

    p3.xaxis.axis_label = 'time'

    p3.yaxis.axis_label = 'Saleprice Monthly'

    x_axis_coordinates = np.array(year)
    y_axis_coordinates = np.array(per)
    color = color
    legend_label = legend

    p3.line(x_axis_coordinates, y_axis_coordinates,
            color=color, legend_label=legend_label)

    p3.legend.click_policy = "hide"
    p3.legend.label_text_font_size = "7pt"
    p3.left[0].formatter.use_scientific = False
    p3.add_layout(p3.legend[0], 'right')

    year = time_quarterly
    per = df4["California"].to_list()
    color = "orange"
    legend = 'California'

    p4 = figure(x_axis_type="datetime", width=600, plot_height=200, title=None)

    p4.xaxis.axis_label = 'time'

    p4.yaxis.axis_label = 'Saleprice Quartertly'

    x_axis_coordinates = np.array(year)
    y_axis_coordinates = np.array(per)
    color = color
    legend_label = legend

    p4.line(x_axis_coordinates, y_axis_coordinates,
            color=color, legend_label=legend_label)

    p4.legend.click_policy = "hide"
    p4.legend.label_text_font_size = "7pt"
    p4.left[0].formatter.use_scientific = False
    p4.add_layout(p4.legend[0], 'right')

    # put all the plots in a VBox
    p = column(p1, p2, p3, p4)
    return p