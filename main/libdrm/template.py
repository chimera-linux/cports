pkgname = "libdrm"
pkgver = "2.4.108"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibkms=true",
    "-Dudev=true",
    "-Dvalgrind=false"
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["eudev-devel", "libpciaccess-devel", "linux-headers"]
pkgdesc = "Userspace interface to kernel DRM services"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://dri.freedesktop.org"
source = f"https://gitlab.freedesktop.org/mesa/drm/-/archive/{pkgname}-{pkgver}/drm-{pkgname}-{pkgver}.tar.gz"
sha256 = "f70e208eb2faab96431f43e397845f8e8c5b543b714d61797d3b7e74845301d2"
options = ["lto"]

# stuff like radeon autodetects, most arm stuff is by default false
match self.profile().arch:
    case "aarch64":
        configure_args += [
            "-Dvc4=true", "-Domap=true", "-Dfreedreno=true",
            "-Dtegra=true", "-Detnaviv=true", "-Dexynos=true"
        ]

@subpackage("libdrm-static")
def _static(self):
    return self.default_static()

@subpackage("libdrm-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel(man = True)
