import os  # added
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
from flask import render_template
from bokeh.embed import components
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, output_file,show
from bokeh.layouts import column
from datetime import datetime
from bokeh.models import CategoricalColorMapper, Legend
import NewJersey
import Mass
import California
import Columbia
import Washinton
import Bedrooms

app = Flask(__name__)


@app.route('/')
def form():

    return render_template('home.html')



@app.route('/next',methods = ['GET','POST'])
def index():
   
    if request.method == 'GET':
        p = figure(width=650, height=380)
        p.image_url(url=['https://cdn.corporatefinanceinstitute.com/assets/real-estate-1024x614.jpeg'], x=0, y=1, w=0.8, h=0.6)
        demo_script_code,chart_code = components(p)
        return render_template('view_temp.html',chart_code = chart_code,demo_script_code = demo_script_code)

    elif request.method =='POST':

        choice = request.form["region"]
        house = request.form["house_type"]
        var1 = request.form["Choice"]

        # if choice == "California" and house == "1 Bedroom":
        #     while True:
        #         if var1 == "Price Vs State":
        #             p = California.California()
        #
        #         elif var1 == "Price vs Area(Square foot)":
        #             p = Bedrooms.B_1()
        #
        #         elif var1 == "Rental price Vs Area(Square foot)":
        #             p = Bedrooms.B_1_RP()
        #
        #         elif var1 == "Increase in House SalePrice as shown by Time Frequency":
        #             p = California.Cal_4()
        #
        #         elif var1 == "New Choice":
        #
        #             p = figure(width=650, height=380)
        #             p.image_url(url=['https://cdn.corporatefinanceinstitute.com/assets/real-estate-1024x614.jpeg'], x=0,
        #                         y=1, w=0.8, h=0.6)
        #             break
        #         # demo_script_code, chart_code = components(p)
        #         # return render_template('view_temp.html', chart_code=chart_code, demo_script_code=demo_script_code)

        if var1 == "Price Vs State":


            if choice == "California":
                p = California.California()

            elif choice == "Massachusetts":
                p = Mass.Massachusetts()

            elif choice == "New Jersey":
                p = NewJersey.New_jersey()

            elif choice == "District of Columbia":
                p = Columbia.Columbia()

            elif choice == "Washington":
                p = Washinton.Wash()


        elif var1 == "Price vs Area(Square foot)":

            if house == "1 Bedroom":
                p = Bedrooms.B_1()

            elif house == "2 Bedroom":
                p = Bedrooms.B_2()

            elif house == "3 Bedroom":
                p = Bedrooms.B_3()

            elif house == "4 Bedroom":
                p = Bedrooms.B_4()

            elif house == "5 Bedroom":
                p = Bedrooms.B_5()

            elif house == "Duplex-Triplex":
                p = Bedrooms.DT()

            elif house == "Single Family Residence":
                p = Bedrooms.SFR()

        elif var1 == "Rental price Vs Area(Square foot)":

            if house == "1 Bedroom":
                p = Bedrooms.B_1_RP()

            elif house == "2 Bedroom":
                p = Bedrooms.B_2_RP()

            elif house == "3 Bedroom":
                p = Bedrooms.B_3_RP()

            elif house == "4 Bedroom":
                p = Bedrooms.B_4_RP()

            elif house == "5 Bedroom":
                p = Bedrooms.B_5_RP()

            elif house == "Duplex-Triplex":
                p = Bedrooms.DT_RP()

            elif house == "Single Family Residence":
                p = Bedrooms.SFR_RP()


        elif var1 == "Increase in House SalePrice as shown by Time Frequency":

            if choice == "California":
                p = California.Cal_4()

            elif choice == "Massachusetts":
                p = Mass.Mass_4()

            elif choice == "New Jersey":
                p = NewJersey.New_Jersey_4()

            elif choice == "District of Columbia":
                p = Columbia.Colum_4()

            elif choice == "Washington":
                p = Washinton.Wash_4()


        demo_script_code,chart_code = components(p)
        return render_template('view_temp.html',chart_code = chart_code,demo_script_code = demo_script_code)



@app.route('/final', methods = ['GET','POST'])

