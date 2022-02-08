pkgname = "base-desktop"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-full",
    "gnome",
    "pipewire",
    "gst-plugins-good",
    "gst-plugins-bad",
    "gst-libav",
    "mesa-dri",
    "xdg-utils",
    "virtual:fonts-dejavu!fonts-dejavu-otf",
]
pkgdesc = "Chimera default desktop session"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
