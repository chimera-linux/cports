pkgname = "toxic"
pkgver = "0.16.3"
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
    "curl-devel",
    "freealut-devel",
    "libconfig-devel",
    "libnotify-devel",
    "libpng-devel",
    "libx11-devel",
    "linux-headers",
    "ncurses-devel",
    "openal-soft-devel",
    "qrencode-devel",
]
pkgdesc = "Tox-based instant messaging and video chat client"
license = "GPL-3.0-only"
url = "https://github.com/JFreegman/toxic"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a6bc6c9ec614b0658963da71debc3d4a1b31cc59158f25a9275dc93076ee3448"
# toxic has no tests
options = ["!check"]
