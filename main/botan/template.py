pkgname = "botan"
pkgver = "3.8.1"
pkgrel = 0
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
hostmakedepends = [
    "pkgconf",
    "python",
]
makedepends = [
    "boost-devel",
    "bzip2-devel",
    "sqlite-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Crypto and TLS for C++"
license = "BSD-2-Clause"
url = "https://botan.randombit.net"
source = f"{url}/releases/Botan-{pkgver}.tar.xz"
sha256 = "b039681d4b861a2f5853746d8ba806f553e23869ed72d89edbfa3c3dbfa17e68"
hardening = ["vis", "!cfi"]
# see below
options = []


if self.profile().arch == "ppc64":
    # hangs the compiler (no lto)/linker (lto)
    broken = "idc"
    configure_args += ["--disable-modules=aes_power8"]


def post_install(self):
    self.install_license("license.txt")


@subpackage("botan-devel")
def _(self):
    return self.default_devel()
