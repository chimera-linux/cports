pkgname = "supertuxkart"
pkgver = "1.4"
pkgrel = 4
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
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
