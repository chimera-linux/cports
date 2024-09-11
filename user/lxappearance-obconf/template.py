pkgname = "lxappearance-obconf"
pkgver = "0.2.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-gtk3", "--disable-static"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "lxappearance",
    "openbox-devel",
    "pkgconf",
]
makedepends = ["gtk+3-devel", "libx11-devel"]
pkgdesc = "LXAppearance plugin for configuring OpenBox"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-only"
url = "https://github.com/lxde/lxappearance"
source = f"https://downloads.sourceforge.net/lxde/lxappearance-obconf-{pkgver}.tar.xz"
sha256 = "3150b33b4b7beb71c1803aee2be21c94767d73b70dfc8d2bcaafe2650ea83149"
