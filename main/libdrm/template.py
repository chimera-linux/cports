pkgname = "libdrm"
pkgver = "2.4.134"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dudev=true", "-Dvalgrind=disabled"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["udev-devel", "libpciaccess-devel", "linux-headers"]
pkgdesc = "Userspace interface to kernel DRM services"
license = "MIT"
url = "https://dri.freedesktop.org"
source = f"https://gitlab.freedesktop.org/mesa/drm/-/archive/libdrm-{pkgver}/drm-libdrm-{pkgver}.tar.gz"
sha256 = "6b18e4834b0c061232cb5c11e98a6ecdc72ebc6bc282d124406b7a9d4e089ce2"
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
def _(self):
    self.depends += makedepends
    return self.default_devel()
