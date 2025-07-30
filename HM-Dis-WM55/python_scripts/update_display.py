VERSION = '1.0.0'

DOMAIN = 'homematic_display'

# Homematic display codes
DATA_START = '0x02'
DATA_STOP = '0x03'
DATA_LINE = '0x12'
DATA_COLOR = '0x11'
DATA_LF = '0x0a'
DATA_ICON = '0x13'

DATA_CHANNEL = 1
DATA_PARAM = 'SUBMIT'

# Homematic display dictionaries
DATA_SPECIAL_CHARS = { "d6": "23", "dc": "24", "3d": "27", "c4": "5b", "df": "5f", "e4": "7b", "f6": "7c", "fc": "7d" }
DATA_ICONS = { "off": "0x80", "on": "0x81", "open": "0x82", "closed": "0x83" , "error": "0x84", "ok": "0x85", "info": "0x86", "message": "0x87", "service": "0x88", "green":"0x89", "yellow":"0x8A", "red":"0x8B" }
DATA_COLORS = {"white":"0x80", "red":"0x81", "orange":"0x82", "yellow":"0x83", "green":"0x84", "blue":"0x85"}

# logger.warning("Update display: {}".format(data))

# get parameters
displayAddress = data.get('address')
displayLines = []
displayLines.append(data.get('line1', ' '))
displayLines.append(data.get('line2', ' '))
displayLines.append(data.get('line3', ' '))
displayLines.append(data.get('line4', ' '))
displayLines.append(data.get('line5', ' '))
displayLines.append(data.get('line6', ' '))
displayIcons = []
displayIcons.append(data.get('icon1', ''))
displayIcons.append(data.get('icon2', ''))
displayIcons.append(data.get('icon3', ''))
displayIcons.append(data.get('icon4', ''))
displayIcons.append(data.get('icon5', ''))
displayIcons.append(data.get('icon6', ''))
displayColors = []
displayColors.append(data.get('color1', ''))
displayColors.append(data.get('color2', ''))
displayColors.append(data.get('color3', ''))
displayColors.append(data.get('color4', ''))
displayColors.append(data.get('color5', ''))
displayColors.append(data.get('color6', ''))

# special characters helper
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

# main rountine
if not displayAddress:
    logger.error('address parameter is missing')
else:
    # start message
    message = []
    message.append(DATA_START)

    # add lines
    for line, icon, color in zip(displayLines, displayIcons, displayColors):
        message.append(DATA_LINE)

        encodedLine = ",".join("0x{:02x}".format(ord(c)) for c in line)
        encodedLine = replace_all(encodedLine, DATA_SPECIAL_CHARS)
        message.append(encodedLine)

        if icon:
            message.append(DATA_ICON)
            message.append(DATA_ICONS.get(icon.lower(), ''))
            
        if color:
            message.append(DATA_COLOR)
            message.append(DATA_COLORS.get(color.lower(), ''))

        message.append(DATA_LF)

    # end message
    message.append(DATA_STOP)

    # logger.warning("Update display message: {}".format(','.join(message)))
    hass.services.call('homematicip_local', 'set_device_value', { 'device_address': displayAddress, 'channel': DATA_CHANNEL, 'parameter': DATA_PARAM, 'value': "{}".format(','.join(message)) })