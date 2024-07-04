pkgname = "libsasl"
pkgver = "2.1.28"
pkgrel = 1
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
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool"]
pkgdesc = "Cyrus SASL (runtime library)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause-Attribution"
url = "https://www.cyrusimap.org/sasl"
source = f"https://github.com/cyrusimap/cyrus-sasl/releases/download/cyrus-sasl-{pkgver}/cyrus-sasl-{pkgver}.tar.gz"
sha256 = "7ccfc6abd01ed67c1a0924b353e526f1b766b21f42d4562ee635a8ebfc5bb38c"
options = ["!cross"]


def post_install(self):
    # we only want libsasl
    self.uninstall("usr/bin")
    self.uninstall("usr/share")
    self.uninstall("usr/lib/sasl2")
    self.install_license("COPYING")


@subpackage("libsasl-devel")
def _devel(self):
    return self.default_devel()
