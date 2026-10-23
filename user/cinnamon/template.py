pkgname = "cinnamon"
pkgver = "6.6.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared", "-Ddocs=false"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "perl",
    "pkgconf",
    "python",
    "sassc",
]
makedepends = [
    "at-spi2-core-devel",
    "cinnamon-menus-devel",
    "cjs-devel",
    "dbus-devel",
    "gcr3-devel",
    "glib-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libsecret-devel",
    "libx11-devel",
    "libxml2-devel",
    "mesa-devel",
    "muffin-devel",
    "networkmanager-devel",
    "polkit-devel",
    "xapp-devel",
]
depends = [
    "accountsservice",
    "bash",
    "cinnamon-control-center",
    "cinnamon-desktop",
    "cinnamon-menus",
    "cinnamon-screensaver",
    "cinnamon-session",
    "cinnamon-settings-daemon",
    "cjs",
    "evolution-data-server",
    "gcr3",
    "gsound",
    "gtk+3",
    "ibus",
    "inxi",
    "libgnomekbd",
    "libical",
    "libkeybinder3",
    "libnma",
    "libnotify",
    "libtimezonemap",
    "libxmlb",
    "muffin",
    "nemo",
    "openrc-settingsd",
    "procps",
    "python-babel",
    "python-cairo",
    "python-dbus",
    "python-distro",
    "python-gobject",
    "python-pam",
    "python-pexpect",
    "python-pillow",
    "python-psutil",
    "python-pytz",
    "python-requests",
    "python-setproctitle",
    "python-tinycss2",
    "python-xapp",
    "upower-libs",
    "xapp",
    "xapp-symbolic-icons",
    "xdg-desktop-portal-gtk",
    "xdg-desktop-portal-xapp",
    "xdg-utils",
]
pkgdesc = "Desktop environment providing a traditional user experience"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = (
    f"https://github.com/linuxmint/cinnamon/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "62fe4a47f727fda66b4f38a83d21b23a7ccb9f2af169a5f8e7c0b4258131d6bf"
# merged menu directory is created by the user
broken_symlinks = ["etc/xdg/menus/cinnamon-applications-merged"]
# tests are not functional
options = ["etcfiles", "!check", "!cross"]


@subpackage("cinnamon-meta")
def _(self):
    self.subdesc = "recommends package"
    self.install_if = [self.parent]
    self.depends = [
        "blueman",
        "desktop-file-utils",
        "gnome-keyring",
        "gvfs",
        "mint-cursor-themes",
        "mint-themes",
        "mint-x-icons",
        "mint-y-icons",
        "network-manager-applet",
        "power-profiles-daemon-meta",
        "system-config-printer",
        "touchegg",
        "udisks",
        "xdg-user-dirs-gtk",
        "xserver-xorg",
    ]
    self.options = ["empty"]

    return []


@subpackage("cinnamon-apps-meta")
def _(self):
    self.subdesc = "apps recommends package"
    self.install_if = [self.with_pkgver("cinnamon-meta")]
    self.depends = [
        "baobab",
        "file-roller",
        "gnome-calculator",
        "gnome-disk-utility",
        "gnome-screenshot",
        "gnome-system-monitor",
        "gnome-terminal",
        "gnome-text-editor",
        "loupe",
        "papers",
    ]
    self.options = ["empty"]

    return []


@subpackage("cinnamon-lightdm-meta")
def _(self):
    self.subdesc = "LightDM recommends package"
    self.install_if = [self.parent]
    self.depends = ["lightdm", "slick-greeter"]
    self.options = ["empty"]

    return []
