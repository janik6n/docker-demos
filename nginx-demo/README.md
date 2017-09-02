README
======

Minimal example of running `Nginx` web server in a container.

Directory `src` contains a tiny web page, which will be copied to the container and served when the container is run.

## Usage

Build the image
`docker build -t tiny-nginx .`

... and run as daemon mapping container port `80` to local port `8000`
`docker run -d -p 8000:80 --name my-webserver tiny-nginx`

Stop the container
`docker stop my-webserver`
