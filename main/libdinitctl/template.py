pkgname = "libdinitctl"
pkgver = "0_git20241009"
pkgrel = 1
_gitrev = "c4d85d34ecf4536c87907766928e9e2c6e642604"
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["dbus-devel", "linux-headers"]
checkdepends = ["dbus"]
pkgdesc = "Library to interact with dinit's client protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/libdinitctl"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "f56577dda8ba3668be51e6cc4d79e53dc2463b710038f2cb68da4dad9d4a1fe9"


def post_install(self):
    self.install_license("COPYING.md")
    self.install_service(self.files_path / "dbus")
    self.install_service(self.files_path / "dbus.user")
    self.install_service(self.files_path / "dinit-dbus")
    self.install_service(self.files_path / "dinit-dbus.user")


@subpackage("dinit-dbus")
def _(self):
    self.pkgdesc = "DBus interface to dinit"
    self.depends += ["dbus"]
    # provides same service files
    self.replaces = ["dbus-dinit<1.14.10-r14"]
    return [
        "cmd:dinit-dbus",
        "usr/lib/dinit.d",
        "usr/share/dbus-1",
    ]


@subpackage("libdinitctl-devel")
def _(self):
    return self.default_devel()
