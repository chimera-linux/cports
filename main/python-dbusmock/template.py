pkgname = "python-dbusmock"
pkgver = "0.34.1"
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
source = f"https://github.com/martinpitt/python-dbusmock/releases/download/{pkgver}/dist.python_dbusmock-{pkgver}.tar.gz"
sha256 = "81a0ef601995889842a4549747cf017f058db2c6193d8dd8fbdc4ee57bea4941"
