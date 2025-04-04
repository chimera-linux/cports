pkgname = "libjodycode"
pkgver = "3.1.2"
pkgrel = 0
build_style = "makefile"
make_dir = "."
make_check_target = "test"
make_use_env = True
pkgdesc = "Shared code used by several utilities written by Jody Bruchon"
license = "MIT"
url = "https://codeberg.org/jbruchon/libjodycode"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d06c63d88ffdc681132eec74095d1ed9cc0cfcc3532f59b93ceea0eecf325f35"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("libjodycode-devel")
def _(self):
    return self.default_devel()
