pkgname = "fakeroot"
pkgver = "1.36.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_check_env = {"VERBOSE": "x"}
hostmakedepends = ["automake", "slibtool"]
makedepends = ["acl-devel"]
checkdepends = ["ugetopt"]
depends = [self.with_pkgver("fakeroot-core")]
pkgdesc = "Tool for simulating superuser privileges"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://salsa.debian.org/clint/fakeroot"
source = f"{url}/-/archive/upstream/{pkgver}/fakeroot-upstream-{pkgver}.tar.gz"
sha256 = "d92fadad835bec18410f5f3ca5242ed4ff397196e16d6886d2b92cde9b6658a3"
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["libcap-devel"]
    depends += ["ugetopt"]
else:
    configure_args += ["ac_cv_func_capset=0"]


@subpackage("fakeroot-core")
def _(self):
    self.subdesc = "core"

    return ["usr/bin/faked", "usr/lib"]
