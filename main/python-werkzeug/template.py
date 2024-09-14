pkgname = "python-werkzeug"
pkgver = "3.0.4"
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
sha256 = "34f2371506b250df4d4f84bfe7b0921e4762525762bbd936614909fe25cd7306"


def post_install(self):
    self.install_license("LICENSE.txt")
