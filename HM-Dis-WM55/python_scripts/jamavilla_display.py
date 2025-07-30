VERSION = '1.0.0'

DISPLAY_ADDRESS = 'REQ0910714'

line1 = 'Fenster'
if hass.states.is_state('binary_sensor.system_windows', 'on'):
    icon1 = 'open'
else:
    icon1 = 'closed'
if hass.states.is_state('binary_sensor.system_windows', 'on'):
    color1 = 'red'
else:
    color1 = 'white'

if hass.states.is_state('binary_sensor.system_windows', 'on'):
    line2 = 'Offen'
else:
    line2 = 'Geschlossen'
icon2 = ''
if hass.states.is_state('binary_sensor.system_windows', 'on'):
    color2 = 'red'
else:
    color2 = 'white'

line3 = 'Licht'
if hass.states.is_state('light.allelichter', 'on'):
    icon3 = 'on'
else:
    icon3 = 'off'
if hass.states.is_state('light.allelichter', 'on'):
    color3 = 'yellow'
else:
    color3 = 'white'
    

if hass.states.is_state('light.allelichter', 'on'):
    line4 = 'An'
else:
    line4 = 'Aus'
icon4 = ''
if hass.states.is_state('light.allelichter', 'on'):
    color4 = 'yellow'
else:
    color4 = 'white'

line5 = 'Temperatur'
icon5 = 'info'
color5 = 'white'

line6 = str(hass.states.get('sensor.outside_temp').state)+ " C"
icon6 = ''
color6 = 'white'

display_data = {'address': DISPLAY_ADDRESS, 'line1':line1, 'line2':line2, 'line3':line3, 'line4':line4, 'line5':line5, 'line6':line6, 'icon1': icon1, 'icon2': icon2, 'icon3':icon3, 'icon4': icon4, 'icon5': icon5, 'icon6':icon6, 'color1':color1, 'color2':color2, 'color3':color3, 'color4':color4, 'color5':color5, 'color6':color6}
hass.services.call('python_script', 'update_display', display_data)