def index2():
   
    if request.method == 'GET':
        p = figure(width=650, height=380)
        p.image_url(url=['https://cdn.corporatefinanceinstitute.com/assets/real-estate-1024x614.jpeg'], x=0, y=1, w=0.8, h=0.6)
        demo_script_code,chart_code = components(p)
        return render_template('final_comparison.html',chart_code = chart_code,demo_script_code = demo_script_code)
    elif request.method =='POST':
        # print("post request made")
        # choice = request.form["region"]
        # house = request.form["house_type"]
        var1 = request.form["Choice"]
        if var1 == "Price Vs State":
            State_time_series=pd.read_csv("State_time_series.csv",parse_dates=True)
            State_time_series.Date=pd.to_datetime(State_time_series.Date)
            State_time_series['year'] = State_time_series.Date.dt.year
            states = set(State_time_series[
                        ~State_time_series['ZHVI_AllHomes'].isnull() &
                        ~State_time_series['Sale_Prices'].isnull()
                                        ]['RegionName'].values)

            State_time_series_year = State_time_series[State_time_series['RegionName'].isin(states)].copy()
            highest_cost_states = State_time_series_year[['RegionName', 'ZHVI_AllHomes']].groupby('RegionName').max().sort_values(by=['ZHVI_AllHomes'], ascending=False)[:5].index.values.tolist()
            State_time_series_year=State_time_series_year[State_time_series_year.RegionName.isin(highest_cost_states)]
            State_time_series_year.year = State_time_series_year.Date.dt.year   
            States_year_SalePrices=State_time_series_year.groupby([State_time_series_year.year,State_time_series_year.RegionName])['ZHVI_AllHomes'].mean().dropna().reset_index(name='SoldPrice')

            grp_1 = States_year_SalePrices[States_year_SalePrices["RegionName"] == "California"]
            cal_year=grp_1['year'].tolist()
            cal_sp=grp_1['SoldPrice'].tolist()
            grp_2 = States_year_SalePrices[States_year_SalePrices["RegionName"] == "Massachusetts"]
            grp_3 = States_year_SalePrices[States_year_SalePrices["RegionName"] == "NewJersey"]
            grp_4 = States_year_SalePrices[States_year_SalePrices["RegionName"] == "DistrictofColumbia"]
            grp_5 = States_year_SalePrices[States_year_SalePrices["RegionName"] == "Washington"]
            Mas_year=grp_2['year'].tolist()
            Mas_sp=grp_2['SoldPrice'].tolist()
            Newj_year=grp_3['year'].tolist()
            Newj_sp=grp_3['SoldPrice'].tolist()
            Dist_year=grp_4['year'].tolist()
            Dist_sp=grp_4['SoldPrice'].tolist()
            Wash_year=grp_5['year'].tolist()
            Wash_sp=grp_5['SoldPrice'].tolist()
            p = figure(title = "House Median Sale Prices from 1996 to 2017 in the US states",plot_width = 700, plot_height = 500)
            #x_axis_type = "datetime"
                        # name of the x-axis
            p.xaxis.axis_label = 'Year'

                        # name of the y-axis
            p.yaxis.axis_label = 'SoldPrice'

                        
            x_axis_coordinates = np.array(cal_year)
            y_axis_coordinates = np.array(cal_sp)
            color = "brown"
            legend_label = "California"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(Mas_year)
            y_axis_coordinates = np.array(Mas_sp)
            color = "blue"
            legend_label = "Massachusetts"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(Newj_year)
            y_axis_coordinates = np.array(Newj_sp)
            color = "orange"
            legend_label = "New Jersey"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
                    
            x_axis_coordinates = np.array(Dist_year)
            y_axis_coordinates = np.array(Dist_sp)
            color = "yellow"
            legend_label = "District of Columbia"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
                    
            x_axis_coordinates = np.array(Wash_year)
            y_axis_coordinates = np.array(Wash_sp)
            color = "deeppink"
            legend_label = "Washington"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
                    
            #p.legend.location = "top_left"
            p.add_layout(p.legend[0], 'right')
            p.left[0].formatter.use_scientific = False
            p.legend.click_policy="hide"
 
            
        
        elif var1 == "Price Vs Tier":
            State_time_series = pd.read_csv("State_time_series.csv",parse_dates=True)
            State_time_series.Date = pd.to_datetime(State_time_series.Date)
            State_time_series['year'] = State_time_series.Date.dt.year

            df_top = State_time_series.groupby(State_time_series['year'])['ZHVI_TopTier'].median().to_frame().reset_index()
            df_middle = State_time_series.groupby(State_time_series['year'])['ZHVI_MiddleTier'].median().to_frame().reset_index()
            df_bottom = State_time_series.groupby(State_time_series['year'])['ZHVI_BottomTier'].median().to_frame().reset_index()

            y_top_tier = df_top["year"].to_list() 
            y_middle_tier = df_middle["year"].to_list() 
            y_bottom_tier = df_bottom["year"].to_list()  

            zhvi_top_tier = df_top["ZHVI_TopTier"].to_list() 
            zhvi_middle_tier = df_middle["ZHVI_MiddleTier"].to_list() 
            zhvi_bottom_tier = df_bottom["ZHVI_BottomTier"].to_list()

            y_final = [y_top_tier,y_middle_tier, y_bottom_tier]
            zhvi_final = [zhvi_top_tier, zhvi_middle_tier, zhvi_bottom_tier]
            colors = ["red", "blue", "green"]
            legends_final = ["Top Tier", "Middle Tier", "Bottom Tier"]

            p = figure(title = "Real Estate Properties ZHVI for different Tiers in US",plot_width = 700, plot_height = 500)
    
            p.xaxis.axis_label = 'Year'

            p.yaxis.axis_label = 'ZHVI Values'

            # year, price, color, legend
            for year, zhvi, color, legend in zip(y_final, zhvi_final, colors, legends_final):
    
                x_axis_coordinates = np.array(year)
                y_axis_coordinates = np.array(zhvi)
                color = color
                legend_label = legend

                p.line(x_axis_coordinates, y_axis_coordinates,
                    color = color, legend_label = legend_label)

    
            p.legend.click_policy = "hide"
            p.legend.label_text_font_size = "7pt"
            p.left[0].formatter.use_scientific = False
            p.add_layout(p.legend[0], 'right')
            
        elif var1 == "Price vs Area(Square foot)":
            # lst = ["2007-11-23", "2008-11-23","2010-11-23","2012-11-23"]
            # temp = ["Not Prime", "Prime", "Prime", "Prime"]
            # res = [2100, 3100, 1250, 1580]
            # dict1 = {"Date": lst, "Units":temp, "Wealth":res}
            # dict1 = pd.DataFrame(dict1)
            # print(dict1)
            # p = figure(width = 700, height = 500, x_axis_type = "datetime",x_axis_label = "Years", y_axis_label = "Wealth")
            # dict1["Date"] = pd.to_datetime(dict1["Date"])
            # p.line(dict1["Date"],dict1["Wealth"], line_width=2)
            State_time_series=pd.read_csv("State_time_series.csv",parse_dates=True)
            State_time_series.Date=pd.to_datetime(State_time_series.Date)
            State_time_series['year'] = State_time_series.Date.dt.year
            dfsq1=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_1Bedroom'].mean().dropna().to_frame().reset_index()
            dfsq2=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_2Bedroom'].mean().dropna().reset_index()
            dfsq3=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_3Bedroom'].mean().dropna().reset_index()
            dfsq4=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_4Bedroom'].mean().dropna().reset_index()
            dfsq5=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_5BedroomOrMore'].mean().dropna().reset_index()
            dfsqall=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_AllHomes'].mean().dropna().reset_index()
            dfsqcc=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_CondoCoop'].mean().dropna().reset_index()
            dfsqDT=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_DuplexTriplex'].mean().dropna().reset_index()
            dfsqSFR=State_time_series.groupby(State_time_series['year'])['MedianListingPricePerSqft_SingleFamilyResidence'].mean().dropna().reset_index()
            sq1lst=dfsq1['year'].to_list()
            sq2lst=dfsq2['year'].to_list()
            sq3lst=dfsq3['year'].to_list()
            sq4lst=dfsq4['year'].to_list()
            sq5lst=dfsq5['year'].to_list()
            sqalllst=dfsqall['year'].to_list()
            sqcclst=dfsqcc['year'].to_list()
            sqDTlst=dfsqDT['year'].to_list()
            sqSFRlst=dfsqSFR['year'].to_list()
            price1=dfsq1['MedianListingPricePerSqft_1Bedroom'].to_list()
            price2=dfsq2['MedianListingPricePerSqft_2Bedroom'].to_list()
            price3=dfsq3['MedianListingPricePerSqft_3Bedroom'].to_list()
            price4=dfsq4['MedianListingPricePerSqft_4Bedroom'].to_list()
            price5=dfsq5['MedianListingPricePerSqft_5BedroomOrMore'].to_list()
            priceall=dfsqall['MedianListingPricePerSqft_AllHomes'].to_list()
            pricecc=dfsqcc['MedianListingPricePerSqft_CondoCoop'].to_list()
            priceDT=dfsqDT['MedianListingPricePerSqft_DuplexTriplex'].to_list()
            priceSFR=dfsqSFR['MedianListingPricePerSqft_SingleFamilyResidence'].to_list()
            p = figure(title = "Median Listing Prices Per Sqft W.r.t Number of Bedrooms",plot_width = 700, plot_height = 500)
            #x_axis_type = "datetime"
                        # name of the x-axis
            p.xaxis.axis_label = 'Year'

                        # name of the y-axis
            p.yaxis.axis_label = 'Median Listing Prices Per Sqft'

                        
            x_axis_coordinates = np.array(sq1lst)
            y_axis_coordinates = np.array(price1)
            color = "brown"
            legend_label = "1 Bedroom"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(sq2lst)
            y_axis_coordinates = np.array(price2)
            color = "blue"
            legend_label = "2 Bedroom"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(sq3lst)
            y_axis_coordinates = np.array(price3)
            color = "orange"
            legend_label = "3 Bedroom"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
                    
            x_axis_coordinates = np.array(sq4lst)
            y_axis_coordinates = np.array(price4)
            color = "yellow"
            legend_label = "4 Bedroom"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
                    
            x_axis_coordinates = np.array(sq5lst)
            y_axis_coordinates = np.array(price5)
            color = "deeppink"
            legend_label = "5 Bedroom"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(sqalllst)
            y_axis_coordinates = np.array(priceall)
            color = "red"
            legend_label = "All Homes"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(sqcclst)
            y_axis_coordinates = np.array(pricecc)
            color = "goldenrod"
            legend_label = "CondoCoop"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(sqDTlst)
            y_axis_coordinates = np.array(priceDT)
            color = "seagreen"
            legend_label = "Duplex-Triplex"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(sqSFRlst)
            y_axis_coordinates = np.array(priceSFR)
            color = "magenta"
            legend_label = "Single Family Residence"
