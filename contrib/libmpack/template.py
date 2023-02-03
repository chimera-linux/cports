pkgname = "libmpack"
pkgver = "1.0.5"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = ["gmake", "libtool", "pkgconf"]
pkgdesc = "Simple implementation of msgpack in C"
license = "MIT"
url = "https://github.com/libmpack/libmpack"
source= f"https://github.com/libmpack/libmpack/archive/{pkgver}.tar.gz"
sha256 = "4ce91395d81ccea97d3ad4cb962f8540d166e59d3e2ddce8a22979b49f108956"
# crossbuild fails because of libtool
options = ["!cross"]

def post_install(self):
    self.install_license("LICENSE-MIT")

@subpackage("libmpack-devel")
def _devel(self):
    return self.default_devel()
