pkgname = "openjpeg"
pkgver = "2.5.2"
_test_commit = "1f4c3cfb0f0266f9731db8a168186a9462358f28"
pkgrel = 0
build_style = "cmake"
# we skip static libs or they get referenced in cmake devel files
configure_args = ["-DBUILD_TESTING=ON", "-DBUILD_STATIC_LIBS=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libpng-devel", "libtiff-devel", "lcms2-devel"]
pkgdesc = "Open-source JPEG 2000 codec written in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.openjpeg.org"
source = [
    f"https://github.com/uclouvain/openjpeg/archive/v{pkgver}.tar.gz",
    f"https://github.com/uclouvain/openjpeg-data/archive/{_test_commit}.tar.gz",
]
source_paths = [".", "data"]
sha256 = [
    "90e3896fed910c376aaf79cdd98bdfdaf98c6472efd8e1debf0a854938cbda6a",
    "502631509e911eec543c7b300bf699020bfd88f118275a4a225326266385f469",
]
hardening = ["!vis", "!cfi"]


def init_configure(self):
    self.configure_args += [f"-DOPJ_DATA_ROOT:PATH={self.chroot_cwd}/data"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openjpeg-devel")
def _devel(self):
    # because cmake is dumb and references binaries in the find file
    self.depends += [self.with_pkgver("openjpeg-progs")]

    return self.default_devel()


@subpackage("openjpeg-progs")
def _progs(self):
    return self.default_progs()
