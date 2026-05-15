pkgname = "gamemode"
pkgver = "1.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dwith-examples=false",
    "-Dwith-sd-bus-provider=tangle",
    "-Dwith-privileged-group=_gamemode",
]
hostmakedepends = [
    "cmake",
    "git",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "inih-devel",
    "linux-headers",
    "tangle-devel",
]
pkgdesc = "Optimise Linux system performance on demand"
license = "BSD-3-Clause"
url = "https://github.com/FeralInteractive/gamemode"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2b4a20894822caf04767af6a1601130d6b718fc30b8a77895607341b1674740f"


def post_install(self):
    self.install_service(self.files_path / "gamemoded.user")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_license("LICENSE.txt")


@subpackage("gamemode-devel")
def _(self):
    return self.default_devel()
