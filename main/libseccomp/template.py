# update python-libseccomp alongside this
pkgname = "libseccomp"
pkgver = "2.6.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "bash",
    "gperf",
    "gsed",
    "pkgconf",
    "slibtool",
]
makedepends = ["linux-headers"]
pkgdesc = "High level interface to seccomp"
license = "LGPL-2.1-or-later"
url = "https://github.com/seccomp/libseccomp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f9a13e4c633d319a9240189760ca348caa0837c0ebe2a09b17061da8ceaf60f0"
# prevent a bunch of pain
exec_wrappers = [("/usr/bin/gsed", "sed")]


@subpackage("libseccomp-devel")
def _(self):
    return self.default_devel()
