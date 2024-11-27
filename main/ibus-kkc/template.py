pkgname = "ibus-kkc"
# this is basically abandoned and there are some fix commits since the last tag,
# easier to just use this
pkgver = "1.5.22_git20220104"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
    "ibus-devel",
    "libkkc-devel",
]
depends = ["ibus"]
pkgdesc = "Japanese KKC engine for IBus"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/ueno/ibus-kkc"
_gitrev = "b3fb76ef26a9238cc2814987d05b480ee4189ed4"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "ecbadb4e0e658da5aa32f07a3293013114789c23c4851fe0d475f3541d733899"
