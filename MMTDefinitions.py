# -*- coding: utf-8 -*-
__author__ = 'david.hernandez@uclm.es'

# ICONS: <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/"             title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/"             title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>

CONST_SETTINGS_PLUGIN_NAME = "qAicedrone"
CONST_SETTINGS_FILE_NAME = "qAicedrone.ini"
CONST_PROGRAM_NAME = "AICEDRONE:"
CONST_PROGRAM_TITLE = "AICEDRONE"
CONST_NO_COMBO_SELECT = " ... "
CONST_GRID_SIZE_ACCURACY = 1
CONST_SELECT_ROIS_SHAPEFILES_DIALOG_TITLE = "Select ROIs Shapefiles"
CONST_DOCUMENTS_TYPE_SHAPEFILE = "shp"

CONST_PROJECT_TYPE_ROAD = "Road"
CONST_PROJECT_TYPE_RAILWAY = "Railway"
CONST_PROJECT_TYPE_BREAKWATER = "Breakwater"

CONST_TEMPLATE_PATH = "\\templates"
# CONST_SYMBOLOGY_POINT_CLOUD_TEMPLATE = "\\PointCloudsTools.qml"
# CONST_SYMBOLOGY_TILES_TEMPLATE = "\\Tiles.qml"
CONST_SYMBOLOGY_ROIS_TEMPLATE = "\\ROIs.qml"
CONST_SYMBOLOGY_AI_PAINTS_IMPORT_TEMPLATE = "\\ai_paints_import.qml"
CONST_SYMBOLOGY_CV_PHM_PAINTS_TEMPLATE = "\\cv_phm_paints.qml"
CONST_SYMBOLOGY_AI_ROADS_IMPORT_TEMPLATE = "\\ai_roads_import.qml"
CONST_SYMBOLOGY_AI_ROADS_TEMPLATE = "\\ai_roads.qml"
CONST_SYMBOLOGY_AI_PAINTS_TILES_TEMPLATE = "\\ai_paints_tiles.qml"
CONST_SYMBOLOGY_ROAD_MARKS_TEMPLATE = "\\road_marks.qml"
CONST_SYMBOLOGY_CUBES_TEMPLATE = "\\Cubes.qml"
CONST_SYMBOLOGY_AI_RAILS_IMPORT_TEMPLATE = "\\ai_rails_import.qml"
CONST_SYMBOLOGY_AI_RAILWAYS_IMPORT_TEMPLATE = "\\ai_railways_import.qml"
CONST_SYMBOLOGY_AI_RAILS_TEMPLATE = "\\ai_rails.qml"
CONST_SYMBOLOGY_CV_PHM_RAILS_TEMPLATE = "\\cv_phm_rails.qml"
CONST_SYMBOLOGY_AI_RAILS_TILES_TEMPLATE = "\\ai_rails_tiles.qml"

# CONST_SYMBOLOGY_ELECTRIC_PYLONS_TEMPLATE = "\\ElectricPylons.qml"
# CONST_SYMBOLOGY_ELECTRIC_PYLONS_CONNECTIONS_TEMPLATE = "\\ElectricPylonsConnections.qml"
# # CONST_SYMBOLOGY_IMAGES_PC = "\\images_pc.qml"
# CONST_SYMBOLOGY_PHOTOVOLTAIC_ARRAY_PANELS_TEMPLATE = "\\PhotovoltaicArrayPanels.qml"
# CONST_SYMBOLOGY_PHOTOVOLTAIC_PANELS_TEMPLATE = "\\PhotovoltaicPanels.qml"
# CONST_SYMBOLOGY_PHOTOVOLTAIC_ANOMALIES_TEMPLATE = "\\PhotovoltaicAnomalies.qml"
# CONST_SYMBOLOGY_PHOTOVOLTAIC_ANOMALIES_PANELS_TEMPLATE = "\\PhotovoltaicAnomaliesPanels.qml"
# CONST_SYMBOLOGY_HAZARD_AREAS_TYPES_TEMPLATE = "\\hazard_areas_type.qml"
# CONST_SYMBOLOGY_HAZARD_AREAS_DISTANCES_TEMPLATE = "\\hazard_areas_distances_mean.qml"
# CONST_SYMBOLOGY_HAZARD_AREAS_FALLS_TEMPLATE = "\\hazard_areas_falls_mean.qml"
# CONST_SYMBOLOGY_HAZARD_AREAS_HEIGHTS_TEMPLATE = "\\hazard_areas_heights_mean.qml"

