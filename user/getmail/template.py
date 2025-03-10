pkgname = "getmail"
pkgver = "6.19.07"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Mail retrieval system"
license = "GPL-2.0-only"
url = "https://getmail6.org"
source = (
    f"https://github.com/getmail6/getmail6/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "afc7c7dd061fccab2968b4b0a30ea025c7123a4722ea0a73fb6e3f9e6d8250cd"
