pkgname = "worker"
pkgver = "5.0.2"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
hostmakedepends = ["pkgconf"]
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
source = f"http://www.boomerangsworld.de/cms/worker/downloads/{pkgname}-{pkgver}.tar.gz"
sha256 = "9381e0217bb2d2aef6a4784653e02e23009434c1ff89c6ac11758815cff0e4ca"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
