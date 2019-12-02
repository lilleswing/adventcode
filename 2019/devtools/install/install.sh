#!/usr/bin/env bash

export ENV_NAME=${ENV_NAME:-aoc2019}
export CONDA_URL=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

unamestr=`uname`
if [[ "$unamestr" == 'Darwin' ]];
then
    echo "Using OSX Conda"
    export CONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
    export CPU_ONLY=1
fi

export CONDA_EXISTS=`which conda`
if [[ "$CONDA_EXISTS" = "" ]];
then
    wget ${CONDA_URL} -O anaconda.sh;
    bash anaconda.sh -b -p `pwd`/anaconda
    export PATH=`pwd`/anaconda/bin:$PATH
else
    echo "Using Existing Conda"
fi

conda config --add channels conda-forge
if [[ $NO_ENV -eq 0 ]]; then
    conda create -y --name $ENV_NAME delegator
    source activate $ENV_NAME
else
    conda install -y -q delegator
fi

python devtools/install/conda_install_from_json.py devtools/install/requirements.json
