pkgname = "cryptsetup-scripts"
pkgver = "2.8.0.1"
_debver = "-".join(pkgver.rsplit(".", 1))
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "DOCBOOK_XSL=/usr/share/xsl-nons/docbook/manpages/docbook.xsl",
    f"VERSION={pkgver}",
]
hostmakedepends = ["perl", "docbook-xsl-nons", "libxslt-progs"]
depends = ["cryptsetup", "lvm2-dm", "util-linux-mount", "util-linux-mkfs"]
pkgdesc = "Supporting infrastructure for cryptsetup from Debian"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/cryptsetup-team/cryptsetup"
source = f"{url}/-/archive/debian/2%25{_debver}/cryptsetup-debian-2%25{_debver}.tar.gz"
sha256 = "2cc5d6240e190007546a05d58d8a3e37275bb937f116e2d5e2d3abaed9b65b5c"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "dinit-cryptdisks", "usr/lib", mode=0o755
    )
