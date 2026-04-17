pkgname = "tlp"
pkgver = "1.9.1"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    "-j1",
    "TLP_SBIN=/usr/bin",
    "TLP_ULIB=/usr/lib/udev",
    "TLP_ELOD=/usr/libexec/elogind/system-sleep",
    "TLP_NO_INIT=1",
    "TLP_WITH_ELOGIND=1",
    "TLP_WITH_SYSTEMD=0",
]
makedepends = ["dinit-chimera"]
depends = ["perl", "ethtool", "hdparm"]
pkgdesc = "Battery life optimization utility"
license = "GPL-2.0-or-later"
url = "https://linrunner.de/tlp"
source = f"https://github.com/linrunner/TLP/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6f7c69a8c56706f83bc3566377caf846c2ccbd8f2621fe8e56c6d1e684d15156"
# no tests, symlinked commands
options = ["!check", "!lintcomp"]


def post_install(self):
    self.install_service("^/tlp")


@subpackage("tlp-rdw")
def _(self):
    self.depends = [self.parent, "networkmanager"]
    self.install_if = [self.parent, "networkmanager"]
    return [
        "usr/bin/tlp-rdw",
        "usr/lib/NetworkManager",
        "usr/lib/udev/tlp-rdw-udev",
        "usr/lib/udev/rules.d/85-tlp-rdw.rules",
        "usr/share/man/man8/tlp-rdw.8",
        "usr/share/zsh/site-functions/_tlp-rdw",
        "usr/share/bash-completion/completions/tlp-rdw",
    ]


@subpackage("tlp-pd")
def _(self):
    self.depends = [self.parent, "!power-profiles-daemon"]
    self.install_if = [self.parent, "!power-profiles-daemon"]
    return [
        "usr/bin/tlp-pd",
        "usr/bin/tlpctl",
        "usr/share/polkit-1/actions",
        "usr/share/dbus-1/system.d",
        "usr/share/dbus-1/system-services",
        "usr/share/man/man8/tlp-pd.8",
        "usr/share/zsh/site-functions/_tlpctl",
        "usr/share/bash-completion/completions/tlpctl",
    ]
