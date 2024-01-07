pkgname = "socat"
pkgver = "1.8.0.0"
pkgrel = 1
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "http://www.dest-unreach.org/socat"
source = f"{url}/download/socat-{pkgver}.tar.gz"
sha256 = "6010f4f311e5ebe0e63c77f78613d264253680006ac8979f52b0711a9a231e82"
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
