pkgname = "fio"
pkgver = "3.35"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--disable-native",
    "--prefix=/usr",
]
make_cmd = "gmake"
make_install_args = ["mandir=/usr/share/man"]
make_check_target = "test"
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "libaio-devel",
    "libnuma-devel",
    "linux-headers",
    "zlib-devel",
]
pkgdesc = "Flexible I/O tester"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://github.com/axboe/fio"
source = f"https://github.com/axboe/fio/archive/refs/tags/fio-{pkgver}.tar.gz"
sha256 = "36b98f35622ee594364bfd9a527523a44cda0dda2455ba9f2dcae2cd7dd3859f"
# FIXME: cfi
hardening = ["vis"]
