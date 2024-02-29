pkgname = "sd-tools"
pkgver = "0.99.0"
pkgrel = 2
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "acl-devel",
    "libcap-devel",
    "linux-headers",
]
depends = ["base-files"]
# replace the other package
provides = ["systemd-utils=255-r0"]
# very old but might as well ensure old systems upgrade nicely
replaces = ["systemd-tmpfiles<255"]
triggers = ["/usr/lib/sysusers.d", "/usr/lib/tmpfiles.d"]
pkgdesc = "Small set of tools forked from systemd"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/chimera-linux/sd-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "09ffbc8bfe1f660d4918fd50dff51db1686ac9b3bd45c7ddcbf27b0470394da3"
# FIXME: hashmap needs a rewrite to be non-UB
hardening = ["vis", "!cfi"]


def post_install(self):
    # deprecated names, to be phased out
    self.install_link("sd-tmpfiles", "usr/bin/systemd-tmpfiles")
    self.install_link("sd-sysusers", "usr/bin/systemd-sysusers")
