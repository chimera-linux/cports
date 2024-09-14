pkgname = "pam-krb5"
pkgver = "4.11"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
makedepends = ["heimdal-devel", "linux-pam-devel"]
pkgdesc = "PAM module for Kerberos authentication"
maintainer = "yanchan09 <yan@omg.lol>"
license = "BSD-3-Clause OR GPL-1.0-or-later"
url = "https://www.eyrie.org/~eagle/software/pam-krb5"
source = (
    f"https://archives.eyrie.org/software/kerberos/pam-krb5-{pkgver}.tar.gz"
)
sha256 = "503cbe2cb1aff4bdfda3bcf7f93f94fb6ba52c26d708934e7039b2182fe10b20"
# Running tests requires non-trivial setup
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
