pkgname = "python-tldextract"
pkgver = "5.2.0"
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
license = "BSD-3-Clause"
url = "https://github.com/john-kurkowski/tldextract"
source = f"$(PYPI_SITE)/t/tldextract/tldextract-{pkgver}.tar.gz"
sha256 = "c3a8c4daf2c25a57f54d6ef6762aeac7eff5ac3da04cdb607130be757b8457ab"


def post_install(self):
    self.install_license("LICENSE")
