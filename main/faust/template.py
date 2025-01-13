pkgname = "faust"
pkgver = "2.77.3"
pkgrel = 0
archs = ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
build_style = "makefile"
make_build_args = ["GENERATOR=Ninja"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
depends = ["bash"]
pkgdesc = "Functional programming language for real-time signal processing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://faust.grame.fr"
source = f"https://github.com/grame-cncm/faust/releases/download/{pkgver}/faust-{pkgver}.tar.gz"
sha256 = "3685348ba2482547fc7675b345caea490ff380814c5dcabc8a5f772682617c0e"
# skip execinfo
tool_flags = {"CXXFLAGS": ["-DALPINE"]}
# no check target
options = ["!cross", "!check"]


def post_install(self):
    self.rename("usr/share/faust", "usr/lib/faust", relative=False)
    self.install_link("usr/share/faust", "../lib/faust")
    self.uninstall("usr/lib/libOSCFaust.a")
    self.uninstall("usr/lib/ios-libsndfile.a")
    self.uninstall("usr/lib/faust/max-msp/sndfile")
    self.uninstall("usr/lib/faust/android/app/lib/libsndfile")
