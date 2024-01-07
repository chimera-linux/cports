pkgname = "lz4"
pkgver = "1.9.4"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["-j1"]
make_use_env = True
hostmakedepends = ["pkgconf", "gmake"]
provides = [f"liblz4={pkgver}-r{pkgrel}"]
pkgdesc = "LZ4 compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND GPL-2.0-or-later"
url = "https://lz4.github.io/lz4"
source = f"https://github.com/lz4/lz4/archive/v{pkgver}.tar.gz"
sha256 = "0b0e3aa07c8c063ddf40b082bdf7e37a1562bda40a0ff5272957f3e987e0e54b"
hardening = ["vis", "cfi"]
options = ["bootstrap"]


def init_configure(self):
    self.make_build_args += [
        "CFLAGS=" + self.get_cflags(shell=True),
        "LDFLAGS=" + self.get_ldflags(shell=True),
    ]


def post_install(self):
    self.install_license("lib/LICENSE")


@subpackage("lz4-devel")
def _devel(self):
    self.provides = [f"liblz4-devel={pkgver}-r{pkgrel}"]

    return self.default_devel()
