#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     27.03.2019
# Copyright:   (c) Shoblin 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from __future__ import print_function
from vconnector.core import VConnector


username = 'Zabbix@vsphere.local'
password = 'qk8cbEIpioQKRtDnzCvJ'
hostname = 'msk-vcenter1.office.finam.ru'

client = VConnector(  user=username, pwd=password, host=hostname)
client.connect()
vms = client.get_vm_view()
print(vms.view)
client.disconnect()
