pkgname = "lmdb"
pkgver = "0.9.36"
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
license = "OLDAP-2.8"
url = "http://www.lmdb.tech/doc"
source = f"https://git.openldap.org/openldap/openldap/-/archive/LMDB_{pkgver}/openldap-LMDB_{pkgver}.tar.gz"
sha256 = "90a595ea500074af61b213464452d8d212405261094667a686357467ae7b57b9"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("COPYRIGHT")
    self.install_file(self.files_path / "lmdb.pc", "usr/lib/pkgconfig")


@subpackage("lmdb-devel")
def _(self):
    return self.default_devel()
