##
import spatialdata as sd
import os
from napari_spatialdata import Interactive

f = 'scratch/userfolders/lucamarconato/liver/data/ResolveHuman.zarr/'
sdata = sd.read_zarr(f)
Interactive(sdata)
##