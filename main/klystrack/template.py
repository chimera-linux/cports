pkgname = "klystrack"
pkgver = "1.7.8"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["sdl2-compat-devel", "sdl2_image-devel", "alsa-lib-devel"]
pkgdesc = "Chiptune tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://kometbomb.github.io/klystrack"
source = f"https://github.com/z-erica/klystrack/releases/download/{pkgver}/klystrack-{pkgver}.tar.xz"
sha256 = "136e2e0db3ed07dc14af1a75481b87645c723f9db429a6f3091c0a957ecd27c5"


def post_install(self):
    self.install_license("LICENSE")
