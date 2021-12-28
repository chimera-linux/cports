pkgname = "libseccomp"
pkgver = "2.5.3"
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
sha256 = "1e337ae9d8bab26641b17669a9871eaa10d4f3b474aaa4885d64b691a04614e3"
# prevent a bunch of pain
exec_wrappers = [
    ("/usr/bin/gsed", "sed")
]

def pre_configure(self):
    self.do("autoreconf", "-if")

@subpackage("libseccomp-devel")
def _devel(self):
    return self.default_devel()
