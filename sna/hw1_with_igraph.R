# igraph is an R library (you can access it via Python if you prefer)
# How to install R packages:http://cran.r-project.org/doc/manuals/R-admin.html
# On a Mac (and PC) you can simply do it through the GUI.
# For Mac: Packages & Data -> Package Installer -> (search for igraph)
# once the igraph package is installed, you can load it
library(igraph)

# read in the .gml file
G = read.graph(file=file.choose(),format="gml")

# get the vitals on the graph you just imported
summary(G)

# check out the function no.clusters for the number of connected components

# look at cluster.distribution for the sizes of the connected components

# degree.distribution should give you the number of nodes with each specific edge count