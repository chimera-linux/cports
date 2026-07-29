pkgname = "python-httpx"
pkgver = "0.28.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-h11",
    "python-hatch-fancy-pypi-readme",
    "python-hatchling",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python",
    "python-anyio",
    "python-certifi",
    "python-h11",
    "python-httpcore",
    "python-idna",
    "python-sniffio",
]
pkgdesc = "Next-generation HTTP client for Python"
license = "BSD-3-Clause"
url = "https://www.python-httpx.org"
source = f"https://pypi.io/packages/source/h/httpx/httpx-{pkgver}.tar.gz"
sha256 = "75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc"
# tests require hpack, certifi, anyio...etc, which are not packaged; skip for now
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
