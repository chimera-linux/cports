pkgname = "fio"
pkgver = "3.40"
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
license = "GPL-2.0-only"
url = "https://github.com/axboe/fio"
source = f"https://github.com/axboe/fio/archive/refs/tags/fio-{pkgver}.tar.gz"
sha256 = "9fc81e3a490a53fe821d76dd759d64f229d0ac6b4d2c711837bcad158242e3b2"
hardening = ["cfi", "vis"]
