import os
import re
import json
from flask import Flask,jsonify,redirect,url_for,Request,request,render_template, flash
from flask_restful import Resource, Api, reqparse
from mapper import Maps

app = Flask(__name__,template_folder='template')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
api = Api(app)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'd21e24db0d56219f41bc512b22f1e281'


class MyMap():
    @app.route('/',methods=['GET','POST'])
    @app.route('/home',methods=['GET','POST'])
    def home():
        lat = request.form.get('latitude')
        lon = request.form.get('longitude')
        if not lat and not lon:
            return render_template('home.html')
        else:
            try:
                lat = float(lat)
                lon = float(lon)
            except:
                flash(f'Invalid coordinates and try again','danger')
                return redirect(url_for('home'))

            else:
                return redirect(url_for('location',
                                        lat=lat,
                                        lon=lon
                                        ))

    @app.route('/location?lat=<string:lat>&lon=string<lon>'
                        ,methods=['GET','POST'])
    def location(lat,lon):
        if lat and lon:
            maps = Maps(lat,lon,save='template/map.html')
            # marker popup can be html 
            # TODO: add geopy location address here

            maps.marker(popup='<strong> PIN POINT LOCATION</strong>',
                    tooltip='Click Here For More Info')
            maps.save()
            return render_template(maps.file)
        return redirect(url_for('home'))         

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003, debug=True)
