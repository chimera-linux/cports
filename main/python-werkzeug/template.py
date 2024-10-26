pkgname = "python-werkzeug"
pkgver = "3.0.6"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--noconftest",
    # need ephemeral-port-preserve + watchdog
    "--ignore=tests/middleware/test_http_proxy.py",
    "--ignore=tests/test_debug.py",
    "--ignore=tests/test_serving.py",
]
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = [
    "python-markupsafe",
    "python-pytest",
    "python-pytest-timeout",
    "python-requests",
]
depends = ["python-markupsafe"]
pkgdesc = "WSGI swiss-army knife"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "MIT"
url = "https://werkzeug.palletsprojects.com"
source = f"$(PYPI_SITE)/w/werkzeug/werkzeug-{pkgver}.tar.gz"
sha256 = "a8dd59d4de28ca70471a34cba79bed5f7ef2e036a76b3ab0835474246eb41f8d"


def post_install(self):
    self.install_license("LICENSE.txt")
