#!/bin/bash
# Needs further testing
# Prerequisites
git clone https://github.com/NVIDIA/NeMo.git
cd NeMo
pip install --editable ".[all]"
cd ..
rm -rf NeMo
pip install -r ./translations/api/requirements.txt
# Download the model
wget https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1736/ensl_GEN_nemo-1.2.6.tar.zst
zstd -d ensl_GEN_nemo-1.2.6.tar.zst
tar -xvf ensl_GEN_nemo-1.2.6.tar
rm ensl_GEN_nemo-1.2.6.tar.zst
# Download data
wget -O data/parabank2.zip http://cs.jhu.edu/\~vandurme/data/parabank-2.0.zip
unzip data/parabank2.zip -d data
rm data/parabank2.zip