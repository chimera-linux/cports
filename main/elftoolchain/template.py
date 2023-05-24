pkgname = "elftoolchain"
# r3984
_commit = "f27fcce314b91b3dece6bee90949183f7a1e18b3"
pkgver = "0.7.1_svn20220506"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "WITH_ADDITIONAL_DOCUMENTATION=no",
    "WITH_TESTS=no",
    "MANTARGET=man",
]
# work around all sorts of bmake weirdness
make_install_args = make_build_args + [
    "LIBOWN=",
    "BINOWN=",
    "BINMODE=755",
    "NONBINMODE=644",
    "DIRMODE=755",
    "MANTARGET=man",
    "MANDIR=/usr/share/man",
]
make_check_target = "run-tests"
make_use_env = True
hostmakedepends = ["byacc", "flex"]
makedepends = ["libarchive-devel", "musl-bsd-headers"]
depends = [f"libelf={pkgver}-r{pkgrel}"]
pkgdesc = "BSD licensed ELF toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://sourceforge.net/projects/elftoolchain"
source = f"https://github.com/chimera-linux/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "f7017a5869c3dd7906010255ce199f3cdc0f220c10970cf23bf4c336fd724ed0"
# missing tet
options = ["bootstrap", "!check"]


def init_build(self):
    flags = self.get_cflags(shell=True) + " " + self.get_ldflags(shell=True)

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


@subpackage("elftoolchain-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libelf")
def _libelf(self):
    self.pkgdesc += " (libelf)"

    return self.default_libs()
