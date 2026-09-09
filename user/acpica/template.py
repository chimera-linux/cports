pkgname = "acpica"
pkgver = "20260930"
pkgrel = 0
build_style = "makefile"
# avoid `_FORTIFY_SOURCE` macro redefined
make_build_args = ["NOFORTIFY=TRUE"]
make_use_env = True
hostmakedepends = ["bison", "flex"]
pkgdesc = "Intel ACPI Component Architecture utilities"
license = "BSD-3-Clause OR GPL-2.0-only"
url = "https://www.acpica.org"
source = f"https://github.com/open-acpica/acpica/releases/download/{pkgver}/acpica-unix-{pkgver}.tar.gz"
sha256 = "aa18901b92e30749be0edc3081c8d550c61fce4fa37546fc6a65d367a4ae71a5"
tool_flags = {"CFLAGS": ["-Wno-unknown-warning-option"]}
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.BSD-3-Clause")
