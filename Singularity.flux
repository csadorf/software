Bootstrap: docker
From: glotzerlab/software:flux

%labels
	MAINTAINER csadorf

%post
	ln -s /usr/bin/python3 /usr/bin/python
	apt-get update && apt-get install -y --no-install-recommends \
		libhdf5-dev \
		graphviz \
		locales \
		python3-dev \
		python3-pip \
		python3-scipy \
		python3-matplotlib \
		python3-mpi4py
	python3 -m pip install --upgrade pip
	python3 -m pip install tensorflow
	python3 -m pip install keras
	python3 -m pip install Pillow
	python3 -m pip install scikit-learn
	python3 -m pip install pandas

%environment
	export LC_ALL=C
