pkgname = "python-authheaders"
pkgver = "0.16.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-authres",
    "python-dkimpy",
    "python-dnspython",
    "python-publicsuffix2",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Library for the generation of email auth headers"
license = "BSD-3-Clause"
url = "https://github.com/ValiMail/authentication-headers"
source = f"$(PYPI_SITE)/a/authheaders/authheaders-{pkgver}.tar.gz"
sha256 = "118edc6d3cb1ad18ffab3d788ccc562fca2854cd645faab08fc47033c648148a"


def post_install(self):
    self.install_license("COPYING")