#p.legend.label_text_font_size = '10pt'

            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
                            




                    
#p.legend.location = "bottom_right"
            p.legend.click_policy="hide"
            p.legend.label_text_font_size = "7pt"
            p.left[0].formatter.use_scientific = False
            p.add_layout(p.legend[0], 'right')
 
        elif var1 == "Percentage Gain/Loss vs year":
            # lst = ["2007-11-23", "2008-11-23","2010-11-23","2012-11-23"]
            # temp = ["Not Prime", "Prime", "Prime", "Prime"]
            # res = [2100, 3100, 1250, 1580]
            # dict1 = {"Date": lst, "Units":temp, "Wealth":res}
            # dict1 = pd.DataFrame(dict1)
            # print(dict1)
            # p = figure(width = 700, height = 500, x_axis_type = "datetime",x_axis_label = "Years", y_axis_label = "Wealth")
            # dict1["Date"] = pd.to_datetime(dict1["Date"])
            # p.line(dict1["Date"],dict1["Wealth"], line_width=2)
            State_time_series=pd.read_csv("State_time_series.csv",parse_dates=True)
            State_time_series.Date=pd.to_datetime(State_time_series.Date)
            State_time_series['year'] = State_time_series.Date.dt.year
            dfgain=State_time_series.groupby(State_time_series['year'])['PctOfHomesSellingForGain_AllHomes'].median().dropna().reset_index()
            dfloss=State_time_series.groupby(State_time_series['year'])['PctOfHomesSellingForLoss_AllHomes'].median().dropna().reset_index()
            gainyear=dfgain['year'].to_list()
            lossyear=dfloss['year'].to_list()
            gain=dfgain['PctOfHomesSellingForGain_AllHomes'].to_list()
            loss=dfloss['PctOfHomesSellingForLoss_AllHomes'].to_list()
            p = figure(title = "Perentage Of Homes Selling for Gain and Loss",plot_width = 700, plot_height = 500)
            #x_axis_type = "datetime"
                        # name of the x-axis
            p.xaxis.axis_label = 'Year'

                        # name of the y-axis
            p.yaxis.axis_label = 'Perentage Gain and Loss'

                        
            x_axis_coordinates = np.array(gainyear)
            y_axis_coordinates = np.array(gain)
            color = "brown"
            legend_label = "PctOfHomesSellingForGain_AllHomes"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
            x_axis_coordinates = np.array(lossyear)
            y_axis_coordinates = np.array(loss)
            color = "blue"
            legend_label = "PctOfHomesSellingForLoss_AllHomes"
            p.line(x_axis_coordinates,
                                y_axis_coordinates,
                                color = color,
                                legend_label = legend_label)
                   
            p.legend.location = "center"
            p.legend.click_policy="hide"
            p.legend.label_text_font_size = "10pt"
            p.left[0].formatter.use_scientific = False
 
        elif var1 == "Rental price Vs Area(Square foot)":
            # lst = ["2007-11-23", "2008-11-23","2010-11-23","2012-11-23"]
            # temp = ["Not Prime", "Prime", "Prime", "Prime"]
            # res = [2100, 3100, 1250, 1580]
            # dict1 = {"Date": lst, "Units":temp, "Wealth":res}
            # dict1 = pd.DataFrame(dict1)
            # print(dict1)
            # p = figure(width = 700, height = 500, x_axis_type = "datetime",x_axis_label = "Years", y_axis_label = "Wealth")
            # dict1["Date"] = pd.to_datetime(dict1["Date"])
            # p.line(dict1["Date"],dict1["Wealth"], line_width=2)
            State_time_series = pd.read_csv("State_time_series.csv",parse_dates=True)
            State_time_series.Date = pd.to_datetime(State_time_series.Date)
            State_time_series['year'] = State_time_series.Date.dt.year
            df_1B = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_1Bedroom'].mean().dropna().to_frame().reset_index()
            df_2B = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_2Bedroom'].mean().dropna().to_frame().reset_index()
            df_3B = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_3Bedroom'].mean().dropna().to_frame().reset_index()
            df_4B = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_4Bedroom'].mean().dropna().to_frame().reset_index()
            df_5B = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_5BedroomOrMore'].mean().dropna().to_frame().reset_index()
            df_All = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_AllHomes'].mean().dropna().to_frame().reset_index()
            df_cc = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_CondoCoop'].mean().dropna().to_frame().reset_index()
            df_dt = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_DuplexTriplex'].mean().dropna().to_frame().reset_index()
            df_sfr = State_time_series.groupby(State_time_series['year'])['MedianRentalPricePerSqft_SingleFamilyResidence'].mean().dropna().to_frame().reset_index()
            y_1b = df_1B["year"].to_list() 
            y_2b = df_2B["year"].to_list() 
            y_3b = df_3B["year"].to_list()  
            y_4b = df_4B["year"].to_list() 
            y_5b = df_5B["year"].to_list()  
            y_all = df_All["year"].to_list() 
            y_cc = df_cc["year"].to_list() 
            y_dt = df_dt["year"].to_list()  
            y_sfr = df_sfr["year"].to_list() 
            price_1b = df_1B['MedianRentalPricePerSqft_1Bedroom']
            price_2b = df_2B['MedianRentalPricePerSqft_2Bedroom']
            price_3b = df_3B['MedianRentalPricePerSqft_3Bedroom']
            price_4b = df_4B['MedianRentalPricePerSqft_4Bedroom']
            price_5b = df_5B['MedianRentalPricePerSqft_5BedroomOrMore']
            price_all = df_All['MedianRentalPricePerSqft_AllHomes']
            price_cc = df_cc['MedianRentalPricePerSqft_CondoCoop']
            price_dt = df_dt['MedianRentalPricePerSqft_DuplexTriplex']
            price_str = df_sfr['MedianRentalPricePerSqft_SingleFamilyResidence']

            price_final = [price_1b, price_2b, price_3b, price_4b, price_5b, price_all,
                   price_cc, price_dt, price_str] 
            colors = ["brown", "blue", "orange", "yellow", "deeppink",
                    "red", "goldenrod", "seagreen", "magenta"]

            legends_final = ['1 Bedroom',
                 '2 Bedroom',
                 '3 Bedroom',
                 '4 Bedroom',
                 '5 Bedrooms Or More',
                 'All Homes',
                 'CondoCoop',
                 'Duplex-Triplex',
                 'Single Family Residence'] 
            years_final = [y_1b, y_2b, y_3b, y_4b, y_5b, y_all, y_cc, y_dt, y_sfr]
            p = figure(title = "Real Estate Rental Prices Per SquareFoot in US",plot_width = 700, plot_height = 500)
    
            p.xaxis.axis_label = 'Year'

            p.yaxis.axis_label = 'Median Rental Prices Per Sqft'

