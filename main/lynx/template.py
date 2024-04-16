pkgname = "lynx"
pkgver = "2.9.1"
pkgrel = 1
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
sha256 = "a6db9b22c20df435df3757925a505531ce9a514d134742e935d71aa5c41339c5"
# FIXME cfi: crashes in UCPutUtf8_charstring via magic function pointer stuff
# when -display_charset utf-8 on any website
hardening = ["vis", "cfi", "cfi-genptr"]
options = ["!cross"]
