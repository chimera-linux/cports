pkgname = "python-dbusmock"
pkgver = "0.33.0"
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
checkdepends = ["dbus", "python-gobject", "python-pytest", *depends]
pkgdesc = "D-Bus object mocks for python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/martinpitt/python-dbusmock"
source = f"https://github.com/martinpitt/python-dbusmock/releases/download/{pkgver}/dist.python-dbusmock-{pkgver}.tar.gz"
sha256 = "04efd311dd1063ac2b8f7baa79a026b5c0aa3ed4ef18cd9226f52a273fa6193a"
