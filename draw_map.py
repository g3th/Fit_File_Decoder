import folium
import webbrowser
from folium import IFrame

class DrawMap:

    def __init__(self, start, end, zoom_value, line_width, w, h):
        self.zoom_value = zoom_value
        self.line_width = line_width
        self.folium_map_object = folium.Map(width=w, height=h, location=[start, end], zoom_start=self.zoom_value)
        self.webbrowser = webbrowser

    def create_points(self, lon, lat, colour):
        folium.PolyLine([lon, lat], color=colour, weight=self.line_width, opacity=0.8).add_to(self.folium_map_object)

    def popup_with_run_info(self, val):
        self.folium_map_object.get_root().html.add_child(folium.Element("""
            <div style="position:fixed;left:1200px;width:200px;height:200px;background-color:white;z-index:900">
            <h1><br> {} </br></h1>
            </div>
        """.format(val)))
    def draw(self):
        self.folium_map_object.save("route.html")
        self.webbrowser.open("route.html")


