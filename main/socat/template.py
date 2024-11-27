pkgname = "socat"
pkgver = "1.8.0.1"
pkgrel = 0
build_style = "gnu_configure"
# broken
configure_gen = []
make_dir = "."
make_check_target = "test"
makedepends = [
    "linux-headers",
    "openssl-devel",
    "readline-devel",
]
checkdepends = ["bash", "iproute2", "procps"]
pkgdesc = "Multipurpose relay for binary protocols"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.dest-unreach.org/socat"
source = f"{url}/download/socat-{pkgver}.tar.gz"
sha256 = "dc350411e03da657269e529c4d49fe23ba7b4610b0b225c020df4cf9b46e6982"
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
