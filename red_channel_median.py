from urllib.request import urlretrieve
from osgeo import gdal
from math import isnan
from statistics import median

tiffUrl = 'https://d2k3km6d0fbrze.cloudfront.net/GSat-output/polar-gazelle/polar-gazelle/2024-03-17/S2A_MSI_2024_03_17_19_12_10_merged_L2R_reprojected_WQ.cog'

# Download the GeoTiff file
urlretrieve(tiffUrl, 'image.cog')

# Open the file using GDAL
dataset = gdal.Open('image.cog', gdal.GA_ReadOnly)

# Get the available bands from the file
bands = [dataset.GetRasterBand(i) for i in range(1, dataset.RasterCount + 1)]

# Select the band with description 'Red'
redChannel = next(filter(lambda b: b.GetDescription() == 'Red', bands))

# Read the values of the band and flatten to a list
redChannelValues = redChannel.ReadAsArray().flatten()

# Remove NaN values and calculate the median
redChannelMedian = median(filter(lambda x: not isnan(x), redChannelValues))

# Print the result: 0.017926272
print(redChannelMedian)
