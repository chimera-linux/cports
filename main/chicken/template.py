pkgname = "chicken"
pkgver = "5.4.0"
pkgrel = 0
build_style = "makefile"
depends = [self.with_pkgver("chicken-devel")]
pkgdesc = "Practical and portable Scheme system"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://call-cc.org"
source = f"https://code.call-cc.org/releases/{pkgver}/chicken-{pkgver}.tar.gz"
sha256 = "3c5d4aa61c1167bf6d9bf9eaf891da7630ba9f5f3c15bf09515a7039bfcdec5f"
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
def _(self):
    return self.default_devel()


@subpackage("chicken-libs")
def _(self):
    return self.default_libs(extra=["usr/lib/chicken"])
