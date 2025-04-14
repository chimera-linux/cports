pkgname = "capstone"
pkgver = "5.0.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "bash",
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Ultimate Disassembler"
license = "BSD-3-Clause-Clear"
url = "https://www.capstone-engine.org"
source = f"https://github.com/capstone-engine/capstone/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "240ebc834c51aae41ca9215d3190cc372fd132b9c5c8aa2d5f19ca0c325e28f9"
hardening = ["vis", "!cfi"]

if self.profile().arch == "armv7":
    # capstone_test_mos65xx segfaults
    # https://github.com/capstone-engine/capstone/issues/2676
    make_check_args = ["-E", "capstone_test_mos65xx"]


def post_install(self):
    self.install_license("LICENSE.TXT")


@subpackage("capstone-devel")
def _(self):
    return self.default_devel()


@subpackage("capstone-progs")
def _(self):
    return self.default_progs()
