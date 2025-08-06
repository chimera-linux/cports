pkgname = "cryptsetup-scripts"
pkgver = "2.8.6.2"
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
sha256 = "f5cabd772d3ebef995eb6d36777b4222045a6344907892742f6bcdac9670545d"
# no test suite
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_file(
        self.files_path / "dinit-cryptdisks", "usr/lib", mode=0o755
    )
