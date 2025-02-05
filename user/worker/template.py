pkgname = "worker"
pkgver = "5.2.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://www.boomerangsworld.de/cms/worker/index.html"
source = (
    f"http://www.boomerangsworld.de/cms/worker/downloads/worker-{pkgver}.tar.gz"
)
sha256 = "c6559e08e38f5e59bbd6758ffd4abd8b5c6cc163a0cd7d319a4c19c263164e5d"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
