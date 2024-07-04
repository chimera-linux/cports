pkgname = "chicken"
pkgver = "5.3.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
depends = [f"chicken-devel={pkgver}-r{pkgrel}"]
pkgdesc = "Practical and portable Scheme system"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://call-cc.org"
source = f"https://code.call-cc.org/releases/{pkgver}/chicken-{pkgver}.tar.gz"
sha256 = "c3ad99d8f9e17ed810912ef981ac3b0c2e2f46fb0ecc033b5c3b6dca1bdb0d76"
# parallel build unsupported
options = ["!parallel"]


def init_build(self):
    self.make_env = {
        "C_COMPILER": self.get_tool("CC"),
        "CXX_COMPILER": self.get_tool("CXX"),
        "C_COMPILER_OPTIMIZATION_OPTIONS": self.get_cflags(shell=True),
        "LINKER_OPTIONS": self.get_ldflags(shell=True),
    }


def post_install(self):
    self.install_license("LICENSE")
    self.rename(
        "usr/share/chicken/doc", "usr/share/doc/chicken", relative=False
    )


@subpackage("chicken-devel")
def _devel(self):
    return self.default_devel()


@subpackage("chicken-libs")
def _libs(self):
    return self.default_libs(extra=["usr/lib/chicken"])
