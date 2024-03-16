pkgname = "python-tldextract"
pkgver = "5.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    "python-wheel",
]
makedepends = [
    "python-filelock",
    "python-idna",
    "python-requests",
    "python-requests-file",
]
checkdepends = [
    "python-pyyaml",
    "python-pytest",
    "python-pytest-mock",
    "python-twisted",
    "python-responses",
]
pkgdesc = "Separates url's subdomain, domain, and public suffix"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/john-kurkowski/tldextract"
source = f"$(PYPI_SITE)/t/tldextract/tldextract-{pkgver}.tar.gz"
sha256 = "9b6dbf803cb5636397f0203d48541c0da8ba53babaf0e8a6feda2d88746813d4"


def post_install(self):
    self.install_license("LICENSE")
