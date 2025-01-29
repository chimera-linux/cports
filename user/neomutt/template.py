pkgname = "neomutt"
pkgver = "2024.12.12"
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
    "perl",
    "pkgconf",
    "tcl",
    "xsltproc",
]
makedepends = [
    "gpgme-devel",
    "libidn2-devel",
    "ncurses-devel",
    "notmuch-devel",
    "openssl-devel",
    "pcre2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Mail reader"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://neomutt.org"
source = f"https://github.com/neomutt/neomutt/archive/refs/tags/{pkgver.replace('.', '')}.tar.gz"
sha256 = "6fbdbfd7f4d028276f7f0b1d9fe2bb5ee67161857111824cf392ca1ff27089c8"
env = {"autosetup_tclsh": "tclsh"}
# TODO: patch cleanup logic
hardening = ["vis", "cfi", "!cfi-icall"]
# no tests defined
options = ["!check"]
