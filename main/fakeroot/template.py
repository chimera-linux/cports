pkgname = "fakeroot"
pkgver = "1.35"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
make_check_env = {"VERBOSE": "x"}
hostmakedepends = ["automake", "gmake", "libtool"]
makedepends = ["acl-devel"]
checkdepends = ["ugetopt"]
depends = [self.with_pkgver("fakeroot-core")]
pkgdesc = "Tool for simulating superuser privileges"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://salsa.debian.org/clint/fakeroot"
source = f"{url}/-/archive/upstream/{pkgver}/fakeroot-upstream-{pkgver}.tar.gz"
sha256 = "544c403716e56c70e7e64390b5601f241feb41f0e710401a50ca7414d20cf1f7"
# redefinition of id_t in libfakeroot
tool_flags = {"CFLAGS": ["-D_ID_T"]}
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
