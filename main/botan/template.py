pkgname = "botan"
pkgver = "3.7.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://botan.randombit.net"
source = f"{url}/releases/Botan-{pkgver}.tar.xz"
sha256 = "fc0620463461caaea8e60f06711d7e437a3ad1eebd6de4ac29c14bbd901ccd1b"
hardening = ["vis", "!cfi"]
# see below
options = []


if self.profile().arch == "ppc64":
    # hangs forever in tests
    options += ["!check"]
    configure_args += ["--disable-modules=aes_power8"]


def post_install(self):
    self.install_license("license.txt")


@subpackage("botan-devel")
def _(self):
    return self.default_devel()
