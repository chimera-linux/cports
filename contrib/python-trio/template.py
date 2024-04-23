pkgname = "python-trio"
pkgver = "0.25.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--pyargs",
    "trio",
    "--skip-optional-imports",
    "-k",
    "not test_signals and not test_for_leaking_fds",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-attrs",
    "python-idna",
    "python-outcome",
    "python-sniffio",
    "python-sortedcontainers",
]
checkdepends = ["python-pytest", "python-astor"] + depends
pkgdesc = "Python library for async concurrency"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/python-trio/trio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ca17721f82cea4805846f62bf4d6d27fe1409009c7be86a99e8b9775e74a9a99"


def post_install(self):
    self.install_license("LICENSE.MIT")
