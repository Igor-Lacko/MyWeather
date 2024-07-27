"""Dictionary with the layout of the INITIAL items in the Weather tab (so not the views the user chooses)."""
from . import *

layout = [

    {
        "type"      :   "stretch",
        "stretch"   :   5
    },
    
    {
        "type"      :   "label",
        "stretch"   :   10,
        "objname"   :   "title",
        "text"      :   "Choose your mode.",
        "pointsize" :   50,
        "alignment" :   Alignments.TopCenter,
    },

    {
        "type"          :   "stretch",
        "stretch"       :   45,
    },

    {
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
                "index"         :   0
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
                "index"         :   1
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
                "index"         :   2
            },

            {
                "type"          :   "stretch",
                "stretch"       :   20,
            },
        ]
    },

    {
        "type"      :   "stretch",
        "stretch"   :   10
    }


]