pkgname = "toxic"
pkgver = "0.16.1"
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
    "curl-devel",
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
sha256 = "4969f0a72e40e0ed296cfff5a5bcd58b999ace52759327c29f23866c96d64f00"
# toxic has no tests
options = ["!check"]
