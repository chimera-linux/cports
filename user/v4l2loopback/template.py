pkgname = "v4l2loopback"
pkgver = "0.15.3"
pkgrel = 0
build_style = "makefile"
make_build_target = "utils"
make_install_target = "install-extra"
hostmakedepends = ["help2man"]
makedepends = ["linux-headers"]
pkgdesc = "Kernel module to create V4L2 loopback devices"
license = "GPL-2.0-or-later"
url = "https://github.com/umlaeute/v4l2loopback"
source = f"https://github.com/umlaeute/v4l2loopback/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2758ea287da8dd34a0421c0dd50094a0342d22414e1bbccbbe92f41bbaa26b2d"
# no testsuite
options = ["!check"]


def post_install(self):
    destp = f"usr/src/{pkgname}-{pkgver}"
    self.install_file(
        self.files_path / "ckms.ini", destp, template={"VERSION": pkgver}
    )
    self.install_file("Kbuild", destp)
    self.install_file("Makefile", destp)
    self.install_file("v4l2loopback.c", destp)
    self.install_file("v4l2loopback.h", destp)
    self.install_file("v4l2loopback_formats.h", destp)


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
