pkgname = "libdrm"
pkgver = "2.4.118"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dudev=true", "-Dvalgrind=disabled"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["udev-devel", "libpciaccess-devel", "linux-headers"]
pkgdesc = "Userspace interface to kernel DRM services"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://dri.freedesktop.org"
source = f"https://gitlab.freedesktop.org/mesa/drm/-/archive/{pkgname}-{pkgver}/drm-{pkgname}-{pkgver}.tar.gz"
sha256 = "56d65ef7576023238c8638204b29174b8a4d690d6b25f84ac9624c0b4ad796b8"
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
