pkgname = "graphite2"
pkgver = "1.3.14"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGRAPHITE2_COMPARE_RENDERER=OFF",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
pkgdesc = "Reimplementation of the SIL Graphite text processing engine"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://github.com/silnrsi/graphite"
source = f"{url}/releases/download/{pkgver}/graphite2-{pkgver}.tgz"
sha256 = "f99d1c13aa5fa296898a181dff9b82fb25f6cc0933dbaa7a475d8109bd54209d"
# FIXME int
hardening = ["!int"]


@subpackage("graphite2-devel")
def _(self):
    return self.default_devel()
