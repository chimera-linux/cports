pkgname = "libdrm"
pkgver = "2.4.114"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dudev=true",
    "-Dvalgrind=disabled"
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["eudev-devel", "libpciaccess-devel", "linux-headers"]
pkgdesc = "Userspace interface to kernel DRM services"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://dri.freedesktop.org"
source = f"https://gitlab.freedesktop.org/mesa/drm/-/archive/{pkgname}-{pkgver}/drm-{pkgname}-{pkgver}.tar.gz"
sha256 = "919ccacc5d9211840b9433d16ee825b1bc7108e7d63e05557969a17c3532d764"
# FIXME cfi int
hardening = ["vis", "!cfi", "!int"]

# stuff like radeon autodetects, most arm stuff is by default false
match self.profile().arch:
    case "aarch64":
        configure_args += [
            "-Dvc4=enabled", "-Domap=enabled", "-Dfreedreno=enabled",
            "-Dtegra=enabled", "-Detnaviv=enabled", "-Dexynos=enabled"
        ]

@subpackage("libdrm-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
