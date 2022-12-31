##
import os
import tifffile

# to fix paths in Luca's machine:
# os.chdir('scratch/userfolders/lucamarconato/mouse_brain')

# geopandas hack
os.environ["USE_PYGEOS"] = "0"
import geopandas

import spatialdata as sd
import numpy as np
import pyarrow as pa
import dask_image.imread
import shutil
import pandas as pd

##
# check can find the data
f = "../../../datasets/mouse_brain/"
assert '1198980035' in os.listdir(f)

##
df = pd.read_csv(os.path.join(f, '10xv3_anno.csv'))
##
from pprint import pprint

pprint(dict(df.iloc[0]))

##
# # extract the data
# os.makedirs("data", exist_ok=True)
# os.system(f"tar -xvf {f}ResolveData_HCA.tar -C data")
# ##
# def create_points_element(path: str) -> pa.Table:
#     from pyarrow.csv import read_csv, ReadOptions, ParseOptions
#
#     table = read_csv(
#         path,
#         read_options=ReadOptions(autogenerate_column_names=True),
#         parse_options=ParseOptions(delimiter="\t"),
#     )
#
#     table = table.rename_columns(["x", "y", "z", "gene", ""]).drop([""])
#
#     xyz = table.to_pandas()[["x", "y", "z"]].to_numpy().astype(np.float32)
#     gene = pa.Table.from_pydict({"gene": table.column("gene").dictionary_encode()})
#
#     t = sd.PointsModel.parse(coords=xyz, annotations=gene)
#     return t
#
#
# organisms = ["ResolveHuman", "ResolveMouse"]
# for o in organisms:
#     points = {}
#     images = {}
#     for filename in os.listdir(f"data/ResolveData_HCA/{o}"):
#         if filename.endswith(".txt"):
#             element = create_points_element(f"data/ResolveData_HCA/{o}/{filename}")
#             points[filename.replace('.txt', '')] = element
#             print(filename, f'converted to Points element ({type(element)}')
#         elif filename.endswith(".tiff"):
#             im = dask_image.imread.imread(f"data/ResolveData_HCA/{o}/{filename}")
#             name = filename.replace(".tiff", "")
#             element = sd.Image2DModel.parse(im, dims=("c", "y", "x"), multiscale_factors=[2, 4, 8, 16], name=name)
#             images[name] = element
#             print(filename, f'converted to Image element ({type(element)})')
#     sdata = sd.SpatialData(points=points, images=images)
#     if os.path.isdir(f'{o}.zarr'):
#         shutil.rmtree(f'{o}.zarr')
#     print(f"saving SpatialData object to {o}.zarr")
#     sdata.write(f"{o}.zarr")
#     print('done')
#
# ##
# interactive visualization with napari (doesn't work in JupyterLab)
from napari_spatialdata import Interactive
sdata = sd.SpatialData.read("ResolveHuman.zarr")
Interactive(sdata)

##