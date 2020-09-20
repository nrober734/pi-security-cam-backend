# pi-security-cam-backend
Camera runtime, inference, and streaming for Raspberry pi security camera


## Running the setup script
To bootstrap your pi with docker and conda, run the `pi_setup.sh` script

`./pi_setup.sh`

(You may need to first run `sudo chmod +x pi_setup.sh` to make the script runnable as bash)

When finished, open a new terminal and execute the following:

`conda config --add channels rpi`

`conda update conda`

## TODO: dockerize

## Set up the environment
`sudo pip3 install -r requirements.txt`

## Set up the Pi camera
`sudo raspi-config` > Enable camera interace connection

## Install torch and torchvision

From the `/torch_wheels` directory:

`pip3 install torch-1.4.0a0+7f73f1d-cp37-cp37m-linux_armv7l.whl`


`pip3 install torchvision-0.5.0a0+85b8fbf-cp37-cp37m-linux_armv7l.whl `

## Fixing the package naming bug after torch installation:

This is a documented issue when installing torch on the Pi: [source](https://github.com/pytorch/pytorch/issues/574#issuecomment-274914572)

Run the following commands to fix:

`cd /home/pi/.local/lib/python3.7/site-packages/torch`

`mv _C.cpython-37m-arm-linux-gnueabi.so _C.so`

There is an additional bug with libopenblas fixed [here](https://github.com/sermanet/OverFeat/issues/10#issuecomment-40912417)

Run the following commands to fix:

`sudo apt-get install libopenblas-base`

` export LD_LIBRARY_PATH=/usr/lib/openblas-base/`

Test the installation success with:

`python3`

Then in the Python shell:

`import torch`

`import torchvision`

## Download YOLO model weights

`mkdir weights`

In the `/weights` directory run:

`./download_weights.sh`
