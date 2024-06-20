# Knowledge Engineering Project
Repository for the Knowledge Engineering project of group 6. Contains data used to create
a property graph in order to answer questions regarding NS and train stations in the
Netherlands.

In the "data" folder there is a mix of our source files as well intermediary data files
we created in order to generate the property graph. Note that source dataset which
we used to compute the daily capacity and retrieve the stations is not present as it
exceeded GitHub's file size limitations.

In the "network_data" folder there are the final files we uploaded to Neo4j's Workplace
to create the property graph. Each file represents a node type or a relationship type.
There is also the .dump file that Neo4j creates to represent the whole property graph.
The file can be loaded in Neo4j to open the property graph directly.

The "scripts" folder contains some of the code we wrote to filter, process and analyse our source data. Not all the steps
are present as some of the data files are not present and also because the creation of the final datasets was done in multiple
small parts.

