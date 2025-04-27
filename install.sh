conda create -n evalscope python=3.10
conda activate evalscope
pip install -e '.[app]'
pip install vllm