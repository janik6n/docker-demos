README
======

Run a Jupyter notebook server within a container.

## Usage

Build the image
`docker build -t alpine-jupyter:latest .`

... and run as daemon mapping container port `8888` to local port `8888`, and local notebook directory to container as a volume to be able to use local notebooks.
`docker run -d -p 8888:8888 -v /local/path/to/notebook/dir:/opt/notebook --name my-alpine-jupyter alpine-jupyter:latest`

Stop the container
`docker stop my-alpine-jupyter`
