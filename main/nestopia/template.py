pkgname = "nestopia"
pkgver = "1.53.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf-archive", "automake", "pkgconf"]
makedepends = [
    "fltk-devel",
    "fontconfig-devel",
    "glu-devel",
    "libarchive-devel",
    "libepoxy-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libsamplerate-devel",
    "libxft-devel",
    "libxinerama-devel",
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "NES/Famicom emulator"
license = "GPL-2.0-or-later"
url = "http://0ldsk00l.ca/nestopia"
source = f"https://github.com/0ldsk00l/nestopia/archive/{pkgver}.tar.gz"
sha256 = "7783d2673ad496109e7dd3d75756cfef30c5b400409131b83b45c2fa3ddd735b"
tool_flags = {"CXXFLAGS": ["-Wno-c++11-narrowing"]}
