# remember to update files/ckms.ini
pkgname = "v4l2loopback"
pkgver = "0.13.2"
pkgrel = 1
build_style = "makefile"
make_build_target = "utils"
make_install_target = "install-extra"
hostmakedepends = ["help2man"]
makedepends = ["linux-headers"]
pkgdesc = "Kernel module to create V4L2 loopback devices"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/umlaeute/v4l2loopback"
source = f"https://github.com/umlaeute/v4l2loopback/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1e57e1e382d7451aa2a88d63cc9f146eab1f425b90e76104d4c3d73127e34771"
# no testsuite
options = ["!check"]

broken = "tmp"


def post_install(self):
    # install ckms source tree
    self.install_dir(f"usr/src/{pkgname}-{pkgver}")
    for file in (
        "Kbuild",
        "Makefile",
        "v4l2loopback.c",
        "v4l2loopback.h",
        "v4l2loopback_formats.h",
        self.files_path / "ckms.ini",
    ):
        self.install_file(file, f"usr/src/{pkgname}-{pkgver}")


@subpackage("v4l2loopback-devel")
def _(self):
    return self.default_devel()


@subpackage("v4l2loopback-ckms")
def _(self):
    self.subdesc = "kernel sources"
    self.install_if = [self.parent, "ckms"]
    self.depends = [
        self.parent,
        "ckms",
        "gmake",
    ]

    return ["usr/src"]
