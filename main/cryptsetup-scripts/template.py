pkgname = "cryptsetup-scripts"
pkgver = "2.7.5.2"
_debver = "-".join(pkgver.rsplit(".", 1))
pkgrel = 1
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
sha256 = "a576f09d17cd33e473d461a6d805b46690c49253f2862e3de79912aee1749db3"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "dinit-cryptdisks", "usr/lib", mode=0o755
    )
