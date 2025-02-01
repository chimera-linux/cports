pkgname = "fvwm3"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-mandoc"]
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = ["asciidoctor", "automake", "libtool", "pkgconf"]
makedepends = [
    "fribidi-devel",
    "libevent-devel",
    "libpng-devel",
    "librsvg-devel",
    "libxcursor-devel",
    "libxft-devel",
    "libxpm-devel",
    "libxrandr-devel",
    "libxt-devel",
    "musl-bsd-headers",
    "xtrans",
]
pkgdesc = "X11 window manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/fvwmorg/fvwm3"
source = f"{url}/releases/download/{pkgver}/fvwm3-{pkgver}.tar.gz"
sha256 = "ecdcf1099bac3e7b1198bdee7542150d378ee333a644c49095e974d819b8d1c3"
