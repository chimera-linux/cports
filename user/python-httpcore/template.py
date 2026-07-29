pkgname = "python-httpcore"
pkgver = "1.0.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch-fancy-pypi-readme",
    "python-hatchling",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python",
    "python-certifi",
    "python-h11",
]
pkgdesc = "Minimal low-level HTTP client"
license = "BSD-3-Clause"
url = "https://www.encode.io/httpcore"
source = f"https://pypi.io/packages/source/h/httpcore/httpcore-{pkgver}.tar.gz"
sha256 = "6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8"
# tests require hpack, certifi, anyio...etc, which are not packaged; skip for now
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
