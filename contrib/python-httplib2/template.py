pkgname = "python-httplib2"
pkgver = "0.22.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["--forked"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["ca-certificates", "python-pyparsing"]
checkdepends = [
    "ca-certificates",
    "python-cryptography",
    "python-pytest",
    "python-pytest-forked",
    "python-pytest-timeout",
    "python-six",
]
pkgdesc = "HTTP client library for Python"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://httplib2.readthedocs.io"
source = f"$(PYPI_SITE)/h/httplib2/httplib2-{pkgver}.tar.gz"
sha256 = "d7a10bc5ef5ab08322488bde8c726eeee5c8618723fdb399597ec58f3d82df81"


# Makes tests a lot faster but causes them to fail sometimes :/
# def init_check(self):
#     self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    # We patch it to use system cacerts
    self.uninstall(
        f"usr/lib/python{self.python_version}/site-packages/httplib2/cacerts.txt"
    )

    self.install_license("LICENSE")
