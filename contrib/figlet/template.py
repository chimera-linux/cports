pkgname = "figlet"
pkgver = "2.2.5"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Program for making large letters out of ordinary text"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "http://www.figlet.org"
source = (
    f"https://github.com/cmatsuoka/figlet/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "4d366c4a618ecdd6fdb81cde90edc54dbff9764efb635b3be47a929473f13930"
tool_flags = {"CFLAGS": ["-Wno-deprecated-non-prototype"]}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
