pkgname = "botan"
pkgver = "3.5.0"
pkgrel = 2
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://botan.randombit.net"
source = f"{url}/releases/Botan-{pkgver}.tar.xz"
sha256 = "67e8dae1ca2468d90de4e601c87d5f31ff492b38e8ab8bcbd02ddf7104ed8a9f"
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
