pkgname = "botan"
pkgver = "3.8.0"
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
sha256 = "2af468933ba6b53b1a65696cdae6479f04726c606c19ee8bd0252df3faf07f99"
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
