pkgname = "ndctl"
pkgver = "81"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
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
license = "GPL-2.0-only AND LGPL-2.1-only AND MIT AND CC0-1.0"
url = "https://github.com/pmem/ndctl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e40784687ac2d0c176748c9ffb8bde541a12301b6fedb607a9a70c8fd1f94929"
hardening = ["vis", "cfi"]
# the MIT licence used doesn't have a copyright line in it
options = ["!distlicense"]


@subpackage("ndctl-devel")
def _(self):
    return self.default_devel()


@subpackage("ndctl-libs")
def _(self):
    return self.default_libs()
