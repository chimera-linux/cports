pkgname = "argon2"
pkgver = "20190702"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["OPTTARGET=none", "ARGON2_VERSION=" + pkgver]
make_install_args = ["OPTTARGET=none"]
make_check_target = "test"
make_use_env = True
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Argon2 password-hashing function"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR CC0-1.0"
url = "https://github.com/P-H-C/phc-winner-argon2"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "daf972a89577f8772602bf2eb38b6a3dd3d922bf5724d45e7f9589b5e830442c"
# otherwise generates broken static libs so we can't link cryptsetup-static
options = ["!lto"]


@subpackage("argon2-progs")
def _lib(self):
    return self.default_progs()


@subpackage("argon2-devel")
def _devel(self):
    return self.default_devel()
