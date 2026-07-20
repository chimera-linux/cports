pkgname = "sddm"
pkgver = "0.21.0"
pkgrel = 6
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
    self.install_file(
        self.files_path / "00-default.conf",
        "usr/lib/sddm/sddm.conf.d",
    )
    # install default breeze theme selection, which gets picked along with
    # kwin for compositor etc. to get proper wayland, else it faills back
    # to sddm builtin stuff and looks awful
    self.install_file(
        self.files_path / "10-breeze-theme.conf",
        "usr/lib/sddm/sddm.conf.d",
    )
    # all unusable
    self.uninstall("usr/share/sddm/themes")
    for pam in ["sddm", "sddm-autologin", "sddm-greeter"]:
        self.install_file(
            self.files_path / f"{pam}.pam", "usr/lib/pam.d", name=pam
        )


# recommended and installed by default, unless you override that
# if you do override that, you also need to set your compositor
# command correctly, or force x11, or whatever
@subpackage("sddm-default-breeze")
def _(self):
    self.subdesc = "Use Breeze theme by default"
    self.install_if = [self.parent]
    self.depends += [
        self.parent,
        "kwin",
        # input method
        "plasma-keyboard",
        "plasma-workspace",
    ]

    return ["usr/lib/sddm/sddm.conf.d/10-breeze-theme.conf"]
