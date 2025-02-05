pkgname = "lxc"
pkgver = "6.0.3"
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
maintainer = "tj <tjheeta@gmail.com>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://linuxcontainers.org"
source = f"{url}/downloads/lxc/lxc-{pkgver}.tar.gz"
sha256 = "adac0837d2abfd2903916eaf56f60756f131327311f4f25ad917f6a71f73f98c"
file_modes = {"usr/libexec/lxc/lxc-user-nic": ("root", "root", 0o4755)}
# symlinks to _lxc
options = ["!lintcomp"]


def post_install(self):
    # sysvinit config
    self.uninstall("etc/default/lxc")


@subpackage("lxc-devel")
def _(self):
    return self.default_devel()
