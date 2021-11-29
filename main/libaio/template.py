pkgname = "libaio"
pkgver = "0.3.112"
pkgrel = 0
_commit = "d892696468cb99d7d98b23b78bde942df0992d5a"
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "partcheck" # full check needs root, e2fsprogs, mount, etc
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Linux-native asynchronous I/O facility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://pagure.io/libaio"
source = f"https://pagure.io/{pkgname}/archive/{_commit}/{pkgname}-{_commit}.tar.gz"
sha256 = "a5181b4fb83e7885098a1f1dd20fcad21ec5e7a013f3b5c73613c14c5097b172"
hardening = ["!ssp"]

@subpackage("libaio-static")
def _static(self):
    return self.default_static()

@subpackage("libaio-devel")
def _devel(self):
    return self.default_devel(man = True)
