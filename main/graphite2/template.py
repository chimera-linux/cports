pkgname = "graphite2"
pkgver = "1.3.15"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGRAPHITE2_COMPARE_RENDERER=OFF",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
checkdepends = ["python-fonttools"]
pkgdesc = "Reimplementation of the SIL Graphite text processing engine"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://github.com/silnrsi/graphite"
source = f"{url}/releases/download/{pkgver}/graphite2-{pkgver}.tgz"
sha256 = "c6bc8b4252724665297f7cad0c55897285c673f9b8e6db3522ace833593fe0b1"
# FIXME int
hardening = ["!int"]


@subpackage("graphite2-devel")
def _(self):
    return self.default_devel()
