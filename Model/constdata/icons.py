"""contains a dictionary of weather conditions : icons
        Structure:  "conditions" : (list),
                    "day" : (url) - their day icon (for all the conditions in that list),
                    "night" : (url) - their night icon (for all the conditions in that list)
"""



Icons = [
    
    {
        "conditions"    :   [
            "Sunny", 
            "Clear"
        ],

        "day"   :   "Assets/ConditionIcons/day/sunny.png",
        "night" :   "Assets/ConditionIcons/night/clear.png"
    },

    {
        "conditions"    :   [
            "Cloudy",
            "Partly cloudy",
            "Overcast"
        ],

        "day" : "Assets/ConditionIcons/day/cloudy.png",
        "night" : "Assets/ConditionIcons/night/cloudy.png"
    },

    {
        "conditions"    :   [
            "Mist", 
            "Fog"
        ],

        "day"   :   "Assets/ConditionIcons/day/fog.png",
        "night" :   "Assets/ConditionIcons/night/fog.png"      
    },

    {
        "conditions"    :   [
            "Patchy rain possible",
            "Light drizzle",
            "Patchy light rain",
            "Light rain",
            "Light rain shower",
        ],

        "day"   :   "Assets/ConditionIcons/day/light-rain.png",
        "night" :   "Assets/ConditionIcons/night/light-rain.png"
    },

    {
        "conditions"    :   [
            "Moderate rain at times",
            "Moderate rain"
        ],

        "day"   :   "Assets/ConditionIcons/day/moderate-rain.png",
        "night" :   "Assets/ConditionIcons/night/moderate-rain.png"
    },

    {
        "conditions"    :   [
            "Heavy rain at times",
            "Heavy rain",
            "Moderate or heavy rain shower",
            "Torrential rain shower"
        ],

        "day"   :   "Assets/ConditionIcons/day/heavy-rain.png",
        "night" :   "Assets/ConditionIcons/night/heavy-rain.png"
    },

    {
        "conditions"    :   [
            "Thundery outbreaks possible",
            "Patchy light rain with thunder",
            "Moderate or heavy rain with thunder"
        ],

        "day"   :   "Assets/ConditionIcons/day/storm.png",
        "night" :   "Assets/ConditionIcons/night/storm.png"
    }


]

