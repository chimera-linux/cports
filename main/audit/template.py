pkgname = "audit"
pkgver = "4.0.2"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-zos-remote",
    "--with-aarch64",
]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "libcap-ng-devel",
    "linux-headers",
]
pkgdesc = "User space tools for kernel auditing"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://people.redhat.com/sgrubb/audit"
source = f"{url}/audit-{pkgver}.tar.gz"
sha256 = "d5d1b5d50ee4a2d0d17875bc6ae6bd6a7d5b34d9557ea847a39faec531faaa0a"


@subpackage("audit-libs")
def _(self):
    return self.default_libs()


@subpackage("audit-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
