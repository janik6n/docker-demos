README
======

Run a Jupyter notebook server within a container.

## Usage

Build the image
`docker build --no-cache -t alpine-jupyter:latest .`
or
`docker build --no-cache -t janikarh/alpine-jupyter:1.5tls .`

... and run as daemon mapping container port `8888` to local port `8888`, and local notebook directory to container as a volume to be able to use local notebooks.
`docker run -d -p 8888:8888 -v /local/path/to/notebook/dir:/opt/notebook -v /local/path/to/_dev_certificates:/certs --name jupyters alpine-jupyter:1.5tls`

Stop the container
`docker stop my-alpine-jupyter`

Note:
This image is in Docker Hub. You can run it from there with Jupyter notebooks on the *current directory*:
`docker run -d -p 8888:8888 -v "$(pwd)":/opt/notebook -v /local/path/to/_dev_certificates:/certs --name jupyters janikarh/alpine-jupyter:1.5tls`


Links:
- https://hub.docker.com/_/alpine/
- https://pkgs.alpinelinux.org/packages
- https://hub.docker.com/_/python/