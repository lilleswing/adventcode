#!/bin/bash
# password=Co**************7!
mkdir ~/.jupyter
cat <<EOT >>  ~/.jupyter/jupyter_notebook_config.json
{
  "NotebookApp": {
    "password": "sha1:7b635dc9fb4d:fa6c7f080e7ccee88894f4b380fdd5a846da0f95"
  }
}
EOT
pip install jupyter
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
