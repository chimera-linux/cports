pkgname = "neomutt"
pkgver = "2026.01.05"
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
license = "GPL-2.0-or-later"
url = "https://neomutt.org"
source = f"https://github.com/neomutt/neomutt/archive/refs/tags/{pkgver.replace('.', '')}.tar.gz"
sha256 = "a78e55a0df62b7f98566676d0ab9041aad89b2384bb5c6f3a96302a5cf49968d"
env = {"autosetup_tclsh": "tclsh"}
# no tests defined
options = ["!check"]
