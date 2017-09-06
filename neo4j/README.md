README
======

Based on this blog post <https://tbgraph.wordpress.com/2017/08/31/neo4j-london-tube-system-analysis/>, let's see how this can be done with Dockerized Neo4j, with the official Docker image.

## Prepare host

We are going to store the data to host among other things. To accomplish this, we need to create few directories under our *work dir (whichever you like it to be)*:
```bash
mkdir data
mkdir logs
mkdir conf
mkdir plugins
```

## Get the initial config

We will need to add new parameter to `neo4j.conf`, so first we need to get our hands on the file as it is now. Luckily we can dump it from the container:
`docker run --rm --volume=$(pwd)/conf:/conf neo4j:3.2.3 dump-config`
... which will "download" the conf to *current host directory*.

Move the file to directory `conf`.

## Download the plugin

In order to use the Graph Algorithm, we need to download it from [GitHub](https://github.com/neo4j-contrib/neo4j-graph-algorithms/) under releases. At the time of writing, the file in question is `graph-algorithms-algo-3.2.2.1.jar`.

Store it in `plugins` directory.

Since we are using Neo4j version 3.2.x, we need to add a line to the conf. From the repo's `README` copy the line `dbms.security.procedures.unrestricted=algo.*` and add it to the `neo4j.conf`.

## Run the container

Now that all prerequisites are in order, it's time to run the container. With the options set as below, 

- the container is run as daemon,
- no authentication is required (we could require it by using `--env NEO4J_AUTH=neo4j/<password>`
 instead)
- data will be stored in `data`,
- logs will be written to `logs`,
- conf will be used from `conf`,
- plugins will be included and run from `plugins`
**on the host** for persistence.

`docker run -d --publish=7474:7474 --publish=7687:7687 --volume=$(pwd)/data:/data --volume=$(pwd)/logs:/logs --volume=$(pwd)/conf:/conf --volume=$(pwd)/plugins:/plugins --env=NEO4J_AUTH=none --name my_neo4j neo4j:3.2.3`

So, with the container running -- we can check the status with `docker ps -a` -- it's time to open a web browser and head to `http://localhost:7474/browser/`. Should all have gone well, we should see Neo4j's web GUI.

We can verify that the plugin have loaded correctly by querying
```CALL dbms.procedures() YIELD name, description, signature
WHERE name STARTS WITH "algo."
RETURN name, description, signature
ORDER BY name
```
... which should list the algorithm procedures.

## Follow the original blog post

Now that we have Neo4j up and running -- with plugins -- it's time to follow the aforementioned blog post and analyze the London Tube data.