CONST_LINEAR_COARSE_PRECISION = "{:.1f}"

CONST_MANUAL_EDITING_OF_LINEAR_ROAD_MARKS_LAYER_NAME = "Layer for manual editing of linear road markings"
CONST_MANUAL_EDITING_OF_LINEAR_ROAD_MARKS_LAYER_FIELD_WIDTH = "width"
CONST_MANUAL_EDITING_OF_LINEAR_ROAD_MARKS_LAYER_FIELD_CATALOGUE_FILE = "marks_file"
CONST_SYMBOLOGY_MANUAL_EDITING_OF_LINEAR_ROAD_MARKS_LAYER_TEMPLATE = "\\ManualEditingLinearRoadMarks.qml"
CONST_FORM_MANUAL_EDITING_OF_LINEAR_ROAD_MARKS_LAYER_TEMPLATE = "\\ManualEditingLinearRoadMarks.ui"

CONST_MANUAL_EDITING_OF_NON_LINEAR_ROAD_MARKS_LAYER_NAME = "Layer for manual editing of non-linear road markings"
CONST_MANUAL_EDITING_OF_NON_LINEAR_ROAD_MARKS_LAYER_FIELD_ROAD_MARK_ID = "marks_id"
CONST_MANUAL_EDITING_OF_NON_LINEAR_ROAD_MARKS_LAYER_FIELD_ROAD_MARK_CODE = "code"
CONST_MANUAL_EDITING_OF_NON_LINEAR_ROAD_MARKS_LAYER_FIELD_ROAD_MARK_TYPE = "type"
CONST_MANUAL_EDITING_OF_NON_LINEAR_ROAD_MARKS_LAYER_FIELD_CATALOGUE_FILE = "marks_file"
CONST_SYMBOLOGY_MANUAL_EDITING_OF_NON_LINEAR_ROAD_MARKS_LAYER_TEMPLATE = "\\ManualEditingNonLinearRoadMarks.qml"

CONST_POWERLINES_MINIMUM_DISTANCE_BETWEEN_ELECTRIC_PYLONS_TITLE = "Input minimum distance between electric pylons"
CONST_POWERLINES_MINIMUM_DISTANCE_BETWEEN_ELECTRIC_PYLONS_DEFAULT_VALUE = 20.0
CONST_POWERLINES_MINIMUM_DISTANCE_BETWEEN_ELECTRIC_PYLONS_MINIMUM_VALUE = 10.0
CONST_POWERLINES_MINIMUM_DISTANCE_BETWEEN_ELECTRIC_PYLONS_MAXIMUM_VALUE = 150.0

CONST_POWERLINES_ELECTRIC_PYLONS_BASE_RADIUS_DEFAULT_VALUE = 7.5
CONST_POWERLINES_BASE_RADIUS_ELECTRIC_PYLONS_TITLE = "Input electric pylons base radius"
CONST_POWERLINES_BASE_RADIUS_ELECTRIC_PYLONS_DEFAULT_VALUE = CONST_POWERLINES_ELECTRIC_PYLONS_BASE_RADIUS_DEFAULT_VALUE
CONST_POWERLINES_BASE_RADIUS_ELECTRIC_PYLONS_MINIMUM_VALUE = 2.0
CONST_POWERLINES_BASE_RADIUS_ELECTRIC_PYLONS_MAXIMUM_VALUE = 20.0

