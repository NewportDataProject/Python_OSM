# Python_OSM
Working with OpenStreetMap in python

## Setting Up The Conda Environment
The `osmnx` package has some fickle dependencies (for windows, anyway). Start by building a conda env like so:

```
> conda create -n OSM python=3.5
```
Then follow the instructions [here](http://geoffboeing.com/2014/09/using-geopandas-windows/) to install `GDAL` and `fiona`.
Where it calls for setting the `PATH` environmental variable in the instructions, use [this](https://conda.io/docs/using/envs.html#saved-environment-variables)
then add the following line to to the `activate.d\env_var.bat` file you created:
```
set PATH=%PATH%;<path/to/omgeo/in/env>
```
Then activate the conda environment and run `pip install -r pip_requirements.txt`
