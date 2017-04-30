'''
2. Using SNMPv3 create two SVG image files.  

The first image file should graph the input and output octets on interface FA4 on pynet-rtr1 every five minutes for an hour. 
Use the pygal library to create the SVG graph file. Note, you should be doing a subtraction here (i.e. the input/output octets 
transmitted during this five minute interval).  

The second SVG graph file should be the same as the first except graph the unicast packets received and transmitted.

The relevant OIDs are as follows:

('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5')
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5')
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5')
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')

username:       pysnmp
auth_key:        galileo1          
encrypt_key:   galileo1

pynet-rtr1    184.105.247.70    UDP 161
​​​​​​​pynet-rtr2    184.105.247.71    UDP 161
'''
import pygal
from snmp_helper import snmp_get_oid_v3, snmp_extract
import time

pynet_rtr1 = ('184.105.247.70', 161)
usuario = ('pysnmp', 'galileo1', 'galileo1')

oid_fa4 = {
    'oid_oct_in_fa4' : '1.3.6.1.2.1.2.2.1.10.5.0',
    'oid_oct_out_fa4' : '1.3.6.1.2.1.2.2.1.16.5.0',
    'oid_uni_in_fa4' : '1.3.6.1.2.1.2.2.1.11.5.0',
    'oid_uni_out_fa4' : '1.3.6.1.2.1.2.2.1.17.5.0'
    }

data_fa4 = {
    'oct_in_fa4' : list(),
    'oct_out_fa4' : list(),
    'uni_in_fa4' : [],
    'uni_out_fa4' : []
    }


for time_track in range(0, 65, 5):
    for oid in oid_fa4:
        data_fa4['oct_in_fa4'] = data_fa4['oct_in_fa4'].append(snmp_get_oid_v3(pynet_rtr1, usuario, oid = oid_fa4['oid_oct_in_fa4']))
        data_fa4['oct_out_fa4'] = data_fa4['oct_out_fa4'].append(snmp_get_oid_v3(pynet_rtr1, usuario, oid = oid['oid_oct_out_fa4']))
        data_fa4['uni_in_fa4'] = data_fa4['uni_in_fa4'].append(snmp_get_oid_v3(pynet_rtr1, usuario, oid = oid['oid_uni_in_fa4']))
        data_fa4['uni_out_fa4'] = data_fa4['uni_out_fa4'].append(snmp_get_oid_v3(pynet_rtr1, usuario, oid = oid['oid_uni_out_fa4']))
  
line_chart_oct = pygal.Line()
line_chart_oct.title = 'Input/Output Fa4 Bytes'
line_chart_oct.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
line_chart_oct.add('InOctets', data_fa4['oct_in_fa4'])
line_chart_oct.add('OutOctets', data_fa4['oct_out_fa4'])
line_chart_oct.render_to_file('octets.svg')

line_chart_uni = pygal.Line()
line_chart_uni.title = 'Input/Output Fa4 Unicasts'
line_chart_uni.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
line_chart_uni.add('InUnicasts', data_fa4['uni_in_fa4'])
line_chart_uni.add('OutUnicasts', data_fa4['uni_out_fa4'])
line_chart_uni.render_to_file('unicasts.svg')

# Create an output image file from this





'''
Note, you should be able to scp (secure copy) your image file off the lab server. You can then open up the file using a browser.  
For example, on MacOs I did the following (from the MacOs terminal):

scp kbyers@<hostname>:SNMP/class2/test.svg .

This copied the file from ~kbyers/SNMP/class2/test.svg to the current directory on my MAC.  

The format of the command is:

scp <remote-username>@<remote-hostname>:<remote_path>/<remote_file> .

The period at the end indicates the file should be copied to the current directory on the local machine.

For Windows, you can use PuTTY scp

You might need to ensure that pscp.exe (putty scp) is in your Windows PATH.

Note, the example on the cornell.edu site is doing a copy of a local file to a remote server. You would need to do the opposite i.e. 
copy a remote file to your local computer:

pscp <remote-username>@<remote-hostname>:<remote_path>/<remote_file> .
'''