pkgname = "tlp"
pkgver = "1.6.1"
pkgrel = 1
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
depends = ["perl", "ethtool", "hdparm"]
pkgdesc = "Battery life optimization utility"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://linrunner.de/tlp"
source = f"https://github.com/linrunner/TLP/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f7d013691a92ffcf42ef1648565dbc24a33202046d3c8138dad1963a3169a0f5"
patch_style = "patch"
# no tests
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "tlp")


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
