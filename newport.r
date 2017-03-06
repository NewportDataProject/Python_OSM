## basic newport network stuff

library(igraph)
library(wellknown)
library(tidyr)
library(plotly)

## will be working off of example from:
## https://plot.ly/r/network-graphs/
## for plotting

newport <- read_graph("newport_streets.gml", format="gml")

E(newport)$between.default <- edge_betweenness(newport)
E(newport)$between.length <- edge_betweenness(newport, weights=E(newport)$length)

## trying with max speed weights
maxspeedw <- as.numeric(sapply(E(newport)$maxspeed, gsub, pattern="mph", replacement=""))

## replace missing values with citywide speed (25mph)
maxspeedw <- ifelse(is.na(maxspeedw), 25, maxspeedw)

E(newport)$between.maxspeed <- edge_betweenness(newport,weights=maxspeedw)


getGGPlotFrame <- function(graphz) {
    ## need to work with the edge dataframe
    retdf <- as_data_frame(graphz)
    
    retdf$x1 <- V(graphz)[retdf$from]$x
    retdf$y1 <- V(graphz)[retdf$from]$y
 
    retdf$x2 <- V(graphz)[retdf$to]$x
    retdf$y2 <- V(graphz)[retdf$to]$y

   ## tempjson <- wkt2geojson(retdf$geostr)
    

    gather(retdf, key=variable, value=value,
           between.default, between.length, between.maxspeed)
}

plotdf <- getGGPlotFrame(newport)

ggplot(plotdf) +
    geom_segment(aes(x=x1,xend=x2,y=y1,yend=y2,color=value)) +
    facet_wrap(~variable) +
    scale_color_distiller(type="seq",direction=1) +
    theme_classic() +
    coord_equal()

## let's try this with plotly!
getPlotlyFrame <- function(graphz) {
    ## need to work with the edge dataframe
    retdf <- as_data_frame(graphz)
    
    retdf$x1 <- V(graphz)[retdf$from]$x
    retdf$y1 <- V(graphz)[retdf$from]$y
 
    retdf$x2 <- V(graphz)[retdf$to]$x
    retdf$y2 <- V(graphz)[retdf$to]$y

    xlists <- apply(retdf,1,function(row){c(row["x1"],row["x2"],NULL)})
    ylists <- apply(retdf,1,function(row){c(row["y1"],row["y2"],NULL)})
 
    geostrfn <- function(x){
        if(nchar(x) ==0){list(character(0))}
        else{wkt2geojson(x)$geometry$coordinates}
    }
    geolists <- lapply(retdf$geostr, geostrfn)
   
    retdf <- unnest(retdf,geolist=geolists)
    
    retdf <- unnest(retdf, xlist=xlists, ylist=ylists)
    
    retdf
}

test <- getPlotlyFrame(newport)

plot_ly(plotdf, x=~
