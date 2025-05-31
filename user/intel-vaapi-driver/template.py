pkgname = "intel-vaapi-driver"
pkgver = "2.4.4"
pkgrel = 0
# only usable here
archs = ["x86_64"]
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libdrm-devel", "libva-devel", "libx11-devel"]
pkgdesc = "VA-API driver for Haswell and older Intel GPUs"
license = "MIT"
url = "https://github.com/irql-notlessorequal/intel-vaapi-driver"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ddb13866c399622d95fa2d8b372f8f8d7dc738432cc20dff52a74159fac12b9c"


def post_install(self):
    self.install_license("LICENSE")
