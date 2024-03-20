pkgname = "passt"
_pkgver = "2024_03_20.71dd405"
# yeardate only
pkgver = _pkgver.split(".")[0].replace("_", ".")
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [f"VERSION={pkgver}"]
make_install_args = ["prefix=/usr"]
make_use_env = True
hostmakedepends = ["gmake", "gsed"]
makedepends = ["linux-headers"]
pkgdesc = "User-mode network translation layer between Layer 2 and 4"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "https://passt.top/passt/about"
source = f"https://passt.top/passt/snapshot/passt-{_pkgver}.tar.zst"
sha256 = "4e0ebf888205613470ba98a6e3e1835fcee3af50accd79cfa7374061579b9c4c"
# tries to pass this via __attribute(optimise) for some stuff but that is ignored
tool_flags = {"CFLAGS": ["-fno-strict-aliasing"]}
hardening = ["vis", "cfi"]
# needs qemu and some other unpackaged tooling
options = ["!check"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")
