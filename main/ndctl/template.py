pkgname = "ndctl"
pkgver = "79"
pkgrel = 0
build_style = "meson"
configure_args = [
    # use this instead of asciidoc+xmlto when added
    "-Dasciidoctor=disabled",
    "-Dmodprobedatadir=/usr/lib/modprobe.d",
    "-Dsystemd=disabled",
    f"-Dversion-tag={pkgver}",
]
hostmakedepends = [
    "asciidoc",
    "bash-completion",
    "meson",
    "pkgconf",
    "xmlto",
]
makedepends = [
    "iniparser-devel",
    "json-c-devel",
    "keyutils-devel",
    "libkmod-devel",
    "libtraceevent-devel",
    "libtracefs-devel",
    "libuuid-devel",
    "linux-headers",
    "udev-devel",
]
pkgdesc = "Tools and libraries for NVDIMMs and other platform memory"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only AND LGPL-2.1-only AND MIT AND CC0-1.0"
url = "https://github.com/pmem/ndctl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c4c4e698c38ba8be4c08f3a9554cca3db8e71db1ace13906e3f8490db13418f0"
hardening = ["vis", "cfi"]
# the MIT licence used doesn't have a copyright line in it
options = ["!distlicense"]


@subpackage("ndctl-devel")
def _devel(self):
    return self.default_devel()


@subpackage("ndctl-libs")
def _libs(self):
    return self.default_libs()
