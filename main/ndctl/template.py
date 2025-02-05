pkgname = "ndctl"
pkgver = "80"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dmodprobedatadir=/usr/lib/modprobe.d",
    "-Dsystemd=disabled",
    f"-Dversion-tag={pkgver}",
]
hostmakedepends = [
    "asciidoctor",
    "bash-completion",
    "meson",
    "pkgconf",
]
makedepends = [
    "iniparser-devel",
    "json-c-devel",
    "keyutils-devel",
    "kmod-devel",
    "libtraceevent-devel",
    "libtracefs-devel",
    "linux-headers",
    "udev-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "Tools and libraries for NVDIMMs and other platform memory"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-only AND MIT AND CC0-1.0"
url = "https://github.com/pmem/ndctl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4bb7565feea486997a0f62b1878aeb6d4db9af128e0fa459359b3c02644325c5"
hardening = ["vis", "cfi"]
# the MIT licence used doesn't have a copyright line in it
options = ["!distlicense"]


@subpackage("ndctl-devel")
def _(self):
    return self.default_devel()


@subpackage("ndctl-libs")
def _(self):
    return self.default_libs()
