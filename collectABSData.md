# These steps manual

Manually download the SEIFA dataset for LGAs, 2016

    http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/2033.0.55.0012016?OpenDocument

Should be called `2033055001 - lga indexes.xls`
Open first sheet, replace "score" with relevant index names, remove colums that have decile in them, highlight relevant area, paste to another sheet, save as csv. There should be these columns left:

    2016 Local Government Area (LGA) Code,
    2016 Local Government Area (LGA) Name,
    Index of Relative Socio-economic Disadvantage,
    Index of Relative Socio-economic Advantage and Disadvantage,
    Index of Economic Resources,
    Index of Education and Occupation,
    Usual Resident Population

Save it at data/lgaSeifa.csv

Manually download the ASGS LGA ESRI digital boundaries shapefile for 2016

    http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.003July%202016?OpenDocument

Should be called `1270055003_lga_2016_aust_shape.zip`

Unzip the file:

    unzip data/1270055003_lga_2016_aust_shape.zip -d data/

