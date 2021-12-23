pkgname = "duktape"
pkgver = "2.6.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["-f", "Makefile.sharedlibrary"]
make_install_args = ["-f", "Makefile.sharedlibrary"]
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Embeddeable JavaScript engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://duktape.org"
source = f"https://github.com/svaarala/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "96f4a05a6c84590e53b18c59bb776aaba80a205afbbd92b82be609ba7fe75fa7"
# no check target
options = ["!check"]

def init_configure(self):
    self.make_install_args += [
        f"INSTALL_PREFIX={self.chroot_destdir / 'usr'}"
    ]

def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_file(self.files_path / "duktape.pc", "usr/lib/pkgconfig")

@subpackage("duktape-devel")
def _devel(self):
    return self.default_devel()
