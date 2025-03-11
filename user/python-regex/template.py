pkgname = "python-regex"
pkgver = "2025.5.18"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Alternative regular expression module, to replace re"
license = "Apache-2.0"
url = "https://github.com/mrabarnett/mrab-regex"
# outdated pypi source
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4af42040e363348b6df730ba36ea14fcebf9c3dacb09bf71b9af99a06909aa0f"
# FIXME: failing tests
options = ["!check"]
