pkgname = "cmake"
_mver = "3.20"
version = f"{_mver}.3"
revision = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr", "--mandir=/share/man", "--docdir=/share/doc/cmake",
    "--system-libarchive", "--system-zlib", "--system-bzip2",
    "--system-liblzma", "--system-zstd",
    f"--parallel={current.conf_jobs}"
]
makedepends = ["libarchive-devel", "ncurses-devel"]
short_desc = "Cross-platform, open source build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause, ICU"
homepage = "https://cmake.org"
sources = [f"https://www.cmake.org/files/v{_mver}/{pkgname}-{version}.tar.gz"]
sha256 = ["4d008ac3461e271fcfac26a05936f77fc7ab64402156fb371d41284851a651b8"]

# prevent cmake self-bootstrap false positive nonsense
tool_flags = {
    "CXXFLAGS": ["-Wno-unused-command-line-argument"],
}

options = ["!check"]

def post_install(self):
    self.install_license("Copyright.txt")
    self.cp("Utilities/KWIML/Copyright.txt", "KWIML-Copyright.txt")
    self.install_license("KWIML-Copyright.txt")
