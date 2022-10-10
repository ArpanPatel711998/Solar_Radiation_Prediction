import streamlit as st
import time
import pickle
import pandas as pd



df = pickle.load(open("df.pkl",'rb'))
model = pickle.load(open('model_rfr.pkl','rb'))


st.markdown("<h1 style='text-align: center; color: black;'>Solar Radiation</h1>", unsafe_allow_html=True)

with st.form('form1'):
    temp = st.number_input('Temperature: degrees Fahrenheit')
    pre = st.number_input('Pressure: Hg')
    hum = st.number_input('Humidity: percent')
    WindDirection_Degrees = st.number_input('Wind direction: degrees')
    speed = st.number_input('Speed: miles per hour')
    sunrise = st.time_input('Sunrise: Time',key = int)
    sunset = st.time_input('Sunset: Time',key = str)
    unix = st.number_input('UNIXTime: EX:1664822918')

    predict = st.form_submit_button('Predict')



    if predict:
        u = time.strftime("%d,%m,%Y,%H,%M", time.localtime(unix))
        unixday,unixmonth,unixyear,unixhour,unixmin = u.split(',')
        unixday=int(unixday)
        unixmonth=int(unixmonth)
        unixyear=int(unixyear)
        unixhour=int(unixhour)
        unixmin=int(unixmin)


        sunrise=str(sunrise)
        sunrise_list = sunrise.split(':')
        sunrise_hour = sunrise_list[0]
        sunrise_min = sunrise_list[1]
        sunrise_hour_int = int(sunrise_hour)
        sunrise_min_int = int(sunrise_min)


        sunset=str(sunset)
        sunset_list = sunset.split(':')
        sunset_hour = sunset_list[0]
        sunset_min = sunset_list[1]
        sunset_hour_int = int(sunset_hour)
        sunset_min_int = int(sunset_min)

        pre = float(pre)
        WindDirection_Degrees = float(WindDirection_Degrees)
        speed = float(speed)




        user_report_data = {
            'Temperature': temp,
            'Pressure': pre,
            'Humidity': hum,
            'WindDirection(Degrees)':WindDirection_Degrees,
            'Speed': speed,
            'SunRise_hour':sunrise_hour_int,
            'SunRise_minute':sunrise_min_int,
            'SunSet_hour':sunset_hour_int,
            'SunSet_minute':sunset_min_int,
            'UNIXTime_day': unixday,
            'UNIXTime_month	': unixmonth,
            'UNIXTime_year': unixyear,
            'UNIXTime_hour': unixhour,
            'UNIXTime_minute': unixmin,
        }
        df = pd.DataFrame(user_report_data, index=[0])
        prediction = model.predict(df)

        st.write('Solar Radiation Prediction')
        st.write(str(prediction),' watts per meter^2')





        
        
        
        