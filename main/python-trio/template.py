pkgname = "python-trio"
pkgver = "0.29.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--pyargs",
    "trio",
    "--skip-optional-imports",
    "-k",
    # these fail on ci
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
checkdepends = ["python-pytest", "python-astor", *depends]
pkgdesc = "Python library for async concurrency"
license = "Apache-2.0 OR MIT"
url = "https://github.com/python-trio/trio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "80da11933df9ec7fa8636966b2b4006e936dcf8127cdc97688af10bb1eb6cb24"


def post_install(self):
    self.install_license("LICENSE.MIT")
