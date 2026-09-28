pkgname = "pipemixer"
pkgver = "0.5.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "inih-devel",
    "ncurses-devel",
    "pipewire-devel",
]
pkgdesc = "TUI volume control for PipeWire"
license = "GPL-3.0-or-later"
url = "https://github.com/heather7283/pipemixer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e61f6c9b113e63af79e84e4f963c2aebdac383281d26b7d02e1fca06158592b1"
