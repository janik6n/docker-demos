FROM alpine:3.8

LABEL maintainer "janikarh@gmail.com"

# docker run -d --name alpine-jupyter-01 -p 8888:8888 -v [host-src]:/opt/notebook eipdev/alpine-jupyter-notebook

ENV LANGUAGE=C.UTF-8 LC_ALL=C.UTF-8 LANG=C.UTF-8

COPY requirements.txt /tmp/

RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
	&& apk update && apk upgrade \
	&& apk add --no-cache tini python3 libstdc++ openblas freetype wget ca-certificates \
	&& python3 -m ensurepip && rm -r /usr/lib/python*/ensurepip \
	&& pip3 install --upgrade pip setuptools \
	&& apk add --no-cache --virtual .build-deps@testing python3-dev make cmake clang clang-dev g++ linux-headers libtbb libtbb-dev openblas-dev freetype-dev libxml2-dev libxslt-dev \
	&& export CC=/usr/bin/clang CXX=/usr/bin/clang++ \
	&& ln -s /usr/include/locale.h /usr/include/xlocale.h \
	&& mkdir -p /opt/tmp && cd /opt/tmp \
	&& pip3 install --no-cache-dir -r /tmp/requirements.txt \
	&& jupyter nbextension enable --py widgetsnbextension \
	&& jupyter nbextension enable --py ipysankeywidget \
	&& echo "c.NotebookApp.token = ''" > /root/.jupyter/jupyter_notebook_config.py \
	&& cd /opt && rm -r /opt/tmp && mkdir -p /opt/notebook \
	&& unset CC CXX \
	&& apk del .build-deps \
	&& rm -r /root/.cache \
	&& find /usr/lib/python3.6/ -type d -name tests -depth -exec rm -rf {} \; \
	&& find /usr/lib/python3.6/ -type d -name test -depth -exec rm -rf {} \; \
	&& find /usr/lib/python3.6/ -name __pycache__ -depth -exec rm -rf {} \;

RUN mkdir -p /certs

EXPOSE 8888
WORKDIR /opt/notebook
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--certfile=/certs/server.crt", "--keyfile", "/certs/server.key"]
