pkgname = "isync"
pkgver = "1.5.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "libsasl-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["perl"]
pkgdesc = "IMAP and MailDir mailbox synchronizer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later WITH custom:LicenseRef-isync-GPL-exception"
url = "https://isync.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/isync/isync/{pkgver}/isync-{pkgver}.tar.gz"
sha256 = "a0c81e109387bf279da161453103399e77946afecf5c51f9413c5e773557f78d"
hardening = ["vis", "!cfi"]
# missing perl modules
options = ["!check"]


def check(self):
    self.do("perl", "src/run-tests.pl")


def post_install(self):
    self.install_license(self.files_path / "gpl-exception")
