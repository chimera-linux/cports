pkgname = "tlp"
pkgver = "1.9.0"
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
makedepends = ["dinit-chimera","dinit-dbus"]
depends = ["perl", "ethtool", "hdparm"]
pkgdesc = "Battery life optimization utility"
license = "GPL-2.0-or-later"
url = "https://linrunner.de/tlp"
source = f"https://github.com/linrunner/TLP/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ddb40400dcba69063d8ab1d41ee55e8dea5a42a26abe27643c13040bb8ef294b"
# no tests, symlinked commands
options = ["!check", "!lintcomp"]


def post_install(self):
    self.install_service("^/tlp")
    self.install_service("^/tlp-pd")

@subpackage("tlp-pd")
def _(self):
    self.depends = [self.parent, "python-shtab", "python-dbus", "python-gobject"]
    self.install_if = [self.parent]
    return  [
        "usr/lib/dinit.d/tlp-pd",
        "usr/bin/tlp-pd",
        "usr/bin/tlpctl",
        "usr/share/dbus-1/system-services/net.hadess.PowerProfiles.service",
        "usr/share/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service",
        "usr/share/dbus-1/system.d/net.hadess.PowerProfiles.conf",
        "usr/share/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf",
        "usr/share/polkit-1/actions/tlp-pd.policy",
        "usr/share/man/man1/tlpctl.1",
        "usr/share/man/man8/tlp-pd.8",
        "usr/share/bash-completion/completions/tlpctl",
        "usr/share/fish/vendor_completions.d/tlpctl.fish",
        "usr/share/zsh/site-functions/_tlpctl"
    ]


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
        "usr/share/fish/vendor_completions.d/tlp-rdw.fish"
    ]
