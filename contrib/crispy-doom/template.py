pkgname = "crispy-doom"
# CAUTION: 5.12 hangs when starting new game (at least on ppc64le)
pkgver = "5.11.1"
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
sha256 = "7c5bb36393dec39b9732e53963dadd6bcc3bd193370c4ec5b1c0121df3b38faa"
# FIXME int cfi
hardening = ["vis", "!cfi", "!int"]

def pre_configure(self):
    self.do("autoreconf", "-if")
