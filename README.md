## Camera access
Seeing error: `* failed to open vchiq instance`? The runAs user needs to be added to the `video` group:
```
sudo usermod -aG video ggc_user
```

Error: permissions denied when writing the image file? Give write permissions to the runAs user:
```
sudo chown -R ggc_user:ggc_group /home/pi/GreenHouse
```

## Local Deployment
```
sudo /greengrass/v2/bin/greengrass-cli deployment create \
  --recipeDir ./recipes \
  --artifactDir ./artifacts \
  --merge "t20g.CameraPublisher=1.0.0"
```

```
sudo /greengrass/v2/bin/greengrass-cli component stop -n "t20g.CameraPublisher"
```