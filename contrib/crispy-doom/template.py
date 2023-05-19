pkgname = "crispy-doom"
pkgver = "6.0"
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
sha256 = "2b85649c615efeac7573883370e9434255af301222b323120692cb9649b7f420"
# FIXME int cfi
hardening = ["vis", "!cfi", "!int"]
