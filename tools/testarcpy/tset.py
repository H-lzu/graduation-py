import arcpy

arcpy.ddd.ThinLas(
in_las_dataset="UAV.las",
    target_folder=r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\data",
    thinning_dimension="3D",
    xy_resolution="20 Centimeters",
    z_resolution="20 Centimeters",
    point_selection_method="CLOSEST_TO_CENTER",
    class_codes_weights=None,
    name_suffix="thinned",
    out_las_dataset=r"C:\Users\Administrator\Documents\ArcGIS\Projects\testchm\uavthined.lasd",
    preserved_class_codes=[],
    preserved_flags=None,
    preserved_returns=None,
    excluded_class_codes=[],
    excluded_flags=None,
    excluded_returns=None,
    compression="NO_COMPRESSION",
    remove_vlr="MAINTAIN_VLR",
    rearrange_points="REARRANGE_POINTS",
    compute_stats="COMPUTE_STATS"
)


