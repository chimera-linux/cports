pkgname = "libexecinfo"
pkgver = "1.1"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Library for inspecting program's backtrace"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://www.freshports.org/devel/libexecinfo"
source = f"http://distcache.freebsd.org/local-distfiles/itetcu/libexecinfo-{pkgver}.tar.bz2"
sha256 = "c9a21913e7fdac8ef6b33250b167aa1fc0a7b8a175145e26913a4c19d8a59b1f"
# no tests present
options = ["!check"]

@subpackage("libexecinfo-devel")
def _devel(self):
    self.depends += ["libexecinfo"]

    return self.default_devel()
