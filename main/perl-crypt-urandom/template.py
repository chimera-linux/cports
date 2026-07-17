pkgname = "perl-crypt-urandom"
pkgver = "0.54"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for non-blocking randomness"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/dist/Crypt-URandom"
# $(CPAN_SITE) (www.cpan.org/modules/by-module) only mirrors the latest
# release per module and 403s on older pinned versions once superseded
# upstream (this one has since moved on to 0.55); the permanent
# author-keyed path never gets pruned.
source = f"https://cpan.metacpan.org/authors/id/D/DD/DDICK/Crypt-URandom-{pkgver}.tar.gz"
sha256 = "4a73cd394933328da484aaeb8645d735b35465df60109e559e0a28b066053a57"
