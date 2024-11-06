pkgname = "cryptsetup-scripts"
pkgver = "2.7.4.1"
_debver = "-".join(pkgver.rsplit(".", 1))
pkgrel = 1
build_style = "makefile"
make_build_args = [
    "DOCBOOK_XSL=/usr/share/xsl-nons/docbook/manpages/docbook.xsl",
    f"VERSION={pkgver}",
]
hostmakedepends = ["perl", "docbook-xsl-nons", "xsltproc"]
depends = ["cryptsetup", "device-mapper", "mount", "mkfs"]
pkgdesc = "Supporting infrastructure for cryptsetup from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/cryptsetup-team/cryptsetup"
source = f"{url}/-/archive/debian/2%25{_debver}/cryptsetup-debian-2%25{_debver}.tar.gz"
sha256 = "d907277761bcb0f04d073ea8349461ede5ae783fa6d37e433653c56ed1dfde31"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "dinit-cryptdisks", "usr/lib", mode=0o755
    )
