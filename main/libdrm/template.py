pkgname = "libdrm"
pkgver = "2.4.125"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dudev=true", "-Dvalgrind=disabled"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["udev-devel", "libpciaccess-devel", "linux-headers"]
pkgdesc = "Userspace interface to kernel DRM services"
license = "MIT"
url = "https://dri.freedesktop.org"
source = f"https://gitlab.freedesktop.org/mesa/drm/-/archive/libdrm-{pkgver}/drm-libdrm-{pkgver}.tar.gz"
sha256 = "dd3e86a9fae99322d6430b28397f8e03ac4fb8deeed9a6e214bd5ced86db68c6"
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