# year, price, color, legend
            for year, price, color, legend in zip(years_final, price_final, colors, legends_final):
    
                x_axis_coordinates = np.array(year)
                y_axis_coordinates = np.array(price)
                color = color
                legend_label = legend

                p.line(x_axis_coordinates, y_axis_coordinates,
                color = color, legend_label = legend_label)

    
            p.legend.click_policy = "hide"
            p.legend.label_text_font_size = "7pt"
            p.left[0].formatter.use_scientific = False
            p.add_layout(p.legend[0], 'right')
        elif var1 == "Increase in House SalePrice as shown by Time Frequency":


            State_time_series = pd.read_csv("State_time_series.csv",parse_dates=True)
            State_time_series.Date = pd.to_datetime(State_time_series.Date)
            State_time_series['year'] = State_time_series.Date.dt.year
            states = set(State_time_series[
                                ~State_time_series['ZHVI_AllHomes'].isnull() &
                                ~State_time_series['Sale_Prices'].isnull()
                                ]['RegionName'].values)

            State_time_series_year = State_time_series[State_time_series['RegionName'].isin(states)].copy()
            highest_cost_states = State_time_series_year[['RegionName', 'ZHVI_AllHomes']].groupby('RegionName').max().sort_values(by=['ZHVI_AllHomes'], ascending=False)[:5].index.values.tolist()
            State_time_series_year=State_time_series_year[State_time_series_year.RegionName.isin(highest_cost_states)]
            State_time_series_year.year = State_time_series_year.Date.dt.year   
            States_year_SalePrices = State_time_series_year.groupby([State_time_series_year.Date,State_time_series_year.RegionName])['Sale_Prices'].mean().dropna().reset_index(name='Sale_Prices')
            PriceDF = States_year_SalePrices.pivot(index='Date', columns='RegionName', values='Sale_Prices').dropna()#.plot(figsize=(15,8))#, color=colors, legend=False)

            t0 = PriceDF.index
            t1 = pd.date_range(pd.to_datetime('30/01/2009'),pd.to_datetime('2017-08-31'),freq='A')
            t2 = pd.date_range(pd.to_datetime('30/01/2009',dayfirst = True),pd.to_datetime('2016-08-31' ,dayfirst=True),freq='M')
            t3 = pd.date_range(pd.to_datetime('30/01/2009',dayfirst = True),pd.to_datetime('2015-08-31',dayfirst=True),freq='Q')



            df1 = PriceDF.reindex(index = t0, columns = highest_cost_states).reset_index()
            df2 = PriceDF.reindex(index = t1, columns = highest_cost_states).reset_index()
            df3 = PriceDF.reindex(index = t2, columns = highest_cost_states).reset_index()
            df4 = PriceDF.reindex(index = t3, columns = highest_cost_states).reset_index()
            time_daily = df1["Date"].to_list()
            time_daily = [time_daily] * 5
            Sale_price_daily = [df1["DistrictofColumbia"].to_list(),df1["California"].to_list(),
                   df1["Massachusetts"].to_list(),df1["NewJersey"].to_list(),
                   df1["Washington"].to_list()]
            time_yearly = df2["index"].to_list()
            time_yearly = [time_yearly] * 5

            Sale_price_yearly = [df2["DistrictofColumbia"].to_list(),df2["California"].to_list(),
                   df2["Massachusetts"].to_list(),df2["NewJersey"].to_list(),
                   df2["Washington"].to_list()]

            time_monthly = df3["index"].to_list()
            time_monthly = [time_monthly] * 5

            Sale_price_monthly = [df3["DistrictofColumbia"].to_list(),df3["California"].to_list(),
                   df3["Massachusetts"].to_list(),df3["NewJersey"].to_list(),
                   df3["Washington"].to_list()]

            time_quarterly = df4["index"].to_list()
            time_quarterly = [time_quarterly] * 5

            Sale_price_quarterly = [df4["DistrictofColumbia"].to_list(),df4["California"].to_list(),
                   df4["Massachusetts"].to_list(),df4["NewJersey"].to_list(),
                   df4["Washington"].to_list()]

            colors = ["blue", "orange", "yellow", "red", "seagreen"]

            legends_final = ['DistrictofColumbia',
                 'California',
                 'Massachusetts',
                 'NewJersey',
                 'Washington']

            p1 = figure(title = "Increase in House SalePrice for Top US states as shown by Time Frequency",
             x_axis_type = "datetime", width=600, plot_height=200)
    
            p1.xaxis.axis_label = 'time'

            p1.yaxis.axis_label = 'Saleprice Daily'

