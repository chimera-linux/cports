pkgname = "sddm"
pkgver = "0.21.0"
pkgrel = 8
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DBUILD_MAN_PAGES=ON",
    "-DBUILD_WITH_QT6=ON",
    # they dropped these upstream anyway, just write our own
    "-DINSTALL_PAM_CONFIGURATION=OFF",
    "-DNO_SYSTEMD=ON",
    "-DUID_MAX=60513",
    "-DRUNTIME_DIR=/run/sddm",
    "-DUSE_ELOGIND=ON",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
    "python-docutils",
]
makedepends = [
    "dinit-chimera",
    "dinit-dbus",
    "elogind",
    "elogind-devel",
    "linux-pam-devel",
    "openrc-settingsd",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
depends = [
    "dinit-dbus",
    "elogind",
    "openrc-settingsd",
    "turnstile",
    "virtual:sddm-compositor-default!sddm-default-none",
    "virtual:sddm-theme-default!sddm-theme-none",
    "xrdb",
]
pkgdesc = "QML based display manager"
license = "GPL-2.0-or-later AND CC-BY-3.0"
url = "https://github.com/sddm/sddm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f895de2683627e969e4849dbfbbb2b500787481ca5ba0de6d6dfdae5f1549abf"

# TODO:
# - any tweaks to /usr/share/sddm/scripts/Xsession required like on gnome?


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "sddm")
    for f in ["default", "wayland-cage", "wayland-kwin", "wayland-weston"]:
        self.install_file(
            self.files_path / f"00-{f}.conf",
            "usr/lib/sddm/sddm.conf.d",
        )
    # all unusable
    self.uninstall("usr/share/sddm/themes")
    for pam in ["sddm", "sddm-autologin", "sddm-greeter"]:
        self.install_file(
            self.files_path / f"{pam}.pam", "usr/lib/pam.d", name=pam
        )


@subpackage("sddm-default-cage")
def _(self):
    self.subdesc = "use cage"
    self.install_if = [self.parent, "!plasma-desktop"]
    self.provides = [self.with_pkgver("sddm-compositor-default")]
    self.provider_priority = 10
    self.depends += [self.parent, "cage"]

    return ["usr/lib/sddm/sddm.conf.d/00-wayland-cage.conf"]


@subpackage("sddm-default-kwin")
def _(self):
    self.subdesc = "use kwin"
    self.install_if = [self.parent, "plasma-desktop"]
    self.provides = [self.with_pkgver("sddm-compositor-default")]
    self.provider_priority = 10
    self.depends += [
        self.parent,
        "kwin",
        # input method
        "plasma-keyboard",
    ]

    return ["usr/lib/sddm/sddm.conf.d/00-wayland-kwin.conf"]


@subpackage("sddm-default-weston")
def _(self):
    self.subdesc = "use weston"
    self.provides = [self.with_pkgver("sddm-compositor-default")]
    self.provider_priority = 0
    self.depends += [self.parent, "weston"]

    return ["usr/lib/sddm/sddm.conf.d/00-wayland-weston.conf"]


@subpackage("sddm-default-none")
def _(self):
    self.subdesc = "custom compositor"
    self.provides = [self.with_pkgver("sddm-compositor-default")]
    self.provider_priority = 0
    self.options = ["empty"]

    return []


@subpackage("sddm-theme-none")
def _(self):
    self.subdesc = "no theme"
    self.provides = ["sddm-theme-default=0"]
    self.options = ["empty"]

    return []
