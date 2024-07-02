pkgname = "python-precis-i18n"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Internationalized usernames and passwords"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/byllyfish/precis_i18n"
source = f"$(PYPI_SITE)/p/precis_i18n/precis_i18n-{pkgver}.tar.gz"
sha256 = "7ad0d9e08b806f3a9aba042f0b5b28f081fe6decf1dd95ec8e4dc8c6b302aec2"


def post_install(self):
    self.install_license("LICENSE.txt")
