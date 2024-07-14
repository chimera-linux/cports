pkgname = "python-tldextract"
pkgver = "5.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-filelock",
    "python-idna",
    "python-requests-file",
]
checkdepends = [
    "python-pytest",
    "python-pytest-httpserver",
    "python-pytest-mock",
    "python-pyyaml",
    "python-responses",
    "python-syrupy",
    "python-twisted",
    "python-werkzeug",
    *depends,
]
pkgdesc = "Separates url's subdomain, domain, and public suffix"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/john-kurkowski/tldextract"
source = f"$(PYPI_SITE)/t/tldextract/tldextract-{pkgver}.tar.gz"
sha256 = "c9e17f756f05afb5abac04fe8f766e7e70f9fe387adb1859f0f52408ee060200"


def post_install(self):
    self.install_license("LICENSE")
