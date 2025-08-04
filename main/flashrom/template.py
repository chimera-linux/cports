pkgname = "flashrom"
pkgver = "1.6.0"
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
license = "GPL-2.0-only"
url = "https://www.flashrom.org"
source = f"https://download.flashrom.org/releases/flashrom-v{pkgver}.tar.xz"
sha256 = "8b9db3987df9b5fc81e70189d017905dd5f6be1e1410347f22687ab6d4c94423"
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
