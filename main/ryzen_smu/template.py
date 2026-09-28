pkgname = "ryzen_smu"
pkgver = "0.1.5"
pkgrel = 3
# only for ryzen cpus
archs = ["x86_64"]
build_style = "makefile"
make_build_args = ["-C", "userspace"]
pkgdesc = "Kernel module for access to AMD Ryzen System Management Units"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/leogx9r/ryzen_smu"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "ede71cb23343d193bfda44ff277c8c1109fb6e30508dcc2c0fb4a6f596ce37d4"
# no tests
options = ["!check"]


def install(self):
    self.install_bin("userspace/monitor_cpu")
    destp = f"usr/src/{pkgname}-{pkgver}"
    self.install_file(
        self.files_path / "ckms.ini", destp, template={"VERSION": pkgver}
    )
    self.install_file("Makefile", destp)
    self.install_file("drv.c", destp)
    self.install_file("smu.c", destp)
    self.install_file("smu.h", destp)


@subpackage("ryzen_smu-ckms")
def _(self):
    self.subdesc = "kernel sources"
    self.install_if = [self.parent, "ckms"]
    self.depends = [
        self.parent,
        "ckms",
        "gmake",
    ]

    return ["usr/src"]
