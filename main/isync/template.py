pkgname = "isync"
pkgver = "1.5.1"
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
license = "GPL-2.0-or-later WITH custom:LicenseRef-isync-GPL-exception"
url = "https://isync.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/isync/isync/{pkgver}/isync-{pkgver}.tar.gz"
sha256 = "28cc90288036aa5b6f5307bfc7178a397799003b96f7fd6e4bd2478265bb22fa"
hardening = ["vis", "!cfi"]
# missing perl modules
options = ["!check"]


def check(self):
    self.do("perl", "src/run-tests.pl")


def post_install(self):
    self.install_license(self.files_path / "gpl-exception")
