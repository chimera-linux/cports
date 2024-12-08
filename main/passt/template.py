pkgname = "passt"
_pkgver = "2024_11_27.c0fbc7e"
# yeardate only
pkgver = _pkgver.split(".")[0].replace("_", ".")
pkgrel = 0
build_style = "makefile"
make_build_args = [f"VERSION={pkgver}"]
make_install_args = ["prefix=/usr"]
make_use_env = True
makedepends = ["linux-headers"]
pkgdesc = "User-mode network translation layer between Layer 2 and 4"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "https://passt.top/passt/about"
source = f"https://passt.top/passt/snapshot/passt-{_pkgver}.tar.zst"
sha256 = "5ae0044c0b134b7cae6d084c352e0e003431ea5a12cf4b54b2d47044c0ae2b08"
# tries to pass this via __attribute(optimise) for some stuff but that is ignored
tool_flags = {"CFLAGS": ["-fno-strict-aliasing"]}
hardening = ["vis", "cfi"]
# needs qemu and some other unpackaged tooling
options = ["!check"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")
