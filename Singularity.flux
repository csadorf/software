Bootstrap: docker
From: glotzerlab/software:flux

%labels
	MAINTAINER csadorf

%post
	ln -s /usr/bin/python3 /usr/bin/python
	apt-get update && apt-get install -y --no-install-recommends \
		python3-scipy \
		python3-matplotlib \
		python3-mpi4py

%environment
	export LC_ALL=C
