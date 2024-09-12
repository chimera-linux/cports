pkgname = "lxde"
pkgver = "0.5.5"
pkgrel = 0
build_style = "meta"
depends = [
    "gpicview",
    "lxappearance",
    "lxappearance-obconf",
    "lxde-common",
    "lxinput",
    "lxlauncher",
    "lxpanel",
    "lxrandr",
    "lxsession",
    "lxtask",
    "lxterminal",
    "openbox",
    "pcmanfm",
    "xserver-xorg-minimal",
]
pkgdesc = "LXDE desktop environment"
subdesc = "session"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "custom:meta"
url = "https://www.lxde.org"


@subpackage("lxde-default-themes")
def _(self):
    self.subdesc = "default themes"
    self.install_if = [self.parent]
    self.depends = ["lxde-icon-theme"]
    return []
