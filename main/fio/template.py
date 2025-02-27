pkgname = "fio"
pkgver = "3.39"
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
sha256 = "e2f4ff137061b44ceb83a55eb9ca8856fe188db6d9b00cb59f8629c9162afe0a"
hardening = ["cfi", "vis"]
