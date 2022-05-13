# Sprachassistent

## General info
This project uses python3.7.<br/>

## Setup on Raspberry PI (tested with Ubuntu 22.04 LTS)

### Install apt packages
```
$ sudo apt-get install libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev portaudio19-dev python-all-dev gcc npm python3-pip git git-lfs
```

### Install Python3.7
```
$ wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz 
$ tar xf Python-3.7.0.tar.xz 
$ cd Python-3.7.0 && ./configure && make && sudo make install
```

### Create virtual python environment and activate it (always let it be activated from now on)
```
$ python3.7 -m venv pyvenv3.7 
$ source pyvenv3.7/bin/activate
```

### Check Python version (should display Python 3.7.0) and upgrade pip
```
$ python -V
$ pip install --upgrade pip
```

### Install Rust and setuptools for SnipsNLU
```
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh 
$ source $HOME/.cargo/env
$ pip install setuptools-rust 
```

### Install Deepspeech from wheel
``` 
$ wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-cp37-cp37m-linux_aarch64.whl 
$ pip install deepspeech-0.9.3-cp37-cp37m-linux_aarch64.whl 
``` 

### Clone Repository and get stt files
``` 
$ clone https://github.com/tlau10/voice_assistant_katja.git
$ cd /voice_assistant_katja
$ wget https://www.dropbox.com/s/zrgkz335z0raotb/de-aashishag-1-prune-kenlm.scorer?dl=0 -o _02_speech_to_text/de-aashishag-1-prune-kenlm.scorer
$ wget https://www.dropbox.com/s/degluxjymq3u6sd/model.tflite?dl=0 -o _02_speech_to_text/model.tflite
$ wget https://www.dropbox.com/s/mg16a7vi6178998/model.pbmm?dl=0 -o _02_speech_to_text/model.pbmm
``` 

### Install pip packages
``` 
$ pip install -r pip_requirements.txt
``` 

### Install SnipsNLU language package de
``` 
$ python -m snips_nlu download de
``` 

### Install Node packages
``` 
$ nmp install axios cheerio
``` 

### Create picovoice.key file
``` 
$ cd _01_wake_word_detection
$ vi picovoice.key
$ insert key from picovoice console: https://console.picovoice.ai/login
$ ZZ
$ cd ..
``` 

### Start the voice assistant
``` 
$ python setup.py
``` 
