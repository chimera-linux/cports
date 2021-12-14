pkgname = "crispy-doom"
pkgver = "5.10.3"
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
sha256 = "eef8dc26e8952b23717be3b20239fda4ee59842511328387766d1c8fe8252f6b"

def pre_configure(self):
    self.do("autoreconf", "-if")
