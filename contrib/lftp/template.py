pkgname = "lftp"
pkgver = "4.9.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-nls",
    "--enable-threads=posix",
    "--with-openssl",
    "--with-modules",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "ncurses-devel",
    "openssl-devel",
    "readline-devel",
    "zlib-devel",
]
pkgdesc = "FTP/HTTP client"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "GPL-3.0-or-later"
url = "https://lftp.yar.ru"
source = f"https://lftp.yar.ru/ftp/lftp-{pkgver}.tar.xz"
sha256 = "c517c4f4f9c39bd415d7313088a2b1e313b2d386867fe40b7692b83a20f0670d"
# tests require internet connection
options = ["!check"]
