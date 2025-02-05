pkgname = "fio"
pkgver = "3.38"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--disable-native",
    "--prefix=/usr",
]
make_install_args = ["mandir=/usr/share/man"]
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "libaio-devel",
    "linux-headers",
    "numactl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Flexible I/O tester"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/axboe/fio"
source = f"https://github.com/axboe/fio/archive/refs/tags/fio-{pkgver}.tar.gz"
sha256 = "73b3ca18a66fb88a90dae73b9994fdd18d35161d914ffe2089380760af5533cf"
hardening = ["cfi", "vis"]
