pkgname = "python-tldextract"
pkgver = "5.1.3"
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
sha256 = "d43c7284c23f5dc8a42fd0fee2abede2ff74cc622674e4cb07f514ab3330c338"


def post_install(self):
    self.install_license("LICENSE")
