pkgname = "botan"
pkgver = "3.4.0"
pkgrel = 1
build_style = "configure"
configure_script = "./configure.py"
configure_args = [
    "--prefix=/usr",
    "--with-boost",
    "--with-bzip2",
    "--with-lzma",
    "--with-os-feature=getrandom",
    "--with-sqlite3",
    "--with-zlib",
]
configure_gen = []
hostmakedepends = [
    "pkgconf",
    "python",
]
makedepends = [
    "boost-devel",
    "bzip2-devel",
    "sqlite-devel",
    "xz-devel",
    "zlib-devel",
]
pkgdesc = "Crypto and TLS for C++"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://botan.randombit.net"
source = f"{url}/releases/Botan-{pkgver}.tar.xz"
sha256 = "71843afcc0a2c585f8f33fa304f0b58ae4b9c5d8306f894667b3746044277557"
# FIXME: cfi
hardening = ["vis"]
# see below
options = []


if self.profile().arch == "ppc64":
    # hangs forever in tests
    options += ["!check"]
    configure_args += ["--disable-modules=aes_power8"]


def post_install(self):
    self.install_license("license.txt")


@subpackage("botan-devel")
def _devel(self):
    return self.default_devel()
