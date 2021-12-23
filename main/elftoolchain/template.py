pkgname = "elftoolchain"
_commit = "f7e9afc6f9ad0d84ea73b4659c5d6d13275d2306"
pkgver = "0.7.1_svn20210623"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "WITH_ADDITIONAL_DOCUMENTATION=no", "WITH_TESTS=no", "MANTARGET=man"
]
# work around all sorts of bmake weirdness
make_install_args = make_build_args + [
    "LIBOWN=", "BINOWN=", "BINMODE=755", "NONBINMODE=644", "DIRMODE=755",
    "MANTARGET=man", "MANDIR=/usr/share/man"
]
make_check_target = "run-tests"
make_use_env = True
hostmakedepends = ["bsdm4", "byacc", "flex"]
makedepends = ["libarchive-devel", "musl-bsd-headers"]
depends = [f"libelf={pkgver}-r{pkgrel}"]
pkgdesc = "BSD licensed ELF toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://sourceforge.net/projects/elftoolchain"
source = f"https://github.com/{pkgname}/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "3d9e0513af4b7cb8ac7944d98057b8d61fcc4ff326b030a7b06006c0abb7922c"
# missing tet
options = ["bootstrap", "!check"]

def init_build(self):
    flags = self.get_cflags(shell = True) + " " + \
            self.get_ldflags(shell = True)

    self.env["SHLIB_LDADD"] = flags
    # abuse this to work around elftoolchain's fucky build system
    self.env["LDSTATIC"] = flags

def post_install(self):
    self.install_license("LICENSE")
    # fix some permissions
    for f in (self.destdir / "usr/lib").glob("*.so.*"):
        f.chmod(0o755)
    # install a musl-compatible elfdefinitions.h
    self.install_file(self.files_path / "elfdefinitions.h", "usr/include/sys")

@subpackage("elftoolchain-static")
def _static(self):
    return self.default_static()

@subpackage("elftoolchain-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libelf")
def _libelf(self):
    self.pkgdesc += " (libelf)"

    return self.default_libs()
