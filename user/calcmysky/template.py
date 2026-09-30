pkgname = "calcmysky"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_VERSION=6"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "eigen",
    "glm",
    "qt6-qtbase-devel",
]
pkgdesc = "Atmospheric scattering simulator"
license = "GPL-2.0-or-later"
url = "https://10110111.github.io/CalcMySky"
source = (
    f"https://github.com/10110111/CalcMySky/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "1096f3c6067e05dd8c4df601b745cca5e88b843ad1328938e5dba69c1fcfb84f"


@subpackage("calcmysky-devel")
def _(self):
    return self.default_devel()
