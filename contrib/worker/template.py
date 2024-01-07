pkgname = "worker"
pkgver = "4.12.1"
pkgrel = 0
build_style = "configure"
make_cmd = "gmake"
make_install_args = ["prefix=/usr"]
hostmakedepends = ["gmake"]
makedepends = [
    "libxft-devel",
    "dbus-devel",
    "libxinerama-devel",
    "openssl-devel",
]
pkgdesc = "Worker file manager"
maintainer = "logout <logout128@gmail.com>"
license = "GPL-2.0-or-later"
url = "http://www.boomerangsworld.de/cms/worker/index.html"
source = f"http://www.boomerangsworld.de/cms/worker/downloads/{pkgname}-{pkgver}.tar.gz"
sha256 = "d75b52395b86b8253422faa910a88abd4663f43b6358912b2e933c22c4edbdcb"
hardening = ["vis", "cfi"]
