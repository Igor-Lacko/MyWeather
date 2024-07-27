"""contains a dictionary of weather conditions : icons
        Structure:  "conditions" : (list),
                    "day" : (url) - their day icon (for all the conditions in that list),
                    "night" : (url) - their night icon (for all the conditions in that list)
"""



Icons = [
    
    {
        "conditions"    :   [
            "sunny", 
            "clear"
        ],

        "day"   :   "Assets/ConditionIcons/day/sunny.png",
        "night" :   "Assets/ConditionIcons/night/clear.png"
    },

    {
        "conditions"    :   [
            "cloudy",
            "partly cloudy",
            "overcast"
        ],

        "day" : "Assets/ConditionIcons/day/cloudy.png",
        "night" : "Assets/ConditionIcons/night/cloudy.png"
    },

    {
        "conditions"    :   [
            "mist", 
            "fog"
        ],

        "day"   :   "Assets/ConditionIcons/day/fog.png",
        "night" :   "Assets/ConditionIcons/night/fog.png"      
    },

    {
        "conditions"    :   [
            "patchy rain possible",
            "patchy rain nearby",
            "light drizzle",
            "patchy light rain",
            "patchy light drizzle",
            "light rain",
            "light rain shower",
        ],

        "day"   :   "Assets/ConditionIcons/day/light-rain.png",
        "night" :   "Assets/ConditionIcons/night/light-rain.png"
    },

    {
        "conditions"    :   [
            "moderate rain at times",
            "moderate rain"
        ],

        "day"   :   "Assets/ConditionIcons/day/moderate-rain.png",
        "night" :   "Assets/ConditionIcons/night/moderate-rain.png"
    },

    {
        "conditions"    :   [
            "heavy rain at times",
            "heavy rain",
            "moderate or heavy rain shower",
            "torrential rain shower",
            "thundery outbreaks in nearby"
        ],

        "day"   :   "Assets/ConditionIcons/day/heavy-rain.png",
        "night" :   "Assets/ConditionIcons/night/heavy-rain.png"
    },

    {
        "conditions"    :   [
            "thundery outbreaks possible",
            "patchy light rain with thunder",
            "moderate or heavy rain with thunder"
        ],

        "day"   :   "Assets/ConditionIcons/day/storm.png",
        "night" :   "Assets/ConditionIcons/night/storm.png"
    }


]