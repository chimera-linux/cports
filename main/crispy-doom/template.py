pkgname = "crispy-doom"
pkgver = "7.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "libpng-devel",
    "libsamplerate-devel",
    "sdl2-compat-devel",
    "sdl2_mixer-devel",
    "sdl2_net-devel",
]
pkgdesc = "Limit-removing enhanced-resolution Doom source port"
license = "GPL-2.0-or-later"
url = "https://github.com/fabiangreffrath/crispy-doom"
source = f"{url}/archive/crispy-doom-{pkgver}.tar.gz"
sha256 = "f0eb02afb81780165ddc81583ed5648cbee8b3205bcc27e181b3f61eb26f8416"
hardening = ["vis", "!cfi", "!int"]
