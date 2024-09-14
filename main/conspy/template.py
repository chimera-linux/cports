pkgname = "conspy"
pkgver = "1.16"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel", "linux-headers"]
pkgdesc = "Remote control Linux virtual consoles"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "AGPL-3.0-or-later"
url = "https://conspy.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/conspy/conspy-{pkgver}-1/conspy-{pkgver}.tar.gz"
sha256 = "ee5ef648ea08d20d9062db22e7bf62a7b7261af02053f916016d1b80a66a5609"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("agpl-3.0.txt")
