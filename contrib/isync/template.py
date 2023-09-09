pkgname = "isync"
pkgver = "1.4.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "pkgconf",
]
makedepends = [
    "libsasl-devel",
    "openssl-devel",
    "zlib-devel",
]
checkdepends = ["perl"]
pkgdesc = "IMAP and MailDir mailbox synchronizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later WITH custom:LicenseRef-isync-GPL-exception"
url = "https://isync.sourceforge.io"
source = (
    f"$(SOURCEFORGE_SITE)/isync/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "7c3273894f22e98330a330051e9d942fd9ffbc02b91952c2f1896a5c37e700ff"
# FIXME: cfi
hardening = ["vis"]
# missing perl modules
options = ["!check"]


def do_check(self):
    self.do("perl", "src/run-tests.pl")


def post_install(self):
    self.install_license(self.files_path / "gpl-exception")
