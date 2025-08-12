A simple weather display for the waveshare 7.5" V2 model
--


Using SystemD (prefered)
```
mkdir -p ~/.config/systemd/user/
cp simple-weather.* ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable simple-weather.timer
loginctl enable-linger
```

Using crontab
```
crontab -e
```
and then enter
```
* * * * * /home/pi/simple_weather_waveshare/main.py
```

Features implemented so far:
- Clock and date functionality
- Minutely refresh using systemd timer

ToDo:
- Display weather data
- Read data from config.ini
- Partial/fast refresh
- Only refresh when certain bt devices are near

Credits
- [sevesalm/eInk-weather-display](https://github.com/sevesalm/eInk-weather-display)
- [mendhak/waveshare-epaper-display](https://github.com/mendhak/waveshare-epaper-display)
- [waveshareteam/e-Paper](https://github.com/waveshareteam/e-Paper/tree/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd)
