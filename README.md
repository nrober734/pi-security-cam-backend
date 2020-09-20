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
## Download YOLO model weights
`mkdir weights`

`./download_weights.sh`
