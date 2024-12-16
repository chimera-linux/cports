pkgname = "catatonit"
pkgver = "0.2.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "slibtool",
]
# copied into containers so has to be static to work
makedepends = [
    "libatomic-chimera-devel-static",
    "libunwind-devel-static",
    "musl-devel-static",
]
pkgdesc = "Init for containers"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/openSUSE/catatonit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "771385049516fdd561fbb9164eddf376075c4c7de3900a8b18654660172748f1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_dir("usr/lib/podman")
    self.install_link("usr/lib/podman/catatonit", "../../bin/catatonit")
