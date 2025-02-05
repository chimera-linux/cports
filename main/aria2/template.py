pkgname = "aria2"
pkgver = "1.37.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-libaria2",
    "--disable-werror",
    "--enable-bittorrent",
    "--enable-metalink",
    "--enable-ssl",
    "--enable-websocket",
    "--enable-year2038",
    "--enable-epoll",
    "--enable-largefile",
    "--enable-nls",
    "--enable-rpath",
    "--without-appletls",
    "--without-wintls",
    "--without-libnettle",
    "--without-libgmp",
    "--without-libgcrypt",
    "--without-libexpat",
    "--without-gnutls",
    "--with-libxml2",
    "--with-openssl",
    "--with-libz",
    "--with-libcares",
    "--with-libuv",
    "--with-libssh2",
    "--with-sqlite3",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "c-ares-devel",
    "cppunit-devel",
    "libssh2-devel",
    "libuv-devel",
    "libxml2-devel",
    "openssl3-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Multi-protocol download utility"
maintainer = "nullobsi <nullobsi@unix.dog>"
license = "GPL-2.0-or-later"
url = "https://github.com/aria2/aria2"
source = f"{url}/releases/download/release-{pkgver}/aria2-{pkgver}.tar.xz"
sha256 = "60a420ad7085eb616cb6e2bdf0a7206d68ff3d37fb5a956dc44242eb2f79b66b"
hardening = ["vis", "cfi"]
# Check is broken
options = ["!check"]
