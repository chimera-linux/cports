pkgname = "worker"
pkgver = "5.1.0"
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
maintainer = "logout <logout128@gmail.com>"
license = "GPL-2.0-or-later"
url = "http://www.boomerangsworld.de/cms/worker/index.html"
source = (
    f"http://www.boomerangsworld.de/cms/worker/downloads/worker-{pkgver}.tar.gz"
)
sha256 = "4df7ffd48f51658a36a171ac9eb19e4acebd5bd9cfbbb3850f0175060e91d35b"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
