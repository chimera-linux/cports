pkgname = "sddm"
pkgver = "0.21.0"
pkgrel = 3
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
    "elogind-devel",
    "linux-pam-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
depends = [
    "dinit-dbus",
    "elogind",
    "plasma-workspace",
    "turnstile",
    "xrdb",
    "xserver-xorg-input-libinput",
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
        self.files_path / "sddm.config",
        "usr/lib/sddm/sddm.conf.d",
        name="default.conf",
    )
    # TODO: we add a hard dependency on plasma-workspace and default to breeze
    # here, because all the default themes (except maui) and most third-party
    # themes depend on the qt5 greeter,
    # and breeze just looks way better
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
