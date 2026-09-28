pkgname = "portsmf"
pkgver = "239"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Library for Standard MIDI Files and Allegro files"
license = "MIT"
url = "https://github.com/portsmf/portsmf"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "83a57cc75f0620110b4354f35993a23e20194d2715eb392646dd3f7f5dfbcbc0"


def post_install(self):
    self.install_license("license.txt")


@subpackage("portsmf-devel")
def _(self):
    return self.default_devel()
