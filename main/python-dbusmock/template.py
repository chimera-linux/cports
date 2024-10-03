pkgname = "python-dbusmock"
pkgver = "0.32.2"
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
checkdepends = ["python-gobject", "python-pytest", *depends]
pkgdesc = "D-Bus object mocks for python"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://github.com/martinpitt/python-dbusmock"
source = f"https://github.com/martinpitt/python-dbusmock/releases/download/{pkgver}/dist.python-dbusmock-{pkgver}.tar.gz"
sha256 = "357c269d53a5bb3f87983bec7ff700a0c4d071481f7cf7221ec8376224fc4316"
