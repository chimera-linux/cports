pkgname = "unifdef"
pkgver = "2.12"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
make_check_target = "test"
make_check_args = ["-j1"]
pkgdesc = "Selectively remove C preprocessor conditionals"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND BSD-3-Clause"
url = "https://github.com/fanf2/unifdef"
source = f"https://dotat.at/prog/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "43ce0f02ecdcdc723b2475575563ddb192e988c886d368260bc0a63aee3ac400"

def post_install(self):
    self.install_license("COPYING")
