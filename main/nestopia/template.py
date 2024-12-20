pkgname = "nestopia"
pkgver = "1.52.1"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["autoconf-archive", "automake", "pkgconf"]
makedepends = [
    "fltk-devel",
    "fontconfig-devel",
    "libarchive-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libxft-devel",
    "sdl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "NES/Famicom emulator"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "http://0ldsk00l.ca/nestopia"
source = f"https://github.com/0ldsk00l/nestopia/archive/{pkgver}.tar.gz"
sha256 = "c9c0bce673eb3b625b538b462e49c00ed1ee1ded1e0bad09be780076880968b5"
tool_flags = {"CXXFLAGS": ["-Wno-c++11-narrowing"]}