# year, price, color, legend
            for year, per, color, legend in zip(time_daily, Sale_price_daily, colors, legends_final):
    
                x_axis_coordinates = np.array(year)
                y_axis_coordinates = np.array(per)
                color = color
                legend_label = legend

                p1.line(x_axis_coordinates, y_axis_coordinates,
                     color = color, legend_label = legend_label)

    
            p1.legend.click_policy = "hide"
            p1.legend.label_text_font_size = "7pt"
            p1.left[0].formatter.use_scientific = False
            p1.add_layout(p1.legend[0], 'right')



            p2 = figure(x_axis_type = "datetime",width=600, plot_height=200, title=None)
    
            p2.xaxis.axis_label = 'time'

            p2.yaxis.axis_label = 'Saleprice Yearly'

# year, price, color, legend
            for year, per, color, legend in zip(time_yearly, Sale_price_yearly, colors, legends_final):
    
                x_axis_coordinates = np.array(year)
                y_axis_coordinates = np.array(per)
                color = color
                legend_label = legend

                p2.line(x_axis_coordinates, y_axis_coordinates,
                    color = color, legend_label = legend_label)

    
            p2.legend.click_policy = "hide"
            p2.legend.label_text_font_size = "7pt"
            p2.left[0].formatter.use_scientific = False
            p2.add_layout(p2.legend[0], 'right')


            p3 = figure(x_axis_type = "datetime",width=600, plot_height=200, title=None)
    
            p3.xaxis.axis_label = 'time'

            p3.yaxis.axis_label = 'Saleprice Monthly'

