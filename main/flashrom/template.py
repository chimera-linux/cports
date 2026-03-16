pkgname = "flashrom"
pkgver = "1.7.0"
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
sha256 = "4328ace9833f7efe7c334bdd73482cde8286819826cc00149e83fba96bf3ab4f"
# needs special configuration?
options = ["!check", "linkundefver"]

# cli fails to build on big endian: https://ticket.coreboot.org/issues/635
_build_cli = self.profile().endian == "little"
if not _build_cli:
    options += ["empty"]
    configure_args += ["-Dclassic_cli=disabled"]


def post_install(self):
    if _build_cli:
        # only present when cli is built
        self.rename(
            "usr/share/bash-completion/completions/flashrom.bash", "flashrom"
        )


@subpackage("flashrom-devel")
def _(self):
    return self.default_devel()


@subpackage("flashrom-libs")
def _(self):
    return self.default_libs()
