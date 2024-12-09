pkgname = "toxic"
pkgver = "0.16.0"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "DISABLE_GAMES=1",
    "PREFIX=/usr",
]
make_install_args = [
    "PREFIX=/usr",
]
make_use_env = True
hostmakedepends = [
    "asciidoc",
    "pkgconf",
]
makedepends = [
    "c-toxcore-devel",
    "freealut-devel",
    "libconfig-devel",
    "libcurl-devel",
    "libnotify-devel",
    "libpng-devel",
    "libx11-devel",
    "linux-headers",
    "ncurses-devel",
    "openal-soft-devel",
    "python-devel",
    "qrencode-devel",
]
pkgdesc = "Tox-based instant messaging and video chat client"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "GPL-3.0-only"
url = "https://github.com/JFreegman/toxic"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9b58f87941c5638e6169f972292351205bb6335bde8121c103d7dc6fc5174ac7"
# toxic has no tests
options = ["!check"]
