pkgname = "lynx"
pkgver = "2.9.2"
pkgrel = 0
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
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Text web browser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://lynx.invisible-island.net"
source = f"https://invisible-mirror.net/archives/lynx/tarballs/lynx{pkgver.replace('_pre', 'dev.')}.tar.bz2"
sha256 = "7374b89936d991669e101f4e97f2c9592036e1e8cdaa7bafc259a77ab6fb07ce"
# CFI: crashes in UCPutUtf8_charstring via magic function pointer stuff
# when -display_charset utf-8 on any website
hardening = ["vis", "cfi", "cfi-genptr"]
options = ["!cross"]