# year, price, color, legend
            for year, per, color, legend in zip(time_monthly, Sale_price_monthly, colors, legends_final):
    
                x_axis_coordinates = np.array(year)
                y_axis_coordinates = np.array(per)
                color = color
                legend_label = legend

                p3.line(x_axis_coordinates, y_axis_coordinates,
                    color = color, legend_label = legend_label)

    
            p3.legend.click_policy = "hide"
            p3.legend.label_text_font_size = "7pt"
            p3.left[0].formatter.use_scientific = False
            p3.add_layout(p3.legend[0], 'right')


            p4 = figure(x_axis_type = "datetime",width=600, plot_height=200, title=None)
    
            p4.xaxis.axis_label = 'time'

            p4.yaxis.axis_label = 'Saleprice Quartertly'

# year, price, color, legend
            for year, per, color, legend in zip(time_quarterly, Sale_price_quarterly, colors, legends_final):
    
                x_axis_coordinates = np.array(year)
                y_axis_coordinates = np.array(per)
                color = color
                legend_label = legend

                p4.line(x_axis_coordinates, y_axis_coordinates,
                    color = color, legend_label = legend_label)

    
            p4.legend.click_policy = "hide"
            p4.legend.label_text_font_size = "7pt"
            p4.left[0].formatter.use_scientific = False
            p4.add_layout(p4.legend[0], 'right')



