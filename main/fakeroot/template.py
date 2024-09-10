pkgname = "fakeroot"
pkgver = "1.36"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_check_env = {"VERBOSE": "x"}
hostmakedepends = ["automake", "libtool"]
makedepends = ["acl-devel"]
checkdepends = ["ugetopt"]
depends = [self.with_pkgver("fakeroot-core")]
pkgdesc = "Tool for simulating superuser privileges"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://salsa.debian.org/clint/fakeroot"
source = f"{url}/-/archive/upstream/{pkgver}/fakeroot-upstream-{pkgver}.tar.gz"
sha256 = "5128dd5df59955d60453aea1817d2f31c29ffb8b8addcc5d7e200460278a6b0a"
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["libcap-devel"]
    depends += ["ugetopt"]
else:
    configure_args += ["ac_cv_func_capset=0"]


@subpackage("fakeroot-core")
def _(self):
    self.subdesc = "core"

    return ["cmd:faked", "usr/lib"]
