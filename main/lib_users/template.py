pkgname = "lib_users"
pkgver = "0.15"
pkgrel = 1
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/klausman/lib_users"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d17f6d2ab633cf5826921c2757e33806495c1db076e13c16c4bc6c6a73d6e2fe"
