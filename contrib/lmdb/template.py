pkgname = "lmdb"
pkgver = "0.9.33"
pkgrel = 0
build_wrksrc = "libraries/liblmdb"
build_style = "makefile"
make_install_args = ["prefix=/usr"]
make_check_target = "test"
make_check_env = {"LD_LIBRARY_PATH": "."}
make_use_env = True
hostmakedepends = [
    "pkgconf",
]
pkgdesc = "Lightning Memory-Mapped Database Manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OLDAP-2.8"
url = "http://www.lmdb.tech/doc"
source = f"https://git.openldap.org/openldap/openldap/-/archive/LMDB_{pkgver}/openldap-LMDB_{pkgver}.tar.gz"
sha256 = "476801f5239c88c7de61c3390502a5d13965ecedef80105b5fb0fcb8373d1e53"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("COPYRIGHT")
    self.install_file(self.files_path / "lmdb.pc", "usr/lib/pkgconfig")


@subpackage("lmdb-devel")
def _(self):
    return self.default_devel()
