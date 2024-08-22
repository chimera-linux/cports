pkgname = "fio"
pkgver = "3.37"
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
    "libnuma-devel",
    "linux-headers",
    "zlib-ng-compat-devel",
]
pkgdesc = "Flexible I/O tester"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://github.com/axboe/fio"
source = f"https://github.com/axboe/fio/archive/refs/tags/fio-{pkgver}.tar.gz"
sha256 = "b59099d42d5c62a8171974e54466a688c8da6720bf74a7f16bf24fb0e51ff92d"
hardening = ["cfi", "vis"]
