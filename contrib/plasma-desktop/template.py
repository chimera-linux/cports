pkgname = "plasma-desktop"
pkgver = "6.0.5"
pkgrel = 8
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
    "baloo-devel",
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
    # TODO: PackageKitQt6? (Software Manager integration, KRunner plugin installer)
]
checkdepends = [
    "dbus",
    "iso-codes",
]
depends = [
    "kactivitymanagerd",
    "kirigami-addons",
]
pkgdesc = "KDE Plasma Desktop"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://kde.org/plasma-desktop"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-desktop-{pkgver}.tar.xz"
sha256 = "5d9001baea32e35055337667f204e28f206ebccaa0a172e0f109426ba8042ecf"
# FIXME: cfi kills systemsettings (when entering "Date & Time") in kcm_clock.so
hardening = ["vis", "!cfi"]

if self.profile().arch != "riscv64":
    # -> libaccounts-qt qmake broken
    makedepends += ["kaccounts-integration-devel"]


@subpackage("plasma-desktop-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        "kded",  # bg services
        "xdg-desktop-portal-kde",  # flatpak save dialog etc
        # welcome!
        "plasma-welcome",
        # default themes, icons, sounds and wallpapers
        "breeze",
        "breeze-icons",
        "ocean-sound-theme",
        "oxygen",
        "oxygen-icons",
        "oxygen-sounds",
        "plasma-workspace-wallpapers",
        "qqc2-breeze-style",
        "qqc2-desktop-style",  # TODO: decide if we want this to be automagically pulled in through kwindowsystem (or similar)
        # default fonts
        "fonts-noto",
        "fonts-hack-ttf",
        "fonts-noto-emoji-ttf",
        # ?
        "baloo",  # search
        "bluedevil",  # bluetooth
        "kde-cli-tools",  # e.g. mount & open external media
        "kquickcharts",  # notifications
        "kscreen",  # display config, TODO: test on baremetal
        "ksshaskpass",  # graphical askpass
        "kio-admin",
        "kio-fuse",
        "kio-extras",
        "kio-zeroconf",
        "milou",  # krunner
        "plasma-browser-integration",  # browser integration with plasma
        "plasma-integration",
        "plasma-nm",  # network-manager integration
        "plasma-pa",  # pipewire-pulse audio integration
        "powerdevil",  # power management daemon, TODO: test on baremetal
        "xwaylandvideobridge",  # x11 screen capture compat under wayland, TODO: test on baremetal
        "ksystemstats",  # TODO: does anything call KSystemStats D-Bus etc? maybe some widget
        "kde-inotify-survey",  # inotify limit monitor
        "plasma-disks",  # smart monitoring
        "kdialog",  # scripted message boxes
        "polkit-kde-agent-1",  # password root auth prompts
        "fcitx5-configtool-kde-meta",  # configure IME
        "plasma-thunderbolt",  # user device authentication
        "colord-kde",  # color profile management
        "flatpak-kcm",  # flatpak permissions
        "kgamma",  # adjust monitor gamma
        "print-manager",  # printer configuration
        # "drkonqi",  # TODO: figure out what crash handler to use
        "kmenuedit",
        # "krdp",  # TODO: remote desktop server kcm for Plasma 6.2
        # non-kde, misc integrations
        "desktop-file-utils",
        "fprintd-meta",  # TODO: test on baremetal
        # "iio-sensor-proxy",  # FIXME: package and test on device with accelerometer
        "power-profiles-daemon-meta",  # battery power saving
        "udisks",  # removable disks applet
        "xdg-user-dirs-gtk",
        "xdg-utils",  # TODO: missing this probably breaks opening various links at least?
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
        "qt6-qtvirtualkeyboard",  # lockscreen virtual keyboard, any alternative that's also usable on wayland side (too?) -> maliit
    ]
    self.options = ["empty"]

    return []


@subpackage("plasma-desktop-apps-meta")
def _apps_meta(self):
    self.pkgdesc = f"{pkgdesc} (apps recommends package)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        # - core
        "systemsettings",
        "konsole",  # terminal
        "dolphin",  # file manager
        # - extra
        "discover",  # extra app management
        "dolphin-plugins",
        "ffmpegthumbs",  # video thumbnails
        "kinfocenter",  # system info
        "spectacle",  # screenshot
        "gwenview",  # image viewer
        "kate",  # text editor(s)
        "markdownpart",
        "svgpart",
        "plasma-systemmonitor",
        "plasma-vault",  # encrypted file storage
        # "ark",  # local WIP, file (un)archiving
        # "haruna",  # local WIP, mpv frontend
        "elisa",  # music player
        "kdenlive",  # video editor
        "kalk",  # calculator
        # "neochat",  # local WIP, matrix client
        "kcharselect",  # fonts character picker
        "kdeconnect",  # phone integration
        "konversation",  # irc client
        # "krdc",  # vnc/rdp client
        "ksystemlog",  # log viewer (TODO: does it ask for root itself?)
        "okular",  # document viewer
        "filelight",  # disk space usage viewer
        "partitionmanager",  # partition manager
        "plasmatube",  # youtube client
        "skanlite",  # image scanner
        "yakuake",  # drop-down terminal
        "kcachegrind",  # callgrind data visualizer
        # - passwords
        "kwallet",
        "kwallet-pam",
        "kwalletmanager",
        # - akonadi stuff (mariadb)
        # "kontact",  # contacts
        # "merkuro",  # calendar
        # "zanshin",  # productivity app
        # "knotes",  # sticky notes
        # - still qt5
        # "heaptrack",  # heap memory profiler
        # "kamoso",  # camera
        # "kompare",  # gui diff
        # "kipi-plugins",  # image export
        # "krita",  # digital art studio
    ]
    # things missing on some arches
    if self.rparent.profile().arch != "riscv64":
        self.depends += ["qalculate-qt"]
    if self.rparent.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
        self.depends += [
            "khelpcenter",  # documentation viewer
            "tokodon",  # mastodon client
        ]
    self.options = ["empty"]

    return []
