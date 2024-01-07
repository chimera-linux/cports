pkgname = "http-parser"
pkgver = "2.9.4"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "library"
make_check_target = "test"
hostmakedepends = ["gmake"]
pkgdesc = "HTTP parser written in C"
maintainer = "aurelia <git@elia.garden>"
license = "MIT"
url = "https://github.com/nodejs/http-parser"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "467b9e30fd0979ee301065e70f637d525c28193449e1b13fbcb1b1fab3ad224f"


def post_install(self):
    self.install_license("LICENSE-MIT")


@subpackage("http-parser-devel")
def _devel(self):
    return self.default_devel()