CONST_POWERLINES_ELECTRIC_PYLONS_HEIGHT_DEFAULT_VALUE = 40.0
CONST_POWERLINES_HEIGHT_ELECTRIC_PYLONS_TITLE = "Input electric pylons height"
CONST_POWERLINES_HEIGHT_ELECTRIC_PYLONS_DEFAULT_VALUE = CONST_POWERLINES_ELECTRIC_PYLONS_HEIGHT_DEFAULT_VALUE
CONST_POWERLINES_HEIGHT_ELECTRIC_PYLONS_MINIMUM_VALUE = 10.0
CONST_POWERLINES_HEIGHT_ELECTRIC_PYLONS_MAXIMUM_VALUE = 80.0

CONST_SELECT_POWER_LINES_FILES_DIALOG_TITLE = "Select Power Lines Files"

CONST_SOLARPARK_REPORT_HOT_SPOTS_COMMAND = "6. Report Hot spots"
CONST_SOLARPARK_REPORT_HOT_SPOTS_CLOSESTS_IMAGE = "Closests image"
CONST_SOLARPARK_REPORT_HOT_SPOTS_MOST_ORTHOGONAL_IMAGE = "Most orthogonal image"
CONST_SOLARPARK_REPORT_HOT_SPOTS_ALL_ARRAYS = "All arrays"
CONST_SOLARPARK_REPORT_HOT_SPOTS_ALL_PANELS = "All panels"
CONST_SOLARPARK_REPORT_HOT_SPOTS_ALL_HOT_SPOTS = "All hot spots"
CONST_SOLARPARK_REPORT_HOT_SPOTS_ALL_IMAGES = "All images"

# CONST_SYMBOLOGY_POINT_CLOUD_TEMPLATE = "/templates/PointCloudsTools.qml"
# CONST_SYMBOLOGY_TILES_TEMPLATE = "/templates/Tiles.qml"
# CONST_SYMBOLOGY_ROIS_TEMPLATE = "/templates/ROIs.qml"
# CONST_SELECT_POINT_CLOUD_FILES_DIALOG_TITLE = "Select Point Cloud Files"
# CONST_DOCUMENTS_TYPE_LASFILE = "las"
# CONST_DOCUMENTS_TYPE_LAZFILE = "laz"
# CONST_PROCESS_LIST_EDITION_DIALOG_TITLE = "Process List Edition"
# CONST_RUN_PROCESS_LIST_DIALOG_TITLE = "Run Process List"
CONST_PROJECT_MANAGEMENT_TEMPORAL_PATH = "/temp"
CONST_PROJECT_MANAGEMENT_OUTPUT_PATH = "/output"
CONST_PROJECT_MANAGEMENT_SLD_FILES_PATH = "/slds"

#
# CONST_SPATIALITE_LAYERS_TILES_TABLE_NAME = "tiles"
# CONST_SPATIALITE_LAYERS_TILES_TABLE_GEOMETRY_COLUMN = "the_geom"
#
# CONST_SPATIALITE_LAYERS_TILE_TABLE_GEOMETRY_COLUMN = "the_geom"
#

