pkgname = "gnome-remote-desktop"
pkgver = "46.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
    "-Drdp=true",
    "-Dvnc=false",
    "-Dtests=false",
    "-Dsystemd_sysusers_dir=/usr/lib/sysusers.d",
    "-Dsystemd_tmpfiles_dir=/usr/lib/tmpfiles.d",
]
hostmakedepends = ["meson", "pkgconf", "gettext", "asciidoc"]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "fdk-aac-devel",
    "ffnvcodec-headers",
    "freerdp3-devel",
    "fuse-devel",
    "glib-devel",
    "libdrm-devel",
    "libei-devel",
    "libepoxy-devel",
    "libnotify-devel",
    "libsecret-devel",
    "libxkbcommon-devel",
    "opus-devel",
    "pipewire-devel",
    "polkit-devel",
    "tpm2-tss-devel",
]
checkdepends = [
    "dbus",
    "libgbm-devel",
    "libgudev-devel",
    "mutter",
    "openssl",
    "pipewire",
    "wireplumber",
]
pkgdesc = "GNOME remote desktop"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0"
url = "https://gitlab.gnome.org/GNOME/gnome-remote-desktop"
source = f"$(GNOME_SITE)/gnome-remote-desktop/{pkgver.split('.')[0]}/gnome-remote-desktop-{pkgver}.tar.xz"
sha256 = "08c6656f11d4639eb4972a8929e8f502427dc1e2ea033e02c992bb1a4c77d794"
# TODO
options = ["!check"]
