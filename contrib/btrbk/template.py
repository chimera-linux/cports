pkgname = "btrbk"
pkgver = "0.32.6"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "asciidoctor"]
depends = ["perl", "btrfs-progs", "openssh", "mbuffer"]
pkgdesc = "Backup tool for btrfs subvolumes"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://digint.ch/btrbk"
source = (
    f"https://digint.ch/download/{pkgname}/releases/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "02e2ac647c918463202cbe607bb95557a4f7fd237069124333c54da5b2bbb76b"
# no tests
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
