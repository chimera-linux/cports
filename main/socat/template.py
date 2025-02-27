pkgname = "socat"
pkgver = "1.8.0.3"
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
license = "GPL-2.0-only"
url = "http://www.dest-unreach.org/socat"
source = f"{url}/download/socat-{pkgver}.tar.gz"
sha256 = "a9f9eb6cfb9aa6b1b4b8fe260edbac3f2c743f294db1e362b932eb3feca37ba4"
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
