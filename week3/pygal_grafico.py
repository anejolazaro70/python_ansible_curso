'''
The below code creates an SVG image using pygal from SNMP interface data.

>>>> CODE <<<<
'''

import pygal

fa4_in_octets = [5269, 5011, 6705, 5987, 5011, 5071, 6451, 5011, 5011, 6181, 5281, 5011]
fa4_out_octets =[5725, 5783, 7670, 6783, 5398, 5783, 9219, 3402, 5783, 6953, 5668, 5783]

fa4_in_packets = [24, 21, 40, 32, 21, 21, 49, 9, 21, 34, 24, 21]
fa4_out_packets = [24, 21, 40, 32, 21, 21, 49, 9, 21, 34, 24, 21]

# Create a Chart of type Line
line_chart = pygal.Line()

# Title
line_chart.title = 'Input/Output Packets and Bytes'

# X-axis labels (samples were every five minutes)
line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']

# Add each one of the above lists into the graph as a line with corresponding label
line_chart.add('InPackets', fa4_in_packets)
line_chart.add('OutPackets', fa4_out_packets)
line_chart.add('InBytes', fa4_out_octets)
line_chart.add('OutBytes', fa4_in_octets)

# Create an output image file from this
line_chart.render_to_file('test.svg')

'''
>>>> END CODE <<<<

You can view the image that was created at:
https://pynet.twb-tech.com/static/img/snmp_interfaces.svg
'''