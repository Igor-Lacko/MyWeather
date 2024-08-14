"""Dictionary with the layout of the INITIAL items in the Weather tab (so not the views the user chooses)."""
from . import *

#used other times than just the default init, so better off as a separate variable
api_options = {
        "type"      :   "layout",
        "layout"    :   "horizontal",
        "spacing"   :   0,
        "margins"   :   [0,0,0,0],
        "stretch"   :   30,
        "items"     :   [

            {
                "type"          :   "stretch",
                "stretch"       :   20,
            },

            {
                "type"          :   "TextImageButton",
                "stretch"       :   15,
                "objname"       :   "realtime",
                "title"         :   "Realtime",
                "description"   :   "Realtime weather data for the location of your choosing.",
            },

            {
                "type"          :   "stretch",
                "stretch"       :   15,
            },

            {
                "type"          :   "TextImageButton",
                "stretch"       :   15,
                "objname"       :   "forecast",
                "title"         :   "Forecast",
                "description"   :   "Weather forecast for the location of your choosing up to 3 days in the future.",
            },

            {
                "type"          :   "stretch",
                "stretch"       :   15,
            },

            {
                "type"          :   "TextImageButton",
                "stretch"       :   15,
                "objname"       :   "history",
                "title"         :   "History",
                "description"   :   "Historic weather data for the location of your choosing. Up to a week in the past.",
            },

            {
                "type"          :   "stretch",
                "stretch"       :   20,
            },
        ]
    }

#the weather tab layout at the beginning
layout = [

    {
        "type"      :   "stretch",
        "stretch"   :   5
    },
    
    {
        "type"      :   "title",
        "stretch"   :   10,
        "text"      :   "Choose your mode.",
        "alignment" :   Alignments.TopCenter,
        "pointsize" :   40
    },

    {
        "type"          :   "stretch",
        "stretch"       :   45,
    },

    api_options,

    {
        "type"      :   "stretch",
        "stretch"   :   10
    }

]


