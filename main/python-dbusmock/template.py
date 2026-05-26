pkgname = "python-dbusmock"
pkgver = "0.38.1"
pkgrel = 0
build_style = "python_pep517"
# needs upower
make_check_args = [
    "-k",
    "not test_dbusmock_test_template and not test_readme_examples",
]
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
source = f"{url}/releases/download/{pkgver}/python_dbusmock-{pkgver}.tar.gz"
sha256 = "221b65e1c2e48de9fd11bf7e8c165adaf91648f49a11f390d086a498386f2984"
