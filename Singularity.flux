Bootstrap: docker
From: glotzerlab/software:flux

%labels
	MAINTAINER csadorf

%post
	ln -s /usr/bin/python3 /usr/bin/python
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade \
		Click==7.0 \
		Keras==2.2.4 \
		rmsd==1.3.0 \
		tensorflow==1.12.0 \
		umap-learn==0.3.6

%environment
	export LC_ALL=C
