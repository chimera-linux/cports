pkgname = "python-dbusmock"
pkgver = "0.30.1"
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
checkdepends = ["python-gobject", "python-pytest"] + depends
pkgdesc = "D-Bus object mocks for python"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://github.com/martinpitt/python-dbusmock"
source = f"https://github.com/martinpitt/python-dbusmock/releases/download/{pkgver}/dist.python-dbusmock-{pkgver}.tar.gz"
sha256 = "aa865e5345aa7626583b83f70e7956c576c24dbc19491ce7fd19281cfef49690"