# put all the plots in a VBox
            p = column(p1, p2, p3, p4)
        elif var1 == "Real Estate Properties With Price Reductions in US":
            State_time_series = pd.read_csv("State_time_series.csv",parse_dates=True)
            State_time_series.Date = pd.to_datetime(State_time_series.Date)
            State_time_series['year'] = State_time_series.Date.dt.year

            df_all = State_time_series.groupby(State_time_series['year'])['PctOfListingsWithPriceReductionsSeasAdj_AllHomes'].median().dropna().to_frame().reset_index()
            df_condo = State_time_series.groupby(State_time_series['year'])['PctOfListingsWithPriceReductionsSeasAdj_CondoCoop'].median().dropna().to_frame().reset_index()
            df_single = State_time_series.groupby(State_time_series['year'])['PctOfListingsWithPriceReductionsSeasAdj_SingleFamilyResidence'].median().dropna().to_frame().reset_index()

            y_all = df_all["year"].to_list()
            y_condo = df_condo["year"].to_list()
            y_single = df_single["year"].to_list()

            per_reduction_all = df_all['PctOfListingsWithPriceReductionsSeasAdj_AllHomes'].to_list()
            per_reduction_condo = df_condo['PctOfListingsWithPriceReductionsSeasAdj_CondoCoop'].to_list()
            per_reduction_single = df_single['PctOfListingsWithPriceReductionsSeasAdj_SingleFamilyResidence'].to_list()

            y_final = [y_all,y_condo, y_single]
            per_reduction_final = [per_reduction_all, per_reduction_condo, per_reduction_single]
            colors = ["red", "green", "yellow"]
            legends_final = ["AllHomes", "CondoCoop","SingleFamilyResidence"]

            p = figure(title = "Real Estate Properties With Price Reductions in US",plot_width = 700, plot_height = 500)
    
            p.xaxis.axis_label = 'Year'

            p.yaxis.axis_label = 'Percentage of Homes with Price Reductions Seasonal Adjustments'

