pkgname = "python-dbusmock"
pkgver = "0.36.0"
pkgrel = 0
build_style = "python_pep517"
# needs upower
make_check_args = ["-k", "not test_dbusmock_test_template"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
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
license = "LGPL-3.0-or-later"
url = "https://github.com/martinpitt/python-dbusmock"
source = (
    f"{url}/releases/download/{pkgver}/dist.python_dbusmock-{pkgver}.tar.gz"
)
sha256 = "2d3812ee6c1e15607bca882ed5dfcabaac449c1a3b9627080bbab3deefd56fd2"
