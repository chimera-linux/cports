pkgname = "lynx"
pkgver = "2.9.0_pre10"
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
sha256 = "898ac82bcfcbd4b20ea39afdf66fd659b8773c7549623b0f8802bf392a41a912"
options = ["!cross"]

# FIXME visibility
hardening = ["!vis"]
