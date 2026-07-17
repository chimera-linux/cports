pkgname = "perl-authen-sasl"
pkgver = "2.1900"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl", "perl-crypt-urandom", "perl-digest-hmac"]
depends = ["perl", "perl-crypt-urandom", "perl-digest-hmac"]
pkgdesc = "SASL authentication framework"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Authen-SASL"
# $(CPAN_SITE) (www.cpan.org/modules/by-module) only mirrors the latest
# release per module and 403s on older pinned versions once superseded
# upstream (this one has since moved on to 2.2000); the permanent
# author-keyed path never gets pruned.
source = f"https://cpan.metacpan.org/authors/id/E/EH/EHUELS/Authen-SASL-{pkgver}.tar.gz"
sha256 = "be3533a6891b2e677150b479c1a0d4bf11c8bbeebed3e7b8eba34053e93923b0"
