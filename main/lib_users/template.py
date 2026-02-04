pkgname = "lib_users"
pkgver = "0.15"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Checks for deleted system libraries still in use"
license = "GPL-2.0-only"
url = "https://codeberg.org/klausman/lib_users"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6b8a61187ae0f2ad22fbe5a2e6c47196a6fab379e65b606cf019d84caa1195d4"
