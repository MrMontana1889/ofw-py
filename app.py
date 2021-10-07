import sys
import clr

sys.path.append('D:\\p4\\Glacier\\Products\\WaterGEMS\\Output\\_Starter\\x64\\Debug')
clr.AddReference('OpenFlows.Water')

# import OpenFlows.Water.Python
from OpenFlows.Water import OpenFlowsWater, WaterProductLicenseType

print("Start")
OpenFlowsWater.StartSession(WaterProductLicenseType.WaterGEMS)

filename = "D:\\p4\\Glacier\\Products\\WaterGEMS\\Development\\Runtime\\Samples\\Example1.wtg"
wm = OpenFlowsWater.Open(filename)

print("End")
OpenFlowsWater.EndSession()