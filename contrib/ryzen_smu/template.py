# remember to update files/ckms.ini
pkgname = "ryzen_smu"
pkgver = "0.1.5"
pkgrel = 2
# only for ryzen cpus
archs = ["x86_64"]
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["-C", "userspace"]
hostmakedepends = ["gmake"]
pkgdesc = "Kernel module for access to AMD Ryzen System Management Units"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/leogx9r/ryzen_smu"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "ede71cb23343d193bfda44ff277c8c1109fb6e30508dcc2c0fb4a6f596ce37d4"
# no tests
options = ["!check"]


def do_install(self):
    self.install_bin("userspace/monitor_cpu")
    self.install_dir(f"usr/src/{pkgname}-{pkgver}")
    for file in [
        "Makefile",
        "drv.c",
        "smu.c",
        "smu.h",
        self.files_path / "ckms.ini",
    ]:
        self.install_file(file, f"usr/src/{pkgname}-{pkgver}")


@subpackage("ryzen_smu-ckms")
def _ckms(self):
    self.pkgdesc = f"{pkgdesc} (kernel sources)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "ckms"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "ckms",
        "gmake",
    ]

    return ["usr/src"]
