pkgname = "iso-codes"
pkgver = "4.13.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["gettext-tiny", "python", "pkgconf"]
pkgdesc = "List of country, language and currency names"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://salsa.debian.org/iso-codes-team/iso-codes"
source = f"$(DEBIAN_SITE)/main/i/{pkgname}/{pkgname}_{pkgver}.orig.tar.xz"
sha256 = "2d4d0e5c02327f52cf7c029202da72f2074348472c26904b7104d2be3e0750ef"

configure_gen = []