# year, price, color, legend
            for year, per, color, legend in zip(y_final, per_reduction_final, colors, legends_final):
    
                x_axis_coordinates = np.array(year)
                y_axis_coordinates = np.array(per)
                color = color
                legend_label = legend

                p.line(x_axis_coordinates, y_axis_coordinates,
                    color = color, legend_label = legend_label)

    
            p.legend.click_policy = "hide"
            p.legend.label_text_font_size = "7pt"
            p.left[0].formatter.use_scientific = False
            p.add_layout(p.legend[0], 'right')

        elif var1 == "Real Estate Properties Decresing Vs Increasing in Values in US":
            State_time_series = pd.read_csv("State_time_series.csv",parse_dates=True)
            State_time_series.Date = pd.to_datetime(State_time_series.Date)
            State_time_series['year'] = State_time_series.Date.dt.year

            df_dec = State_time_series.groupby(State_time_series['year'])['PctOfHomesDecreasingInValues_AllHomes'].median().dropna().to_frame().reset_index()
            df_inc = State_time_series.groupby(State_time_series['year'])['PctOfHomesIncreasingInValues_AllHomes'].median().dropna().to_frame().reset_index()

            y_inc = df_inc["year"].to_list()
            y_dec = df_dec["year"].to_list()


            per_dec = df_dec['PctOfHomesDecreasingInValues_AllHomes'].to_list()
            per_inc = df_inc['PctOfHomesIncreasingInValues_AllHomes'].to_list()

            y_final = [y_inc, y_dec]
            per_final = [per_inc, per_dec]
            colors = ["red", "blue"]
            legends_final = ["% of Homes Increasing", "% of Homes Decreasing"]
            p = figure(title = "Real Estate Properties Decresing Vs Increasing in Values in US",plot_width = 700, plot_height = 500)
    
            p.xaxis.axis_label = 'Year'

            p.yaxis.axis_label = 'Percentage of Homes increasing and decreasing in values'

# year, price, color, legend
            for year, per, color, legend in zip(y_final, per_final, colors, legends_final):
    
                x_axis_coordinates = np.array(year)
                y_axis_coordinates = np.array(per)
                color = color
                legend_label = legend

                p.line(x_axis_coordinates, y_axis_coordinates,
                     color = color, legend_label = legend_label)

    
            p.legend.click_policy = "hide"
            p.legend.label_text_font_size = "7pt"
            p.left[0].formatter.use_scientific = False
            p.add_layout(p.legend[0], 'right')

        demo_script_code,chart_code = components(p)
        return render_template('final_comparison.html',chart_code = chart_code,demo_script_code = demo_script_code)

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 5000))         # added
    app.run(host='0.0.0.0', port=PORT, debug=True)    # added
    # app.run(debug=True)
