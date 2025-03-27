pkgname = "nestopia"
pkgver = "1.53.1"
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
sha256 = "21aa45f6c608fe290d73fdec0e6f362538a975455b16a4cc54bcdd10962fff3e"
tool_flags = {"CXXFLAGS": ["-Wno-c++11-narrowing"]}
