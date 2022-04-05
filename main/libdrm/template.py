pkgname = "libdrm"
pkgver = "2.4.110"
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
sha256 = "80908d23709e0530a60de7a6efd026760e4d83c1bb334a953bd357c297be49a3"

# stuff like radeon autodetects, most arm stuff is by default false
match self.profile().arch:
    case "aarch64":
        configure_args += [
            "-Dvc4=true", "-Domap=true", "-Dfreedreno=true",
            "-Dtegra=true", "-Detnaviv=true", "-Dexynos=true"
        ]

@subpackage("libdrm-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
