pkgname = "python-precis-i18n"
pkgver = "1.1.2"
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
license = "MIT"
url = "https://github.com/byllyfish/precis_i18n"
source = f"$(PYPI_SITE)/p/precis_i18n/precis_i18n-{pkgver}.tar.gz"
sha256 = "78ef37bff7a8f8374aa65040aac1cedcd60bf97bf4a8113ee713cf72300517b9"


def post_install(self):
    self.install_license("LICENSE.txt")
