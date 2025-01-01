pkgname = "python-dbusmock"
pkgver = "0.34.2"
pkgrel = 0
build_style = "python_pep517"
# needs upower
make_check_args = ["-k", "not test_dbusmock_test_template"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-dbus"]
checkdepends = [
    "dbus",
    "libnotify",
    "modemmanager",
    "networkmanager",
    "polkit",
    "python-gobject",
    "python-pytest",
    *depends,
]
pkgdesc = "D-Bus object mocks for python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/martinpitt/python-dbusmock"
source = (
    f"{url}/releases/download/{pkgver}/dist.python_dbusmock-{pkgver}.tar.gz"
)
sha256 = "69c3137f15d3397846fd4aeb2e7f41289aa4c7dc2a894502225186d1fcb396ec"
