pkgname = "lynx"
pkgver = "2.9.0"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--enable-widec",
    "--enable-ipv6",
    "--with-brotli",
    "--with-bzlib",
    "--with-ssl",
    "--with-zlib",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "brotli-devel",
    "bzip2-devel",
    "libidn2-devel",
    "ncurses-devel",
    "openssl-devel",
    "zlib-devel",
]
pkgdesc = "Text web browser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://lynx.invisible-island.net"
source = f"https://invisible-mirror.net/archives/{pkgname}/tarballs/{pkgname}{pkgver.replace('_pre', 'dev.')}.tar.bz2"
sha256 = "5bcae5e2e6043ca7b220963a97763c49c13218d849ffda6be7739bfd5a2d36ff"
# FIXME cfi: crashes in UCPutUtf8_charstring via magic function pointer stuff
# when -display_charset utf-8 on any website
hardening = ["vis", "cfi", "cfi-genptr"]
options = ["!cross"]
