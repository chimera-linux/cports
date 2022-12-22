pkgname = "perl-authen-sasl"
pkgver = "2.16"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl", "perl-digest-hmac"]
depends = ["perl", "perl-digest-hmac"]
pkgdesc = "SASL authentication framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Authen-SASL"
source = f"$(CPAN_SITE)/Authen/Authen-SASL-{pkgver}.tar.gz"
sha256 = "6614fa7518f094f853741b63c73f3627168c5d3aca89b1d02b1016dc32854e09"

# FIXME visibility
hardening = ["!vis"]
