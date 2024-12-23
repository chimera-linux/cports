pkgname = "neomutt"
pkgver = "2025.01.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--gpgme",
    "--notmuch",
    "--pcre2",
    "--ssl",
    "--zlib",
]
configure_gen = []
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext-devel",
    "libxml2-progs",
    "libxslt-progs",
    "perl",
    "pkgconf",
    "tcl",
]
makedepends = [
    "gpgme-devel",
    "libidn2-devel",
    "ncurses-devel",
    "notmuch-devel",
    "openssl3-devel",
    "pcre2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Mail reader"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://neomutt.org"
source = f"https://github.com/neomutt/neomutt/archive/refs/tags/{pkgver.replace('.', '')}.tar.gz"
sha256 = "cc7835e80fd72af104a8e146e009e93e687cefbc6c11725ee2ed11d7377486ff"
env = {"autosetup_tclsh": "tclsh"}
# no tests defined
options = ["!check"]
