pkgname = "python-dbusmock"
pkgver = "0.34.3"
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
sha256 = "439127291ec4364cbe3c2f58c47987bbe189e9493ccc6d56629bd484e79a6f8b"
