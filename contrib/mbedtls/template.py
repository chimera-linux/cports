pkgname = "mbedtls"
pkgver = "3.5.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_TESTING=ON",
    "-DUSE_SHARED_MBEDTLS_LIBRARY=ON",
    "-DUSE_STATIC_MBEDTLS_LIBRARY=ON",
]
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = ["linux-headers"]
pkgdesc = "Light-weight cryptographic and SSL/TLS library"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR GPL-2.0-or-later"
url = "https://www.trustedfirmware.org/projects/mbed-tls"
source = (
    f"https://github.com/ARMmbed/mbedtls/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "35890edf1a2c7a7e29eac3118d43302c3e1173e0df0ebaf5db56126dabe5bb05"
# vis breaks symbols
hardening = []


def pre_configure(self):
    # set defines for allowing threads for non-embedded use
    self.do("python3", "scripts/config.py", "set", "MBEDTLS_THREADING_C")
    self.do("python3", "scripts/config.py", "set", "MBEDTLS_THREADING_PTHREAD")


@subpackage("mbedtls-devel")
def _devel(self):
    return self.default_devel()


@subpackage("mbedtls-progs")
def _progs(self):
    return self.default_progs()
