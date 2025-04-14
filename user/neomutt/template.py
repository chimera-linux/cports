pkgname = "neomutt"
pkgver = "2025.04.04"
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
sha256 = "732d4fd006856030971c99ef0e569846d0358feababea115a353f90ab02d3142"
env = {"autosetup_tclsh": "tclsh"}
# no tests defined
options = ["!check"]
