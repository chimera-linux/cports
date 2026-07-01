pkgname = "tlp"
pkgver = "1.10.1"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    "-j1",
    "TLP_SBIN=/usr/bin",
    "TLP_ULIB=/usr/lib/udev",
    "TLP_ELOD=/usr/lib/elogind/system-sleep",
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
sha256 = "c3f1f4b72a603a134e24b21364669a828180a3de5cbe62917ba88f0c53ca6397"
# no tests, symlinked commands
options = ["!check", "!lintcomp"]


def post_install(self):
    self.make.install(["install-man"])
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
        "usr/share/fish/vendor_completions.d/tlp-rdw.fish",
    ]
