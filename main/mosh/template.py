pkgname = "mosh"
pkgver = "1.4.0"
pkgrel = 21
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "perl",
    "pkgconf",
    "protobuf",
]
makedepends = [
    "abseil-cpp-devel",
    "protobuf-devel",
    "ncurses-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
depends = ["perl"]
pkgdesc = "Mobile shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://mosh.org"
source = f"https://github.com/mobile-shell/mosh/releases/download/mosh-{pkgver}/mosh-{pkgver}.tar.gz"
sha256 = "872e4b134e5df29c8933dff12350785054d2fd2839b5ae6b5587b14db1465ddd"
hardening = ["vis", "cfi"]
