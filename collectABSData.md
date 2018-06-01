# These steps manual

Manually download the SEIFA dataset for LGAs, 2016

    http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/2033.0.55.0012016?OpenDocument

Should be called `2033055001 - lga indexes.xls`
Move it to data/
Open first sheet, replace "score" with relevant index names, remove colums that have decile in them, highlight relevant area, paste to another sheet, save as csv. There should be these columns left:

    2016 Local Government Area (LGA) Code,
    2016 Local Government Area (LGA) Name,
    Index of Relative Socio-economic Disadvantage,
    Index of Relative Socio-economic Advantage and Disadvantage,
    Index of Economic Resources,
    Index of Education and Occupation,
    Usual Resident Population

Save it at data/

Manually download the ASGS LGA ESRI digital boundaries shapefile

    http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.003July%202017?OpenDocument

Should be called `1270055003_lga_2017_aust_shp.zip`
Move it to data/

Unzip the file:

    unzip data/1270055003_lga_2017_aust_shp.zip -d data/
