pkgname = "worker"
pkgver = "5.2.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = [
    "dbus-devel",
    "file-devel",
    "libxft-devel",
    "libxinerama-devel",
    "lua5.4-devel",
    "openssl3-devel",
]
pkgdesc = "Worker file manager"
license = "GPL-2.0-or-later"
url = "http://www.boomerangsworld.de/cms/worker/index.html"
source = (
    f"http://www.boomerangsworld.de/cms/worker/downloads/worker-{pkgver}.tar.gz"
)
sha256 = "c49c5d39be9e12bf2cb9fdeefefa2e6021b34c5ba02692eda0ac8231eba826fe"
hardening = ["cfi", "vis"]
# no tests
# FIXME lintpixmaps
options = ["!check", "!lintpixmaps"]
