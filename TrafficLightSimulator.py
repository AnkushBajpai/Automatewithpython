market_2nd = {'ns': 'yellow', 'ew': 'red'}
mission_16th = {'ns': 'red', 'xy':'red', 'ew': 'green'}

#fn. to switch the lights

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
        assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)   
        # The above line makes sure that one signal must be red at all time to avoid crash
 
switchLights(mission_16th) # fn. call