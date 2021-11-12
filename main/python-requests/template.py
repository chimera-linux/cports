pkgname = "python-requests"
pkgver = "2.26.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = [
    "ca-certificates", "python-charset-normalizer",
    "python-urllib3", "python-idna"
]
pkgdesc = "Python HTTP library for human beings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://python-requests.org"
source = f"$(PYPI_SITE)/r/requests/requests-{pkgver}.tar.gz"
sha256 = "b8aa58f8cf793ffd8782d3d8cb19e66ef36f7aba4353eec859e74678b01b07a7"
