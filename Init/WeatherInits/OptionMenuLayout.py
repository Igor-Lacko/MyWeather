"""Module with the layout/item specification dictionaries for option menu"""
from ..CityDatabase import database
from MyWeather.View.utils.methods import GetDaylist

realtime_menu_layout = [
    {
        "stretch"   :   10,
        "type"      :   "twobuttonsoption",
        "name"      :   "realtimebuttons",
        "pointsize" :   20,
        "space"     :   80,

        "resetbutton"   :   {
            "name"      :   "resetbutton",
            #add slot here later
        },

        "submitbutton"  :   {
            "name"      :   "submitbutton"
            #add slot here later
        }
    },

    {
        "stretch"   :   20,
        "type"      :   "lineeditoption",
        "name"      :   "realtimelocationoption",

        "label"     :   {
            "text"      :   "Select the location you want to view the current weather for",
            "pointsize" :   20,
            "name"      :   "realtimelocationdescription"
        },

        "lineedit"  :   {
            "items"     :   database,
            "example"   :   "e.g. 'New York'",
            "name"      :   "realtimelocationlineedit"
        }
    },

    {
        "stretch"   :   20,
        "type"      :   "comboboxoption",
        "name"      :   "realtimeviewoption",

        "label"     :   {
            "text"      :   "Select the appearance of the weather data",
            "pointsize" :   20,
            "name"      :   "realtimeviewdescription"
        },

        "combobox"  :   {
            "items"     :   ["Graph", "Text"],
            "name"      :   "realtimeviewcombobox"
        }
    },

    {
        "type"      :   "imageoption",
        "name"      :   "tenkinokomeme",
        "stretch"   :   50,

        "label"     :   {
            "text"      :   "Hodaka approves! ------->",
            "pointsize" :   40,
            "name"      :   "tenkinokomemetext",
        },

        "image"     :   {
            "name"      :   "tenkinokomemeimage",
            "path"      :   "Assets/Memes/Hodaka_Morishima_Profile.webp"
        }
    }
]

forecast_menu_layout = [
        {
        "type"      :   "twobuttonsoption",
        "stretch"   :   10,
        "name"      :   "forecastbuttons",
        "pointsize" :   20,
        "space"     :   80,

        "resetbutton"   :   {
            "name"      :   "resetbutton",
            #add slot here later
        },

        "submitbutton"  :   {
            "name"      :   "submitbutton"
            #add slot here later
        }
    },

    {
        "type"      :   "lineeditoption",
        "stretch"   :   20,
        "name"      :   "forecastlocationoption",

        "label"     :   {
            "text"      :   "Select the location you want to view the current weather for",
            "pointsize" :   20,
            "name"      :   "forecastlocationdescription"
        },

        "lineedit"  :   {
            "items"     :   database,
            "example"   :   "e.g. 'New York'",
            "name"      :   "forecastlocationlineedit"
        }
    },

    {
        "type"      :   "comboboxoption",
        "stretch"   :   20,
        "name"      :   "forecastviewoption",

        "label"     :   {
            "text"      :   "Select the appearance of the weather data",
            "pointsize" :   20,
            "name"      :   "forecastviewdescription"
        },

        "combobox"  :   {
            "items"     :   ["Graph", "Tabs"],
            "name"      :   "forecastviewcombobox"
        }
    },

    {
        "type"      :   "slideroption",
        "stretch"   :   20,
        "name"      :   "forecastdayoption",

        "label"     :   {
            "text"      :   "Select how many days you want to view the forecast for",
            "pointsize" :   15,
            "name"      :   "forecastdaysdescription"
        },

        "slider"    :   {
            "range" :   3,
            "name"  :   "forecastdaybar"
        }
    },

    {
        "type"      :   "comboboxoption",
        "stretch"   :   20,
        "name"      :   "forecastdateoption",

        "label"     :   {
            "text"      :   "Or if you want to only see one day, pick a date from the upcoming 3 days",
            "pointsize" :   15,
            "name"      :   "forecastdatedescription"
        },

        "combobox"  :   {
            "items"     :   GetDaylist(3, True),
            "name"      :   "forecastdatecombobox"
        }
    },

    {
        "type"      :   "stretch",
        "stretch"   :   10
    }
]

history_menu_layout = [
    {
        "stretch"   :   10,
        "type"      :   "twobuttonsoption",
        "name"      :   "historybuttons",
        "pointsize" :   20,
        "space"     :   80,

        "resetbutton"   :   {
            "name"      :   "resetbutton",
            #add slot here later
        },

        "submitbutton"  :   {
            "name"      :   "submitbutton"
            #add slot here later
        }
    },

    {
        "type"      :   "lineeditoption",
        "stretch"   :   20,
        "name"      :   "historylocationoption",

        "label"     :   {
            "text"      :   "Select the location you want to view the current weather for",
            "pointsize" :   20,
            "name"      :   "historylocationdescription"
        },

        "lineedit"  :   {
            "items"     :   database,
            "example"   :   "e.g. 'New York'",
            "name"      :   "historylocationlineedit"
        }
    },

    {
        "stretch"   :   20,
        "type"      :   "comboboxoption",
        "name"      :   "historyviewoption",

        "label"     :   {
            "text"      :   "Select the appearance of the weather data",
            "pointsize" :   20,
            "name"      :   "historyviewdescription"
        },

        "combobox"  :   {
            "items"     :   ["Graph", "Text"],
            "name"      :   "historyviewcombobox"
        }
    },

    {
        "type"      :   "slideroption",
        "stretch"   :   20,
        "name"      :   "historydayoption",

        "label"     :   {
            "text"      :   "Select how many days in the past do you want to view the weather for",
            "pointsize" :   15,
            "name"      :   "historydaydescription"
        },

        "slider"        :   {
            "range"     :   7,
            "name"      :   "historydaybar"
        }
    },

    {
        "type"      :   "comboboxoption",
        "stretch"   :   20,
        "name"      :   "historydateoption",

        "label"     :   {
            "text"      :   "Or if you want to only see one day, pick a date from the 7 past days",
            "pointsize" :   15,
            "name"      :   "historydatedescription"
        },

        "combobox"  :   {
            "items"     :   ["None"] + GetDaylist(7, False),
            "name"      :   "historydatecombobox"
        }
    },

    {
        "type"      :   "stretch",
        "stretch"   :   10
    }
]