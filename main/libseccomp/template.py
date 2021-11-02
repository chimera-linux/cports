pkgname = "libseccomp"
pkgver = "2.5.2"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "bash", "gsed", "gmake", "automake", "libtool", "gperf", "pkgconf"
]
makedepends = ["linux-headers"]
pkgdesc = "High level interface to seccomp"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/seccomp/libseccomp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "95b93bff271751aae52a9802297c9d0cf57c42eabf10b70a6a5f192ee8a96ac0"
# prevent a bunch of pain
exec_wrappers = [
    ("/usr/bin/gsed", "sed")
]

def pre_configure(self):
    self.do("autoreconf", ["-if"])

@subpackage("libseccomp-devel")
def _devel(self):
    return self.default_devel(man = True)
