pkgname = "lxc"
pkgver = "6.0.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dapparmor=false",
    # needs docbook2x
    "-Dman=false",
    "-Dinit-script=sysvinit",
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
    "openssl-devel",
]
depends = [
    "xz",
    "wget2",
]
pkgdesc = "Linux containers"
maintainer = "tj <tjheeta@gmail.com>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://linuxcontainers.org"
source = f"{url}/downloads/lxc/lxc-{pkgver}.tar.gz"
sha256 = "ccb38fbcdb86a82ee8192ccc85bba47edaf824439e9a7f12ab178d51ff1f77e0"
file_modes = {"usr/libexec/lxc/lxc-user-nic": ("root", "root", 0o4755)}
# symlinks to _lxc
options = ["!lintcomp"]


def post_install(self):
    # openrc scripts
    self.uninstall("etc/default/lxc")
    self.uninstall("etc/init.d")


@subpackage("lxc-devel")
def _(self):
    return self.default_devel()