CONST_SPATIALITE_LAYERS_ROIS_TABLE_NAME = "rois"
CONST_SPATIALITE_LAYERS_ROIS_TABLE_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_ROAD_MARKS_TABLE_NAME = "road_marks"
CONST_SPATIALITE_LAYERS_ROAD_MARKS_FIELD_ROAD_MARKS_FILE = "marks_file"
CONST_SPATIALITE_LAYERS_ROAD_MARKS_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_ROAD_MARKS_FIELD_ID = "id"
CONST_SPATIALITE_LAYERS_CUBES_TABLE_NAME = "cubes"
CONST_SPATIALITE_LAYERS_CUBES_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_AI_RAILS_IMPORT_TABLE_NAME = "ai_rails_import"
CONST_SPATIALITE_LAYERS_AI_RAILS_IMPORT_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_AI_RAILWAYS_IMPORT_TABLE_NAME = "ai_railways_import"
CONST_SPATIALITE_LAYERS_AI_RAILWAYS_IMPORT_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_AI_RAILS_TILES_TABLE_NAME = "ai_rails_tiles"
CONST_SPATIALITE_LAYERS_AI_RAILS_TILES_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_AI_RAILS_TABLE_NAME = "ai_rails"
CONST_SPATIALITE_LAYERS_AI_RAILS_FIELD_ID = "id"
CONST_SPATIALITE_LAYERS_AI_RAILS_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_CV_PHM_RAILS_TABLE_NAME = "cv_phm_rails"
CONST_SPATIALITE_LAYERS_CV_PHM_RAILS_FIELD_ID = "id"
CONST_SPATIALITE_LAYERS_CV_PHM_RAILS_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_MERGED_RAILS_TABLE_NAME = "merged_rails"
CONST_SPATIALITE_LAYERS_MERGED_RAILS_FIELD_ID = "id"
CONST_SPATIALITE_LAYERS_MERGED_RAILS_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_MERGED_RAILS_TABLE_FIELD_CATEGORY_SIMBOLOGY ="merged_rail_id"
CONST_SPATIALITE_LAYERS_AI_PAINTS_IMPORT_TABLE_NAME = "ai_paints_import"
CONST_SPATIALITE_LAYERS_AI_PAINTS_IMPORT_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_CV_PHM_PAINTS_TABLE_NAME = "cv_phm_paints"
CONST_SPATIALITE_LAYERS_CV_PHM_PAINTS_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_AI_ROADS_IMPORT_TABLE_NAME = "ai_roads_import"
CONST_SPATIALITE_LAYERS_AI_ROADS_IMPORT_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_AI_PAINTS_TILES_TABLE_NAME = "ai_paints_tiles"
CONST_SPATIALITE_LAYERS_AI_PAINTS_TILES_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_AI_ROADS_TABLE_NAME = "ai_roads"
CONST_SPATIALITE_LAYERS_AI_ROADS_GEOMETRY_COLUMN = "the_geom"

CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_TABLE_NAME = "standard_road_marks"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_FIELD_ID = "rowid"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_FIELD_CODE = "code"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_FIELD_TYPE = "type"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_FIELD_ENABLED = "enabled"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_FIELD_WIDTH = "width"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_FIELD_GEOMETRY = "geometry"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_FIELD_TYPE_LONGITUDINAL_SUB_STRING = "longitudinal"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_FIELD_IMG = "img"
CONST_SPATIALITE_LAYERS_STANDARD_ROAD_MARKS_PATH_IMGS = "catalog"

CONST_MODELBREAKWATERDEFINITIONS_COMMAND_CSSHP = "Cubes segmentation for shapefile"
CONST_MODELBREAKWATERDEFINITIONS_COMMAND_RCSHP = "Remove cubes for shapefile"

CONST_MODELRAILWAYDEFINITIONS_COMMAND_CRWSFFPCF = "Compute railway sections from filtered point clouds files"
CONST_MODELRAILWAYDEFINITIONS_COMMAND_RRWSFFPCF = "Remove railway sections from filtered point clouds files"
CONST_MODELRAILWAYDEFINITIONS_COMMAND_CVPHOFSAIR = "3.2 CV and Photogrammetry solution for selected AI rails"
CONST_MODELRAILWAYDEFINITIONS_COMMAND_CVPHOFSAIR_PARAMETER_TAG_SELECTED_RAILS_ID = "CVPHOFSAIR_SelectedRailsId"

CONST_SPATIALITE_LAYERS_ELECTRIC_PYLONS_TABLE_NAME = "pylons"
CONST_SPATIALITE_LAYERS_ELECTRIC_PYLONS_TABLE_GEOMETRY_COLUMN = "the_geom"

CONST_SPATIALITE_LAYERS_ELECTRIC_PYLONS_CONNECTIONS_TABLE_NAME = "pylons_connections"
CONST_SPATIALITE_LAYERS_ELECTRIC_PYLONS_CONNECTIONS_TABLE_GEOMETRY_COLUMN = "the_geom"

CONST_SPATIALITE_LAYERS_HAZARD_AREAS_TABLE_NAME = "hazard_areas"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_TABLE_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_TYPES_LAVER_NAME = "hazard_areas_types"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_DISTANCES_LAVER_NAME = "hazard_areas_distances"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_FALLS_LAVER_NAME = "hazard_areas_falls"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_HEIGHTS_LAVER_NAME = "hazard_areas_heights"

