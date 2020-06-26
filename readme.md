# OpenTTD port for the 3DS
A port of OpenTTD v0.7.0 to the Nintendo 3DS
## Installation
* Download the latest version of openttd.zip from the releases page.
* Extract its contents to /3ds/ on your SD card.
## Building
* Install DevKitPro/Add DKP packages to your pacman
* Install the 3DS dev depenencies (`dkp-pacman -S 3ds-dev`)
* Install the 3ds-sdl library using (dkp-)pacman
* From the root of the project directory, run:
```bash
./configure --os=N3DS --host $DEVKITARM/bin/arm-none-eabi --enable-static --prefix-dir=$DEVKITPRO --with-sdl --without-png --without-threads --disable-network --disable-unicode --without-libfontconfig --without-zlib --without-libfreetype --without-icu --enable-debug=2
```
(If you are having issues with your sdl, 
specify a path to SDL like this `--with-sdl=/opt/devkitpro/portlibs/3ds/bin/sdl-config`. 
You can find your path by using `dkp-pacman -Ql 3ds-sdl`)

* Type:
```bash
make
```
* Then, in ./bin/ run:
```bash
$DEVKITPRO/tools/bin/3dsxtool openttd openttd.3dsx
```
* You will need to copy the generated folders from bin, the 3dsx file, as well as `openttd.cfg` and the `data` folder into a new folder for distribution. This is also done automatically by the CI.

## Why 0.7.0?
Smaller memory footprint, already a port on DS. This version will be bumped, and compatiblity may only be kept with the new 3ds.
