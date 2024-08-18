pkgname = "powertop"
pkgver = "2.15"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-nls"]
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "autoconf-archive",
    "gettext-devel",
    "libnl-devel",
    "linux-headers",
    "ncurses-devel",
    "pciutils-devel",
]
pkgdesc = "Diagnostic tool for power usage"
maintainer = "stbk <stbk@elia.garden>"
license = "GPL-2.0-only"
url = "https://github.com/fenrus75/powertop"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e58ab3fd7b8ff5f4dd0d17f11848817e7d83c0a6918145ac81de03b5dccf8f49"
