pkgname = "worker"
pkgver = "5.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = [
    "dbus-devel",
    "file-devel",
    "libxft-devel",
    "libxinerama-devel",
    "lua5.4-devel",
    "openssl-devel",
]
pkgdesc = "Worker file manager"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://www.boomerangsworld.de/cms/worker/index.html"
source = (
    f"http://www.boomerangsworld.de/cms/worker/downloads/worker-{pkgver}.tar.gz"
)
sha256 = "3d704f9c5c102aabb1c9e9763444175cebe24849d251d46bc7e772a26cca2fe9"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
