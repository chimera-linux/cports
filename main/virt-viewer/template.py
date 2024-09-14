pkgname = "virt-viewer"
pkgver = "11.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbash_completion=enabled",
    "-Dspice=enabled",
    "-Dvnc=enabled",
    "-Dvte=enabled",
    "-Dovirt=disabled",
    "-Dlibvirt=disabled",
]
hostmakedepends = [
    "bash-completion",
    "gettext",
    "gobject-introspection",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = [
    "gtk-vnc-devel",
    "spice-gtk-devel",
    "vte-gtk3-devel",
]
pkgdesc = "Graphical display viewer for VNC and SPICE protocols"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/virt-viewer/virt-viewer"
source = f"{url}/-/archive/v{pkgver}/virt-viewer-v{pkgver}.tar.bz2"
sha256 = "9928f91c55029aaba270c0d29d31936d873e0e5b8fd073716d58401120d99e23"
