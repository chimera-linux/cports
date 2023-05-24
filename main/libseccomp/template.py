pkgname = "libseccomp"
pkgver = "2.5.4"
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
sha256 = "96bbadb4384716272a6d2be82801dc564f7aab345febfe9b698b70fc606e3f75"
# prevent a bunch of pain
exec_wrappers = [("/usr/bin/gsed", "sed")]


@subpackage("libseccomp-devel")
def _devel(self):
    return self.default_devel()
