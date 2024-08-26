pkgname = "nvidia-settings"
pkgver = "560.35.03"
pkgrel = 0
archs = ["x86_64"]
build_style = "makefile"
make_build_args = [
    "GTK2_AVAILABLE=0",
    "GTK3_AVAILABLE=1",
    "JANSSON_CFLAGS=",
    "MANPAGE_GZIP=0",
    "NV_USE_BUNDLED_LIBJANSSON=0",
    "STRIP_CMD=true",
    "WAYLAND_AVAILABLE=1",
]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = [
    "dbus-devel",
    "gtk+3-devel",
    "jansson-devel",
    "libvdpau-devel",
    "libxv-devel",
    "linux-headers",
    "vulkan-headers",
]
pkgdesc = "NVIDIA driver control panel"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "GPL-2.0-only"
url = f"https://github.com/NVIDIA/{pkgname}"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e0e85a58423c30bcc2f95b7c28c674593a95e862f9c8c5c7b82e19cd3ce18fe5"
# no tests
options = ["!check"]
