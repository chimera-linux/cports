pkgname = "passt"
_pkgver = "2026_07_28.f8df3f1"
# yeardate only
pkgver = _pkgver.split(".")[0].replace("_", ".")
pkgrel = 0
build_style = "makefile"
make_build_args = [f"VERSION={pkgver}"]
make_install_args = ["prefix=/usr"]
make_use_env = True
makedepends = ["linux-headers"]
pkgdesc = "User-mode network translation layer between Layer 2 and 4"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "https://passt.top/passt/about"
source = f"https://passt.top/passt/snapshot/passt-{_pkgver}.tar.zst"
sha256 = "13cd432b1d15fc26d5d7e4a3642d26f1a44943aec72185882de2e9609d46bb4c"
# tries to pass no-strict-aliasing via __attribute(optimise) for some stuff but that is ignored
tool_flags = {"CFLAGS": ["-fno-strict-aliasing", "-std=c23"]}
hardening = ["vis", "cfi"]
# needs qemu and some other unpackaged tooling
options = ["!check"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")
