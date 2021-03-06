pkgname = "bsddiff"
pkgver = "0.99.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Alternative to GNU diffutils from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdutils"
source = f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9505436bc26b7a9ba7efed7e67194f1fc21ff3b3b4c968277c96d3da25676ca1"
# no test suite
options = ["bootstrap", "!check"]
