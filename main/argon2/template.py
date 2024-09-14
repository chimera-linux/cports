pkgname = "argon2"
pkgver = "20190702"
pkgrel = 1
build_style = "makefile"
make_build_args = ["OPTTARGET=none", "ARGON2_VERSION=" + pkgver]
make_install_args = ["OPTTARGET=none"]
make_check_target = "test"
make_use_env = True
hostmakedepends = ["pkgconf"]
pkgdesc = "Argon2 password-hashing function"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR CC0-1.0"
url = "https://github.com/P-H-C/phc-winner-argon2"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "daf972a89577f8772602bf2eb38b6a3dd3d922bf5724d45e7f9589b5e830442c"


@subpackage("argon2-progs")
def _(self):
    return self.default_progs()


@subpackage("argon2-devel")
def _(self):
    return self.default_devel()
