pkgname = "milkytracker"
pkgver = "1.05.00"
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
sha256 = "370a33057025a15077cb71d0765f32caa782d760ded94aa495f3019541c32af5"
