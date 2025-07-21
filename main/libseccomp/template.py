# update python-libseccomp alongside this
pkgname = "libseccomp"
pkgver = "2.6.0"
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
sha256 = "0889a8da98e37f86019c90789fd4ff7eda6e1ceb9ef07d4c51c67aeb50a77860"
# prevent a bunch of pain
exec_wrappers = [("/usr/bin/gsed", "sed")]


@subpackage("libseccomp-devel")
def _(self):
    return self.default_devel()
