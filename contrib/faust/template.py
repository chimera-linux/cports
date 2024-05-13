pkgname = "faust"
pkgver = "2.72.14"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["GENERATOR=Ninja"]
hostmakedepends = ["cmake", "gmake", "ninja", "pkgconf"]
depends = ["bash"]
pkgdesc = "Functional programming language for real-time signal processing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://faust.grame.fr"
source = f"https://github.com/grame-cncm/faust/releases/download/{pkgver}/faust-{pkgver}.tar.gz"
sha256 = "dcd5aaf263c59d34c385e65c4f4c5b85b0e9435e57cbfd79bb67a01e5780acf0"
# skip execinfo
tool_flags = {"CXXFLAGS": ["-DALPINE"]}
# no check target
options = ["!cross", "!check"]


def post_install(self):
    self.mv(self.destdir / "usr/share/faust", self.destdir / "usr/lib")
    self.install_link("usr/share/faust", "../lib/faust")
    self.rm(self.destdir / "usr/lib/libOSCFaust.a")
    self.rm(self.destdir / "usr/lib/ios-libsndfile.a")
    self.rm(self.destdir / "usr/lib/faust/max-msp/sndfile", recursive=True)
    self.rm(
        self.destdir / "usr/lib/faust/android/app/lib/libsndfile",
        recursive=True,
    )
