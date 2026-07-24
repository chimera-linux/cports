pkgname = "yoshimi"
pkgver = "2.3.6.4"
pkgrel = 0
build_style = "cmake"
cmake_dir = "src"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "argp-standalone",
    "cairo-devel",
    "fftw-devel",
    "fltk-devel",
    "fontconfig-devel",
    "libedit-readline-devel",
    "lv2",
    "mesa-devel",
    "mxml3-devel",
    "pipewire-jack-devel",
]
pkgdesc = "Software synthesizer"
license = "GPL-2.0-or-later"
url = "https://yoshimi.github.io"
source = f"https://github.com/Yoshimi/yoshimi/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "dd6757574df41f4d1297e549fef6a565e62aa7fc42a8fc24641d56bdbe4018f4"


def post_install(self):
    # already installed in usr/share/icons/64x64/apps
    self.uninstall("usr/share/pixmaps/yoshimi.png")
