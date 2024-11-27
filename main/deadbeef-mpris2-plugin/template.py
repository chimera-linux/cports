pkgname = "deadbeef-mpris2-plugin"
pkgver = "1.16"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "deadbeef-devel",
    "glib-devel",
]
pkgdesc = "Mpris plugin for deadbeef"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/DeaDBeeF-Player/deadbeef-mpris2-plugin"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3218e2adeea56267552f561316d1e243965b3a03481ab4fdbc535b54a97f4865"
# breaks symbols
hardening = ["!vis"]
