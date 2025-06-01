pkgname = "cadical"
pkgver = "2.1.3"
pkgrel = 0
build_style = "configure"
make_check_target = "test"
pkgdesc = "SAT solver"
license = "MIT"
url = "https://fmv.jku.at/cadical"
source = f"https://github.com/arminbiere/cadical/archive/refs/tags/rel-{pkgver}.tar.gz"
sha256 = "abfe890aa4ccda7b8449c7ad41acb113cfb8e7e8fbf5e49369075f9b00d70465"
# cross: tries to run compiled executable
options = ["!cross"]


def install(self):
    self.install_bin("build/cadical")
    self.install_bin("build/mobical")
    self.install_lib("build/libcadical.a")
    self.install_file("src/cadical.hpp", "usr/include")
    self.install_license("LICENSE")


@subpackage("cadical-devel")
def _(self):
    return self.default_devel()
