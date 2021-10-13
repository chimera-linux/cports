pkgname = "cmake"
_mver = "3.21"
pkgver = f"{_mver}.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr", "--mandir=/share/man", "--docdir=/share/doc/cmake",
    "--system-libarchive", "--system-zlib", "--system-bzip2",
    "--system-liblzma", "--system-zstd",
    f"--parallel={current.conf_jobs}"
]
makedepends = ["libarchive-devel", "ncurses-devel"]
pkgdesc = "Cross-platform, open source build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://cmake.org"
source = f"https://www.cmake.org/files/v{_mver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "fac3915171d4dff25913975d712f76e69aef44bf738ba7b976793a458b4cfed4"
# prevent cmake self-bootstrap false positive nonsense
tool_flags = {
    "CXXFLAGS": ["-Wno-unused-command-line-argument"],
}
# checkdepends are missing
options = ["!check"]

def post_install(self):
    self.install_license("Copyright.txt")
    self.cp("Utilities/KWIML/Copyright.txt", "KWIML-Copyright.txt")
    self.install_license("KWIML-Copyright.txt")
