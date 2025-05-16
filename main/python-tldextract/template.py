pkgname = "python-tldextract"
pkgver = "5.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
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
license = "BSD-3-Clause"
url = "https://github.com/john-kurkowski/tldextract"
source = f"$(PYPI_SITE)/t/tldextract/tldextract-{pkgver}.tar.gz"
sha256 = "b3d2b70a1594a0ecfa6967d57251527d58e00bb5a91a74387baa0d87a0678609"


def post_install(self):
    self.install_license("LICENSE")
