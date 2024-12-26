pkgname = "nestopia"
pkgver = "1.53.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf-archive", "automake", "pkgconf"]
makedepends = [
    "fltk-devel",
    "fontconfig-devel",
    "libarchive-devel",
    "libepoxy-devel",
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
sha256 = "27a26a6fd92e6acc2093bbd6c1e3ab7f2fff419d9ed6de13bc43349b52e1f705"
tool_flags = {"CXXFLAGS": ["-Wno-c++11-narrowing"]}
