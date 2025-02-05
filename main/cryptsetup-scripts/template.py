pkgname = "cryptsetup-scripts"
pkgver = "2.7.5.1"
_debver = "-".join(pkgver.rsplit(".", 1))
pkgrel = 2
build_style = "makefile"
make_build_args = [
    "DOCBOOK_XSL=/usr/share/xsl-nons/docbook/manpages/docbook.xsl",
    f"VERSION={pkgver}",
]
hostmakedepends = ["perl", "docbook-xsl-nons", "libxslt-progs"]
depends = ["cryptsetup", "lvm2-dm", "util-linux-mount", "util-linux-mkfs"]
pkgdesc = "Supporting infrastructure for cryptsetup from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/cryptsetup-team/cryptsetup"
source = f"{url}/-/archive/debian/2%25{_debver}/cryptsetup-debian-2%25{_debver}.tar.gz"
sha256 = "287eb3d3f9fea6ad2c1b64339a75e312fa8182c9a57ee6039edb0e7908fd25a5"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "dinit-cryptdisks", "usr/lib", mode=0o755
    )
