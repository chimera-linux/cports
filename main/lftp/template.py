pkgname = "lftp"
pkgver = "4.9.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-nls",
    "--enable-threads=posix",
    "--with-openssl",
    "--with-modules",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "ncurses-devel",
    "openssl3-devel",
    "readline-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "FTP/HTTP client"
license = "GPL-3.0-or-later"
url = "https://lftp.yar.ru"
source = f"https://lftp.yar.ru/ftp/lftp-{pkgver}.tar.xz"
sha256 = "96e7199d7935be33cf6b1161e955b2aab40ab77ecdf2a19cea4fc1193f457edc"
# tests require internet connection
options = ["etcfiles", "!check"]
