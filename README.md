# pi-security-cam-backend
Camera runtime, inference, and streaming for Raspberry pi security camera


## Running the setup script
To bootstrap your pi with docker and conda, run the `pi_setup.sh` script

`./pi_setup.sh`

(You may need to first run `sudo chmod +x pi_setup.sh` to make the script runnable as bash)

When finished, open a new terminal and execute the following:

`conda config --add channels rpi`

`conda update conda`
