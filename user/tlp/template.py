pkgname = "tlp"
pkgver = "1.11.0"
pkgrel = 1
build_style = "makefile"
make_install_args = [
    "TLP_NO_INIT=1",
    "TLP_SBIN=/usr/bin",
    "TLP_WITH_ELOGIND=1",
    "TLP_WITH_SYSTEMD=0",
    "install-man",
]
makedepends = [
    "dinit-chimera",
    "dinit-dbus",
    "polkit-devel",
]
depends = ["perl", "ethtool", "hdparm"]
pkgdesc = "Battery life optimization utility"
license = "GPL-2.0-or-later"
url = "https://linrunner.de/tlp"
source = f"https://github.com/linrunner/TLP/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e014b4dcfa1e41bf912857ee9f3d5a6539231b086d4f34304719ddfe3ad402f0"
# no tests, symlinked commands
options = ["etcfiles", "!check", "!lintcomp"]


def post_install(self):
    self.install_service(self.files_path / "tlp")
    self.install_service(self.files_path / "tlp-pd")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("usr/share/dbus-1/*/*.sedbackup", glob=True)


@subpackage("tlp-rdw")
def _(self):
    self.depends = [self.parent, "networkmanager"]
    self.install_if = [self.parent, "networkmanager"]
    return ["**/*rdw*"]


@subpackage("tlp-pd")
def _(self):
    self.provides = ["power-profiles-daemon"]
    self.depends = [self.parent, "python-gobject"]
    self.install_if = [self.parent, "power-profiles-daemon-meta"]
    return ["**/*tlpctl*", "**/*tlp-pd*", "usr/share/dbus-1"]
