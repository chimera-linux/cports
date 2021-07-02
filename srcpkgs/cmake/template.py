pkgname = "cmake"
_mver = "3.20"
version = f"{_mver}.3"
revision = 1
build_style = "configure"
configure_args = [
    "--prefix=/usr", "--mandir=/share/man", "--docdir=/share/doc/cmake",
    "--system-libarchive", "--system-zlib", "--system-bzip2",
    "--system-liblzma", "--system-zstd"
]
makedepends = ["libarchive-devel", "ncurses-devel"]
short_desc = "Cross-platform, open source build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause, ICU"
homepage = "https://cmake.org"
distfiles = [f"https://www.cmake.org/files/v{_mver}/{pkgname}-{version}.tar.gz"]
checksum = ["4d008ac3461e271fcfac26a05936f77fc7ab64402156fb371d41284851a651b8"]

from cbuild.util import make

configure_args += ["--parallel=" + str(make.jobs())]

def post_install(self):
    import shutil
    self.install_license("Copyright.txt")
    shutil.copyfile(
        self.abs_wrksrc / "Utilities/KWIML/Copyright.txt",
        self.abs_wrksrc / "KWIML-Copyright.txt"
    )
    self.install_license("KWIML-Copyright.txt")
