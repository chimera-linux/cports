pkgname = "libdrm"
pkgver = "2.4.117"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dudev=true", "-Dvalgrind=disabled"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["udev-devel", "libpciaccess-devel", "linux-headers"]
pkgdesc = "Userspace interface to kernel DRM services"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://dri.freedesktop.org"
source = f"https://gitlab.freedesktop.org/mesa/drm/-/archive/{pkgname}-{pkgver}/drm-{pkgname}-{pkgver}.tar.gz"
sha256 = "69e0e763bea9069c32cac466264f7ff4d559058fcfe38536816a44a955df3cdc"
# FIXME cfi int
hardening = ["vis", "!cfi", "!int"]
options = ["!distlicense"]

# stuff like radeon autodetects, most arm stuff is by default false
match self.profile().arch:
    case "aarch64":
        configure_args += [
            "-Dvc4=enabled",
            "-Domap=enabled",
            "-Dfreedreno=enabled",
            "-Dtegra=enabled",
            "-Detnaviv=enabled",
            "-Dexynos=enabled",
        ]


@subpackage("libdrm-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
