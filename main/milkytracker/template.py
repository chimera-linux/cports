pkgname = "milkytracker"
pkgver = "1.05.01"
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
sha256 = "c487fccf6c97c483f5a624c3a408377393fa45a27cca27323425ad71ee689e16"
