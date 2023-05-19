pkgname = "lynx"
pkgver = "2.9.0_pre12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-widec", "--enable-ipv6", "--with-zlib", "--with-bzlib",
    "--with-ssl"
]
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "libbz2-devel", "ncurses-devel", "openssl-devel"
]
pkgdesc = "Text web browser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://lynx.invisible-island.net"
source = f"http://invisible-mirror.net/archives/{pkgname}/tarballs/{pkgname}{pkgver.replace('_pre', 'dev.')}.tar.bz2"
sha256 = "a6455b159d00776d8ec1051285c972dc1f0c552d0571a0cff02a23ec146ee8e5"
hardening = ["vis", "cfi"]
options = ["!cross"]

configure_gen = []
