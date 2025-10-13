pkgname = "bash-completion"
pkgver = "2.16.0"
pkgrel = 1
build_style = "gnu_configure"
make_install_args = [
    "profiledir=/usr/share/bash/bashrc.d",
]
hostmakedepends = ["automake", "pkgconf"]
checkdepends = ["bash", "python-pytest", "python-pexpect"]
depends = ["bash"]
pkgdesc = "Programmable completion functions for bash"
license = "GPL-2.0-or-later"
url = "https://github.com/scop/bash-completion"
source = f"{url}/releases/download/{pkgver}/bash-completion-{pkgver}.tar.xz"
sha256 = "3369bd5e418a75fb990863925aed5b420398acebb320ec4c0306b3eae23f107a"
# what's the point (needs a truckload of checkdepends too)
options = ["!check"]
