pkgname = "crispy-doom"
pkgver = "5.12.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "sdl-devel", "sdl_mixer-devel", "sdl_net-devel",
    "libsamplerate-devel", "libpng-devel"
]
pkgdesc = "Limit-removing enhanced-resolution Doom source port"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/fabiangreffrath/crispy-doom"
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "d85d6e76aa949385458b7702e6fb594996745b94032ffb13e1790376eeecb462"

def pre_configure(self):
    self.do("autoreconf", "-if")
