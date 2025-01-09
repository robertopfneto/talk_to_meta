
conda create --name tf python=3.9
conda activate tf

conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0

pip install --upgrade pip

pip install "tensorflow<2.11"

pip install matplotlib pandas

pip install "numpy<2"
