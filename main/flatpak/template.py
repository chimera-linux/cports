pkgname = "flatpak"
pkgver = "1.16.1"
pkgrel = 0
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
sha256 = "2b47e8f2d90d35d29339ed78e1a6eabb36eefa9cfa5a5ca3b0d1f27502c43675"
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