CONST_SPATIALITE_LAYERS_HAZARD_AREAS_MSH_TABLE_NAME = "hazard_areas_msh"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_MSH_TABLE_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_MSH_TYPES_LAVER_NAME = "hazard_areas_msh_types"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_MSH_DISTANCES_LAVER_NAME = "hazard_areas_msh_distances"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_MSH_FALLS_LAVER_NAME = "hazard_areas_msh_falls"
CONST_SPATIALITE_LAYERS_HAZARD_AREAS_MSH_HEIGHTS_LAVER_NAME = "hazard_areas_msh_heights"

CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_ARRAY_PANELS_TABLE_NAME = "arrays"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_PANELS_TABLE_NAME = "panels"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_ARRAY_PANELS_TABLE_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_PANELS_TABLE_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_PV_ANOMALIES_TABLE_NAME = "pv_anomalies"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_PV_ANOMALIES_TABLE_NAME_FIELD_NAME = "name"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_PV_ANOMALIES_TABLE_GEOMETRY_COLUMN = "the_geom"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_PV_ANOMALIES_PANELS_TABLE_NAME = "pv_anomalies_panels"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_PV_ANOMALIES_PANELS_TABLE_NAME_FIELD_NAME = "name"
CONST_SPATIALITE_LAYERS_PHOTOVOLTAIC_PV_ANOMALIES_PANELS_TABLE_GEOMETRY_COLUMN = "the_geom"

CONST_PANELS_LAYER_MINIMUM_SCALE = 100 # 100:1
CONST_PANELS_LAYER_MAXIMUM_SCALE = 0.01 # 100:1

CONST_ANOMALIES_LAYER_MINIMUM_SCALE = 2000 # 100:1
CONST_ANOMALIES_LAYER_MAXIMUM_SCALE = 0.01 # 100:1

CONST_ANOMALIES_PANELS_LAYER_MINIMUM_SCALE = 500 # 100:1
CONST_ANOMALIES_PANELS_LAYER_MAXIMUM_SCALE = 0.01 # 100:1
#
CONST_LAYER_TREE_PROJECT_NAME = "Model Db Project: "

CONST_EGM08_25_FILE_NAME = "egm08_25.gtx"
CONST_EGM08_25_COMPRESS_FILE_NAME = "egm08_25.7z"

CONST_DEFAULT_CRS = "EPSG:25830"
CONST_ELLIPSOID_HEIGHT = "Ellipsoid"
CONST_EPSG_PREFIX = "EPSG:"
CONST_DEFAULT_VERTICAL_CRS = "EPSG:5782"

# CONST_LAYER_TREE_PCTILES_NAME = "Point Cloud Tiles"
#
# CONST_LAYER_PCTILES_FIELD_ID_NAME = "id"
#
# CONST_RCM_REPORT_DEFAULT_SELECTED_CLASSES = "2;3;4;5;6;7"



# CONST_LIDARQC_SELECT_INPUT_LIDAR_FILES_DIALOG_TITLE = "Select Lidar files"
# CONST_LIDARQC_DOCUMENTS_TYPE_LAS = "las"
# CONST_LIDARQC_DOCUMENTS_TYPE_LAZ = "laz"
# CONST_LIDARQC_SELECT_INPUT_SHAPEFILES_DIALOG_TITLE = "Select Shapefiles"
# CONST_LIDARQC_DOCUMENTS_TYPE_SHAPEFILE = "shp"
# CONST_LIDARQC_SPATIALITE_DATABASE_TEMPLATE = "/templates/LidarQC_template.sqlite"
# CONST_COMBOBOX_NO_SELECT_OPTION = " ... "
# CONST_LIDARQC_PROJECT_DEFINITION_DIALOG = "Lidar Quality Control - Project Definition"
# CONST_LIDARQC_SELECT_DATA_DIALOG = "Lidar Quality Control - Select Data"
# CONST_LIDARQC_SYMBOLOGY_TEMPLATE = "/templates/LidarQC.qml"
# CONST_LIDARTILES_SYMBOLOGY_TEMPLATE = "/templates/lidartiles.qml"
