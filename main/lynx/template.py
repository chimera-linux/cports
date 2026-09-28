pkgname = "lynx"
pkgver = "2.9.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-widec",
    "--enable-ipv6",
    "--with-brotli",
    "--with-bzlib",
    "--with-ssl",
    "--with-zlib",
    "--enable-externs",
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
license = "GPL-2.0-or-later"
url = "https://lynx.invisible-island.net"
source = f"https://invisible-mirror.net/archives/lynx/tarballs/lynx{pkgver.replace('_pre', 'dev.')}.tar.bz2"
sha256 = "174b7f2866a60f3247ba75f5c7dbb10b124aede4a1359312de15f3bfebd2050f"
# CFI: crashes in UCPutUtf8_charstring via magic function pointer stuff
# when -display_charset utf-8 on any website
hardening = ["vis", "!cfi"]
options = ["etcfiles", "!cross"]
