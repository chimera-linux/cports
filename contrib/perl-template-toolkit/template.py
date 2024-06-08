pkgname = "perl-template-toolkit"
pkgver = "3.101"
pkgrel = 0
build_style = "perl_module"
make_cmd = "gmake"
make_build_args = ["MAKE=gmake"]
make_install_args = list(make_build_args)
make_check_args = list(make_build_args)
hostmakedepends = [
    "gmake",
    "perl",
]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl templating module"
maintainer = "psykose <alice@ayaya.dev>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/Template"
source = f"$(CPAN_SITE)/Template/Template-Toolkit-{pkgver}.tar.gz"
sha256 = "d2a32dd6c21e4b37c6a93df8087ca9e880cfae613a3e5efaea307b0bdcaedb58"
