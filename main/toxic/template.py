pkgname = "toxic"
pkgver = "0.15.1"
pkgrel = 1
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
sha256 = "56cedc37b22a1411c68fd8b395f40f515d6a4779be02540c5cd495665caa127c"
# toxic has no tests
options = ["!check"]
