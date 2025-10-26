pkgname = "supertuxkart"
pkgver = "1.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "bluez-devel",
    "curl-devel",
    # "enet-devel",  # system enet does not allow for ipv6
    "freetype-devel",
    "harfbuzz-devel",
    "libjpeg-turbo-devel",
    "libopenglrecorder-devel",
    "libpng-devel",
    "libvorbis-devel",
    "mesa-devel",
    "openal-soft-devel",
    "openssl3-devel",
    "sdl2-compat-devel",
    "shaderc-devel",
    "sqlite-devel",
]
depends = [self.with_pkgver("supertuxkart-data")]
pkgdesc = "Kart racing game"
license = "GPL-3.0-or-later"
url = "https://supertuxkart.net"
source = f"https://github.com/supertuxkart/stk-code/releases/download/{pkgver}/SuperTuxKart-{pkgver}-src.tar.gz"
sha256 = "33cf8841e4ff4082d80b9248014295bbbea61d14683e86dff100e3ab8f7b27cb"
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
