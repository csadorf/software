FROM glotzerlab/software:flux

RUN apt-get update && apt-get install -y --no-install-recommends \
  python3-scipy \
  python3-matplotlib \
  python3-mpi4py

ENV LC_ALL=C
