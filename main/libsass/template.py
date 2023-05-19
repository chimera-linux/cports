pkgname = "libsass"
pkgver = "3.6.5"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
pkgdesc = "C implementation of the Sass CSS preprocessor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.sass-lang.com/libsass"
source = f"https://github.com/sass/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "89d8f2c46ae2b1b826b58ce7dde966a176bac41975b82e84ad46b01a55080582"

def pre_configure(self):
    # otherwise the .pc file will have 'na' version
    with open(self.cwd / "VERSION", "w") as vf:
        vf.write(pkgver)

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libsass-devel")
def _devel(self):
    return self.default_devel()
