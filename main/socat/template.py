pkgname = "socat"
pkgver = "1.8.1.1"
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
sha256 = "f68b602c80e94b4b7498d74ec408785536fe33534b39467977a82ab2f7f01ddb"
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
