pkgname = "milkytracker"
pkgver = "1.04.00"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "pipewire-jack-devel",
    "rtmidi-devel",
    "sdl-devel",
]
pkgdesc = "FT2 compatible music tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://milkytracker.github.io"
source = f"https://github.com/milkytracker/MilkyTracker/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "29b9c9572ad8bf8f4add2de19c3f8fb0382738763a92e76f3d01dea82c40ff72"
