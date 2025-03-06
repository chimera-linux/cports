pkgname = "python-watchdog"
pkgver = "6.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pyyaml"]
checkdepends = ["python-pytest"]
pkgdesc = "Python API to monitor file system events"
license = "Apache-2.0"
url = "https://github.com/gorakhargosh/watchdog"
source = f"$(PYPI_SITE)/w/watchdog/watchdog-{pkgver}.tar.gz"
sha256 = "9ddf7c82fda3ae8e24decda1338ede66e1c99883db93711d8fb941eaa2d8c282"
# tests don't run
options = ["!check"]
