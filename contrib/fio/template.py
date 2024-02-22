pkgname = "fio"
pkgver = "3.36"
pkgrel = 1
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
sha256 = "b34b8f3c5cd074c09ea487ffe3f444e95565c214b34a73042f35b00cbaab0e17"
hardening = ["cfi", "vis"]
