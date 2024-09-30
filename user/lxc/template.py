pkgname = "lxc"
pkgver = "6.0.2"
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
sha256 = "1930aa10d892db8531d1353d15f7ebf5913e74a19e134423e4d074c07f2d6e8b"
patch_style = "patch"
file_modes = {"usr/libexec/lxc/lxc-user-nic": ("root", "root", 0o4755)}
# symlinks to _lxc
options = ["!lintcomp"]


def post_install(self):
    # sysvinit config
    self.uninstall("etc/default/lxc")


@subpackage("lxc-devel")
def _(self):
    return self.default_devel()
