pkgname = "python-chess"
pkgver = "1.11.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["stockfish"]
pkgdesc = "Pure Python chess library with move generation and validation"
license = "GPL-3.0-or-later"
url = "https://github.com/niklasf/python-chess"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cd920994700e700c0354f56b73a2591f652a44fa2ff28552d89c975bd820c647"
# tests not runnable >=3.13
options = ["!check"]
