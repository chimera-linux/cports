pkgname = "flatpak"
pkgver = "1.18.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddconf=enabled",
    "-Ddbus_config_dir=/usr/share/dbus-1/system.d",
    "-Dgdm_env_file=true",
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
    "bison",
    "bubblewrap",
    "docbook-xml",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libxml2-progs",
    "meson",
    "pkgconf",
    "python-pyparsing",
    "xdg-dbus-proxy",
    "xmlto",
]
makedepends = [
    "appstream-devel",
    "appstream-glib-devel",
    "curl-devel",
    "dconf-devel",
    "fuse-devel",
    "gcab-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gpgme-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libcap-devel",
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
license = "LGPL-2.1-or-later"
url = "https://flatpak.org"
source = f"https://github.com/flatpak/flatpak/releases/download/{pkgver}/flatpak-{pkgver}.tar.xz"
sha256 = "bc683fc916ed21c0524bb064f358c2ac18586b8ec88c76f2f7f289877521631c"
# test runner expects a different env (possible FIXME?)
options = ["etcfiles", "!check", "!cross"]


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
