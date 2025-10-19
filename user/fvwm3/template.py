pkgname = "fvwm3"
pkgver = "1.1.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dmandoc=true",
]
hostmakedepends = ["asciidoctor", "meson", "perl", "pkgconf"]
makedepends = [
    "fribidi-devel",
    "libevent-devel",
    "libpng-devel",
    "librsvg-devel",
    "libxcursor-devel",
    "libxft-devel",
    "libxkbcommon-devel",
    "libxpm-devel",
    "libxrandr-devel",
    "libxt-devel",
    "musl-bsd-headers",
    "xtrans",
]
pkgdesc = "X11 window manager"
license = "GPL-2.0-or-later"
url = "https://github.com/fvwmorg/fvwm3"
source = f"{url}/releases/download/{pkgver}/fvwm3-{pkgver}.tar.gz"
sha256 = "3377bf7ecb2ad4fdbe4e9efde328c3a794894db66f670b9d2b7f03a0010c5de5"
