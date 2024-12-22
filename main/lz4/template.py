pkgname = "lz4"
pkgver = "1.10.0"
pkgrel = 1
build_style = "makefile"
make_check_args = ["-j1"]
make_use_env = True
hostmakedepends = ["pkgconf"]
provides = [self.with_pkgver("liblz4")]
pkgdesc = "LZ4 compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND GPL-2.0-or-later"
url = "https://lz4.github.io/lz4"
source = f"https://github.com/lz4/lz4/archive/v{pkgver}.tar.gz"
sha256 = "537512904744b35e232912055ccf8ec66d768639ff3abe5788d90d792ec5f48b"
options = ["bootstrap"]


def init_configure(self):
    self.make_build_args += [
        "CFLAGS=" + self.get_cflags(shell=True),
        "LDFLAGS=" + self.get_ldflags(shell=True),
    ]


def post_install(self):
    self.install_license("lib/LICENSE")


@subpackage("lz4-devel")
def _(self):
    self.provides = [self.with_pkgver("liblz4-devel")]

    return self.default_devel()
