pkgname = "rnnoise"
pkgver = "0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Neural network based noise reduction library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://jmvalin.ca/demo/rnnoise"
source = f"https://github.com/xiph/rnnoise/releases/download/v{pkgver}/rnnoise-{pkgver}.tar.gz"
sha256 = "90fce4b00b9ff24c08dbfe31b82ffd43bae383d85c5535676d28b0a2b11c0d37"
hardening = ["vis", "cfi"]

if self.profile().arch == "x86_64":
    configure_args = ["--enable-x86-rtcd"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("rnnoise-devel")
def _(self):
    return self.default_devel()
