pkgname = "conspy"
pkgver = "1.17"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel", "linux-headers"]
pkgdesc = "Remote control Linux virtual consoles"
license = "AGPL-3.0-or-later"
url = "https://conspy.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/conspy/conspy-{pkgver}-1/conspy-{pkgver}.tar.gz"
sha256 = "61230ef6c5898dcfb3a8cb60d218c8458588d97367a90d9538b66f1d94990b64"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("agpl-3.0.txt")
