pkgname = "dmraid"
pkgver = "1.0.0_rc16"
_rver = "1.0.0.rc16-3"
pkgrel = 0
build_wrksrc = f"{_rver}/dmraid" # :(
build_style = "gnu_configure"
configure_args = [
    "--enable-led", "--enable-intel_led", "--enable-shared_lib"
]
make_cmd = "gmake"
make_dir = "." # :(
hostmakedepends = ["gmake", "gsed"]
makedepends = ["device-mapper-devel", "linux-headers"]
pkgdesc = "Device mapper RAID interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://people.redhat.com/~heinzm/sw/dmraid"
source = f"{url}/src/{pkgname}-{_rver}.tar.bz2"
sha256 = "93421bd169d71ff5e7d2db95b62b030bfa205a12010b6468dcdef80337d6fbd8"
# no test suite
options = ["!parallel", "!check"]
# :(
exec_wrappers = [
    ("/usr/bin/gsed", "sed")
]

def pre_configure(self):
    (self.cwd / "autoconf/install-sh").chmod(0o755) # :(

@subpackage("libdmraid")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs(extra = ["usr/lib/device-mapper"])

@subpackage("dmraid-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
