pkgname = "deepin-icon-theme"
pkgver = "2026.02.28"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["python", "xcursorgen", "gtk+3-update-icon-cache"]
makedepends = []
# optionally falls back to papirus, but I don't think it should be a dependency…
pkgdesc = "Deepin Icons & Cursors"
license = "GPL-3.0-or-later"
url = "https://github.com/linuxdeepin/deepin-icon-theme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e4c9470d3f4f2064ff89eeafc3cc105f16ec1eddd8a97d75580639a21e115505"
broken_symlinks = [
    "usr/share/icons/vintage/apps/*/uos-activator-true.svg",
    "usr/share/icons/vintage/apps/*/uos-activator.svg",
    "usr/share/icons/bloom/apps/*/uos-activator-true.svg",
    "usr/share/icons/bloom/apps/*/uos-activator.svg",
    "usr/share/icons/bloom/actions/24/draw-triangle?.svg",  # variants 1,2,3,4
]
# no hardening needed; it's just icons
