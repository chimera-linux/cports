pkgname = "lmdb"
pkgver = "0.9.29"
pkgrel = 0
build_wrksrc = "libraries/liblmdb"
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["gmake"]
pkgdesc = "Lightning Memory-Mapped Database Manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OLDAP-2.8"
url = "http://symas.com/mdb"
source = f"https://github.com/LMDB/lmdb/archive/LMDB_{pkgver}.tar.gz"
sha256 = "22054926b426c66d8f2bc22071365df6e35f3aacf19ad943bc6167d4cae3bebb"

def init_configure(self):
    eflags = [
        "CC=" + self.get_tool("CC"),
        "AR=" + self.get_tool("AR"),
        "XCFLAGS=" + self.get_cflags(shell = True),
        "LDFLAGS=" + self.get_ldflags(shell = True),
    ]
    self.make_build_args += eflags
    self.make_install_args += eflags

def post_install(self):
    self.install_license("LICENSE")
    self.install_license("COPYRIGHT")

@subpackage("lmdb-static")
def _static(self):
    return self.default_static()

@subpackage("lmdb-devel")
def _devel(self):
    return self.default_devel()
