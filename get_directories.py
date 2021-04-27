#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     29/01/2020
# Copyright:   (c) Admin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import arcpy

arcpy.env.workspace
def main(folder):
    dirs = os.listdir(folder)
    arcpy.AddMessage(dirs)

    for folder in dirs:
        path = os.path.dirname(folder)
        arcpy.AddMessage(path)


    """for fol in dirs:
        os.chdir(fol)
        arcpy.AddMessage(fol)
        tifs = arcpy.ListRasters("*", "TIF")
        arcpy.AddMessage(tifs)"""

    #for root, dirs, filenames in os.walk(folder):


if __name__ == '__main__':
    folder = arcpy.GetParameterAsText(0)
    arcpy.AddMessage(folder)
    main(folder)
