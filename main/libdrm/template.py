pkgname = "libdrm"
pkgver = "2.4.107"
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
sha256 = "16b23932a2b7d41d091cf95662a83f56c680a9bb3456931c0b76fde02ae2d53f"

# stuff like radeon autodetects, most arm stuff is by default false
match current.profile().arch:
    case "aarch64":
        configure_args += [
            "-Dvc4=true", "-Domap=true", "-Dfreedreno=true",
            "-Dtegra=true", "-Detnaviv=true", "-Dexynos=true"
        ]

@subpackage("libdrm-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel(man = True)
