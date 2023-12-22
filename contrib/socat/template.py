pkgname = "socat"
pkgver = "1.8.0.0"
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
pkgdesc = "Multipurpose relay for binary protocols"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "http://www.dest-unreach.org/socat"
source = f"{url}/download/socat-{pkgver}.tar.gz"
sha256 = "6010f4f311e5ebe0e63c77f78613d264253680006ac8979f52b0711a9a231e82"
hardening = ["vis", "cfi"]
# needs a smorgasbord of random network utilities
options = ["!check"]
