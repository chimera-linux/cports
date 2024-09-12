pkgname = "obconf"
pkgver = "2.0.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libsm-devel",
    "openbox-devel",
    "gtk+3-devel",
    "imlib2-devel",
    "startup-notification-devel",
]
depends = ["desktop-file-utils", "shared-mime-info"]
pkgdesc = "GTK-based configuration tool for Openbox window manager"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/danakj/obconf"
source = f"{url}/archive/refs/heads/master.zip"
sha256 = "debfc518883d77a650357386a0ad76ebf239a8d6b8a7ef84f4c2131d3892194d"
