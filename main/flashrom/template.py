pkgname = "flashrom"
pkgver = "1.5.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Duse_internal_dmi=false"]
hostmakedepends = ["meson", "pkgconf", "python-sphinx"]
makedepends = [
    "libftdi1-devel",
    "libusb-devel",
    "linux-headers",
    "pciutils-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["cmocka-devel"]
pkgdesc = "Utility for flashing ROM chips"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.flashrom.org"
source = f"https://download.flashrom.org/releases/flashrom-v{pkgver}.tar.xz"
sha256 = "1f934b076ed49eace203655ec249fc7861a6b8e87fe4aef732e47b6e485b6293"
# needs special configuration?
options = ["!check", "linkundefver"]


def post_install(self):
    self.rename(
        "usr/share/bash-completion/completions/flashrom.bash", "flashrom"
    )


@subpackage("flashrom-devel")
def _(self):
    return self.default_devel()


@subpackage("flashrom-libs")
def _(self):
    return self.default_libs()
