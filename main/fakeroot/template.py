pkgname = "fakeroot"
pkgver = "1.25.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
configure_gen = []
make_cmd = "gmake"
make_check_env = {"VERBOSE": "x"}
hostmakedepends = ["gmake"]
makedepends = ["acl-devel"]
checkdepends = ["ugetopt"]
depends = [f"fakeroot-core={pkgver}-r{pkgrel}"]
pkgdesc = "Tool for simulating superuser privileges"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://salsa.debian.org/clint/fakeroot"
source = f"https://repo.chimera-linux.org/distfiles/{pkgname}-{pkgver}.tar.gz"
sha256 = "2c8a1443d77009b07f3b9ef3797036fb7d77b16fb648692ae39e8c480fd0e0e9"
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["libcap-devel"]
    depends += ["ugetopt"]
else:
    configure_args += ["ac_cv_func_capset=0"]


@subpackage("fakeroot-core")
def _core(self):
    self.pkgdesc = f"{pkgdesc} (core)"

    return ["usr/bin/faked", "usr/lib"]
