pkgname = "socat"
pkgver = "1.8.0.2"
pkgrel = 0
build_style = "gnu_configure"
# broken
configure_gen = []
make_dir = "."
make_check_target = "test"
makedepends = [
    "linux-headers",
    "openssl3-devel",
    "readline-devel",
]
checkdepends = ["bash", "iproute2", "procps"]
pkgdesc = "Multipurpose relay for binary protocols"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.dest-unreach.org/socat"
source = f"{url}/download/socat-{pkgver}.tar.gz"
sha256 = "e9498367cb765d44bb06be9709c950f436b30bf7071a224a0fee2522f9cbb417"
hardening = ["vis", "cfi"]
# tests have heisenbugs
options = ["!check"]


def post_install(self):
    self.install_dir("usr/share/examples/socat")
    self.mv(
        self.destdir / "usr/bin/socat-*.sh",
        self.destdir / "usr/share/examples/socat",
        glob=True,
    )
