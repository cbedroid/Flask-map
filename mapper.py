from folium  import Map,Marker

class Maps():
    def __init__(self,lat,lon,**kwargs):
        # two coords point
        self.lat = lat
        self.lon = lon
        self.save_location = kwargs.pop('save','template/map.html')
        self.file = self.save_location.split('/')[-1]
        self.maps = Map(location=[self.lat,self.lon],**kwargs)

    def save(self):
        self.maps.save(self.save_location)
    
    def marker(self,**kwargs):
        add_to = kwargs.pop('add_to',True)

        marker = Marker([self.lat,self.lon],
                **kwargs)
        if add_to:
            marker.add_to(self.maps)


