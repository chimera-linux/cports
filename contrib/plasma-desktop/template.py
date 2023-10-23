pkgname = "plasma-desktop"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
# FIXME: missing layout memory xml file? QTemporaryFile broken?
make_check_args = ["-E", "kcm-keyboard-keyboard_memory_persister_test"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "attica-devel",
    "ibus-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kded-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemmodels-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "krunner-devel",
    "kscreenlocker-devel",
    "ksvg-devel",
    "kwin-devel",
    "kxmlgui-devel",
    "libcanberra-devel",
    "libksysguard-devel",
    "libplasma-devel",
    "plasma-activities-devel",
    "plasma-activities-stats-devel",
    "plasma-wayland-protocols",
    "plasma-workspace-devel",
    "plasma5support-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "sdl-devel",
    "sonnet-devel",
    "wayland-protocols",
    "xcb-util-devel",
    "xserver-xorg-devel",
    "xserver-xorg-input-evdev-devel",
    "xserver-xorg-input-libinput-devel",
    # TODO: libaccounts-qt6-devel + kaccounts-integration-devel (OpenDesktop integration plugin)
    # TODO: signon-plugin-oauth2 (OAuth* login, OpenDesktop integration plugin, https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/tree/qt6 + other signon deps)
    # TODO: baloo-devel (File Search KCM)
    # TODO: PackageKitQt6? (Software Manager integration, KRunner plugin installer)
]
checkdepends = [
    "dbus",
    "iso-codes",
]
depends = [
    "kactivitymanagerd",
    "kirigami-addons",
    # accountsservice?
    # ibus (for /usr/share/ibus/dicts)?
]
pkgdesc = "KDE Plasma Desktop"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://kde.org/plasma-desktop"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-desktop-{pkgver}.tar.xz"
sha256 = "5d9001baea32e35055337667f204e28f206ebccaa0a172e0f109426ba8042ecf"
# FIXME: cfi kills systemsettings (when entering "Date & Time") in kcm_clock.so
hardening = ["vis", "!cfi"]


@subpackage("plasma-desktop-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        "kded",  # bg services
        "xdg-desktop-portal-kde",  # flatpak save dialog etc
        # default themes, icons, fonts, sounds and wallpapers
        "breeze",
        # "oxygen",
        # "oxygen-icons",
        # "oxygen-sounds"
        # "qqc2-desktop-style",  # TODO: decide if we want this to be automagically pulled in through kwindowsystem (or similar)
        "plasma-integration",
        "breeze-icons",
        "fonts-noto",
        "fonts-hack-ttf",
        "fonts-noto-emoji-ttf",
        "ocean-sound-theme",
        "plasma-workspace-wallpapers",
        "milou",  # krunner
        "kquickcharts",  # notifications
        "kscreen",  # display config, TODO: test on baremetal
        "kde-cli-tools",  # e.g. mount & open external media
        "xwaylandvideobridge",  # x11 screen capture compat under wayland, TODO: test on baremetal
        "powerdevil",  # power management daemon, TODO: test on baremetal
        "bluedevil",  # bluetooth
        "plasma-nm",  # network-manager integration
        "plasma-pa",  # pipewire-pulse audio integration
        # "ksystemstats",  # TODO: does anything call KSystemStats D-Bus etc? maybe some widget
        # "kde-inotify-survey",  # inotify limit monitor
        # "plasma-disks",  # smart monitoring
        # "kdialog",  # scripted message boxes
        # "polkit-kde-agent",  # password root auth prompts
        "fcitx5-configtool-meta",  # configure IME
        # "plasma-thunderbolt",  # user device authentication
        # "print-manager",
        # "colord-kde",  # color profile management
        # "kgamma",  # adjust monitor gamma
        # "drkonqi",  # TODO: figure out what crash handler to use
        # "kmenuedit",
        # "krdp",  # TODO: remote desktop server kcm for Plasma 6.2
        # non-kde
        # "power-profiles-daemon-meta",  # battery power saving
        "udisks",  # removable disks applet
        # "fprintd-meta",  # TODO: test on baremetal
        # "iio-sensor-proxy",  # FIXME: package and test on device with accelerometer
        # "xdg-utils",  # TODO: missing this probably breaks opening various links at least?
        # "desktop-file-utils",
        # "xdg-user-dirs-gtk",
    ]
    self.options = ["empty"]

    return []


@subpackage("plasma-desktop-x11-meta")
def _x11_meta(self):
    self.pkgdesc = f"{pkgdesc} (X11 session recommends package)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        "xserver-xorg-input-libinput",  # general input
        # "xserver-xorg-input-evdev",  # TODO: used by mouse KCM? page loads even without it at least
        "setxkbmap",  # configure non-us layout
        # "qt6-qtvirtualkeyboard",  # lockscreen virtual keyboard, any alternative that's also usable on wayland side (too?) -> maliit
    ]
    self.options = ["empty"]

    return []


@subpackage("plasma-desktop-apps-meta")
def _apps_meta(self):
    self.pkgdesc = f"{pkgdesc} (apps recommends package)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        # core
        "systemsettings",
        "konsole",  # terminal
        "dolphin",  # file manager
        # extra
        # "kio-admin",
        # "kio-fuse",
        # "kio-extras",
        # "dolphin-plugins",
        # "ffmpegthumbs",
        "kinfocenter",
        "spectacle",  # screenshot
        # "kipi-plugins",  # image export
        # "gwenview",  # image viewer
        "kate",  # text editor(s)
        # "markdownpart",
        # "svgpart",
        "plasma-systemmonitor",
        # "ark",  # local WIP, file (un)archiving
        # "merkuro",  # calendar
        # "haruna",  # local WIP, mpv frontend
        # "elisa",  # music player
        # "kdenlive",  # video editor
        # "kalk",  # calculator
        # "kamoso",  # camera
        # "neochat",  # local WIP, matrix client
        # "kcharselect",  # fonts character picker
        # "kdeconnect",  # phone integration
        # "khelpcenter",  # kde documentation viewer
        # "knotes",  # sticky notes
        # "kompare",  # gui diff
        # "konversation",  # irc client
        # "krdc",  # vnc/rdp client
        # "ksystemlog",  # log viewer
        # "kwalletmanager",
        # "okular",  # document viewer
        # "filelight",
        # "partitionmanager",
        # "plasmatube",  # youtube client
        # "skanlite",  # image scanner
        # "tokodon",  # mastodon client
        # "yakuake",  # drop-down terminal
        # "zanshin",  # todo
        # "heaptrack",  # heap memory profiler
        # "kcachegrind",  # callgrind data visualizer
        # "krita",  # digital art studio
    ]
    if self.rparent.profile().arch != "riscv64":
        # FIXME: qmake busted under emulation (https://bugreports.qt.io/browse/QTBUG-98951)
        self.depends += ["qalculate-qt"]
    self.options = ["empty"]

    return []
