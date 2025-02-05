pkgname = "flatpak"
pkgver = "1.16.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Ddconf=enabled",
    "-Ddbus_config_dir=/usr/share/dbus-1/system.d",
    "-Dgdm_env_file=true",
    "-Dhttp_backend=curl",
    "-Dlibzstd=enabled",
    "-Dselinux_module=disabled",
    "-Dsystem_bubblewrap=/usr/bin/bwrap",
    "-Dsystem_dbus_proxy=/usr/bin/xdg-dbus-proxy",
    "-Dsystem_fusermount=/usr/bin/fusermount3",
    "-Dsystem_helper_user=_flatpak",
    "-Dsystemd=disabled",
    "-Dtests=false",
    "-Dwayland_security_context=enabled",
]
hostmakedepends = [
    "meson",
    "bison",
    "bubblewrap",
    "docbook-xml",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libxml2-progs",
    "pkgconf",
    "python-pyparsing",
    "xdg-dbus-proxy",
    "xmlto",
]
makedepends = [
    "appstream-devel",
    "appstream-glib-devel",
    "dconf-devel",
    "fuse-devel",
    "gcab-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gpgme-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libcap-devel",
    "curl-devel",
    "libseccomp-devel",
    "libxau-devel",
    "libxml2-devel",
    "ostree-devel",
    "polkit-devel",
    "wayland-devel",
    "wayland-protocols",
    "zstd-devel",
]
checkdepends = ["bash", "dbus", "socat"]
depends = [
    "bubblewrap",
    "desktop-file-utils",
    "gtk+3-update-icon-cache",
    "shared-mime-info",
    "xdg-dbus-proxy",
]
# invoke the trigger on self
triggers = ["/usr/share/flatpak"]
pkgdesc = "Linux application sandboxing and distribution framework"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://flatpak.org"
source = f"https://github.com/flatpak/flatpak/releases/download/{pkgver}/flatpak-{pkgver}.tar.xz"
sha256 = "cb0ac565adcb62127c6d11ed50ee7044d6a836fa69c354b2f4b640a22bfa4b2a"
# test runner expects a different env (possible FIXME?)
options = ["!check", "!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.uninstall("usr/lib/tmpfiles.d/flatpak.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="flatpak.conf",
    )


@subpackage("flatpak-devel")
def _(self):
    return self.default_devel()
