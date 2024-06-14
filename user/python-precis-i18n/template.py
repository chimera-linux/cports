pkgname = "python-precis-i18n"
pkgver = "1.1.1"
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
sha256 = "369fe3bcc29ea56ce0b5603e26165d0aabd885168512d92fc08e4f60d716bb31"


def post_install(self):
    self.install_license("LICENSE.txt")
