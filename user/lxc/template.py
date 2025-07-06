pkgname = "lxc"
pkgver = "6.0.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dapparmor=false",
    # needs docbook2x
    "-Dman=false",
    "-Dinit-script=[]",
    "-Ddistrosysconfdir=default",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "libatomic-chimera-devel",
    "libatomic-chimera-devel-static",
    "libcap-devel",
    "libcap-devel-static",
    "libseccomp-devel",
    "libunwind-devel",
    "libunwind-devel-static",
    "musl-devel-static",
    "openssl3-devel",
]
depends = ["ugetopt", "xz", "wget2"]
pkgdesc = "Linux containers"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://linuxcontainers.org"
source = f"{url}/downloads/lxc/lxc-{pkgver}.tar.gz"
sha256 = "872d26ce8512b9f993d194816e336bf9f3ad8326f22dc24ef0f01f85599fa8b9"
file_modes = {"usr/libexec/lxc/lxc-user-nic": ("root", "root", 0o4755)}
# symlinks to _lxc
options = ["!lintcomp"]


def post_install(self):
    # sysvinit config
    self.uninstall("etc/default/lxc")


@subpackage("lxc-devel")
def _(self):
    return self.default_devel()
