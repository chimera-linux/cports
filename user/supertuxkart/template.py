pkgname = "supertuxkart"
pkgver = "1.4"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "bluez-devel",
    # "enet-devel",  # system enet does not allow for ipv6
    "freetype-devel",
    "harfbuzz-devel",
    "curl-devel",
    "libjpeg-turbo-devel",
    "libopenglrecorder-devel",
    "libpng-devel",
    "libvorbis-devel",
    "mesa-devel",
    "openal-soft-devel",
    "openssl-devel",
    "sdl-devel",
    "shaderc-devel",
    "sqlite-devel",
]
depends = [self.with_pkgver("supertuxkart-data")]
pkgdesc = "Kart racing game"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://supertuxkart.net"
source = f"https://github.com/supertuxkart/stk-code/releases/download/{pkgver}/SuperTuxKart-{pkgver}-src.tar.xz"
sha256 = "9890392419baf4715313f14d5ad60746f276eed36eb580636caf44e2532c0f03"
# breaks bullet
hardening = ["!int"]


def post_install(self):
    # leftover static libs and cmake confs and whatever
    self.uninstall("usr/lib")
    self.uninstall("usr/share/supertuxkart/data/po/*.py", glob=True)


@subpackage("supertuxkart-data")
def _(self):
    self.subdesc = "data files"
    return ["usr/share/supertuxkart"]
