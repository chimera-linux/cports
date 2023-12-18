pkgname = "libseccomp"
pkgver = "2.5.5"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "bash",
    "gsed",
    "gmake",
    "automake",
    "libtool",
    "gperf",
    "pkgconf",
]
makedepends = ["linux-headers"]
pkgdesc = "High level interface to seccomp"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/seccomp/libseccomp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7082b016d3cbda3e15c0e71ebd018023d693bb7507389b32f943db13f935e01d"
# prevent a bunch of pain
exec_wrappers = [("/usr/bin/gsed", "sed")]


@subpackage("libseccomp-devel")
def _devel(self):
    return self.default_devel()
