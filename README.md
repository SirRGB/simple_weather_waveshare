A simple weather display for the waveshare 7.5" V2 model
--
This project is still in early progress, so dont expect full support just yet.


Initial Setup  
--

Install git and configure user if needed  
This guides assumes you are running a Debian based distro  
like Raspberry Pi OS (Lite) with GPIO support
```
cd ${HOME}
sudo apt update && sudo apt upgrade
sudo apt install git
git clone https://github.com/SirRGB/simple_weather_waveshare.git
```
Enable GPIO and install Python dependencies
```
cd ${HOME}/simple_weather_waveshare
sudo apt install python3 python3-venv
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
sudo raspi-config nonint do_spi 0  #This enables SPI
sudo reboot
```
Customize configs
```
cp ${HOME}/simple_weather_waveshare/config.ini.example ${HOME}/simple_weather_waveshare/config.ini
nano ${HOME}/simple_weather_waveshare/config.ini
```


Shedule using SystemD (prefered)
```
mkdir -p ~/.config/systemd/user/
cp simple-weather.* ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable simple-weather.timer
loginctl enable-linger
```

... or using crontab
```
crontab -e
```
and then enter (adjust to your home directory if needed)
```
* * * * * /home/pi/simple_weather_waveshare/main.py
```

Features implemented so far:
- Clock and date functionality
- Minutely refresh using systemd timer

ToDo:
- Display weather data
- [Partial/fast refresh](https://github.com/waveshareteam/e-Paper/blob/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd7in5_V2.py)
- Only refresh when certain bt devices are near
- [Ruuvi Tag support](https://github.com/sevesalm/eInk-weather-display/blob/master/eInk-weather-display/sensor_data.py)

Credits
- [sevesalm/eInk-weather-display](https://github.com/sevesalm/eInk-weather-display)
- [mendhak/waveshare-epaper-display](https://github.com/mendhak/waveshare-epaper-display)
- [waveshareteam/e-Paper](https://github.com/waveshareteam/e-Paper/tree/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd)
