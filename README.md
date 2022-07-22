# connect_iitm_eth
Headlessly authorize your device on IIT-M LAN. 
Currently only supports Linux for the start-up automation because of the systemd dependency. 

# Instructions
- Setup Python3 dependencies. ```pip3 install selenium python-dotenv```
- Update path to main.py in ```connect_iitm.sh```
- Create a ```.env``` file and update username & password. Refer example values in ```.env_example```.
- Give executable permissions to the bash script ```chmod +x connect_iitm.sh```
- Run manually ```connect_iitm.sh```

# Auto-Run on Start-Up using systemd
- Move the systemd service configuration example to ```/etc/systemd/system/connect_eth.service```.
- Edit the path to the bash script. ```/home/your_user/connect_iitm.sh```
- Edit the python path env variable to your site-packages dir. ```/home/my_user/.local/lib/python3.8/site-packages```
- Reload systemd daemon ```systemctl daemon-reload```
- Enable your service ```systemctl enable connect_eth.service```

# Info
- Output will be found in ```/var/log/syslog```. Could be useful for debugging. 