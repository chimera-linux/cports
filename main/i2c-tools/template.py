pkgname = "i2c-tools"
pkgver = "4.4"
pkgrel = 0
build_style = "makefile"
make_build_args = ["EXTRA=py-smbus"]
make_install_args = ["sbindir=/usr/bin", *make_build_args]
hostmakedepends = ["python", "python-setuptools"]
makedepends = ["linux-headers", "python-devel"]
depends = ["perl"]
pkgdesc = "Heterogeneous set of I2C tools and I2C library for Linux"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git"
source = f"https://mirrors.edge.kernel.org/pub/software/utils/i2c-tools/i2c-tools-{pkgver}.tar.xz"
sha256 = "8b15f0a880ab87280c40cfd7235cfff28134bf14d5646c07518b1ff6642a2473"
# no tests
options = ["!check"]


# LGPL-2.1-or-later
@subpackage("i2c-tools-devel")
def _(self):
    return self.default_devel()


# GPL-2.0-only
@subpackage("python-smbus")
def _(self):
    self.pkgdesc = "Python bindings for Linux SMBus access through i2c-dev"
    self.depends += ["python"]
    return ["usr/lib/python3*"]
