pkgname = "faust"
pkgver = "2.69.3"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["cmake", "gmake", "pkgconf"]
depends = ["bash"]
pkgdesc = "Functional programming language for real-time signal processing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://faust.grame.fr"
source = f"https://github.com/grame-cncm/faust/releases/download/{pkgver}/faust-{pkgver}.tar.gz"
sha256 = "169a2f1e8a95e159c78c734c1c5dd818bf5c95b3b002a7efd9f6bb8589357062"
# skip execinfo
tool_flags = {"CXXFLAGS": ["-DALPINE"]}
# no check target
options = ["!cross", "!check"]


def post_install(self):
    self.mv(self.destdir / "usr/share/faust", self.destdir / "usr/lib")
    self.install_link("../lib/faust", "usr/share/faust")
    self.rm(self.destdir / "usr/lib/libOSCFaust.a")
    self.rm(self.destdir / "usr/lib/ios-libsndfile.a")
    self.rm(self.destdir / "usr/lib/faust/max-msp/sndfile", recursive=True)
    self.rm(
        self.destdir / "usr/lib/faust/android/app/lib/libsndfile",
        recursive=True,
    )
