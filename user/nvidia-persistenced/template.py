pkgname = "nvidia-persistenced"
pkgver = "560.35.03"
pkgrel = 0
archs = ["x86_64"]
build_style = "makefile"
make_build_args = ["MANPAGE_GZIP=0", "STRIP_CMD=true"]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = [
    # "dbus-devel",
    # "gtk+3-devel",
    # "jansson-devel",
    # "libvdpau-devel",
    # "libxv-devel",
    # "linux-headers",
    # "vulkan-headers"
    "libtirpc-devel",
]
pkgdesc = "NVIDIA driver persistence daemon"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "MIT"
url = f"https://github.com/NVIDIA/{pkgname}"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e4b85c7ada85010212c45b84582f0af4aaed795335dcc7c0ceea9f274a8b7eb0"
# no tests
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")
