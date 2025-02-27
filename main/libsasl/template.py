pkgname = "libsasl"
pkgver = "2.1.28"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--enable-cram",
    "--enable-digest",
    "--enable-auth-sasldb",
    "--enable-plain",
    "--enable-anon",
    "--enable-login",
    "--enable-gssapi",
    "--enable-ntlm",
    "--with-configdir=/etc/sasl2:/etc/sasl:/usr/lib/sasl2",
    "--disable-otp",
    "--disable-srp",
    "--disable-srp-setpass",
    "--disable-krb4",
    "--with-devrandom=/dev/random",
    "--with-dblib=none",
]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Cyrus SASL"
subdesc = "runtime library"
license = "BSD-3-Clause-Attribution"
url = "https://www.cyrusimap.org/sasl"
source = f"https://github.com/cyrusimap/cyrus-sasl/releases/download/cyrus-sasl-{pkgver}/cyrus-sasl-{pkgver}.tar.gz"
sha256 = "7ccfc6abd01ed67c1a0924b353e526f1b766b21f42d4562ee635a8ebfc5bb38c"
options = ["!cross"]


def post_install(self):
    # we only want libsasl and plugins
    self.uninstall("usr/bin")
    self.uninstall("usr/share")
    self.install_license("COPYING")


@subpackage("libsasl-devel")
def _(self):
    return self.default_devel()
