pkgname = "plasma-desktop"
pkgver = "6.1.0"
pkgrel = 1
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
    "kaccounts-integration-devel",
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
    "plasma-welcome",  # welcome!
    # default themes, icons, sounds and wallpapers
    "breeze",
    "breeze-icons",
    "ocean-sound-theme",
    "plasma-workspace-wallpapers",
    # default KDE fonts
    "fonts-noto",
    "fonts-hack-ttf",
    "fonts-noto-emoji-ttf",
    # very default base stuff
    "accountsservice",
    "flatpak-kcm",
    "kactivitymanagerd",
    "kded",  # bg services
    "kgamma",
    "kio-admin",
    "kio-zeroconf",
    "kirigami-addons",  # needed by tons of apps, should be direct dep but also just pull it here
    "kscreen",
    "ksystemstats",
    "kwallet-pam",
    "kwalletmanager",
    "plasma-integration",
    "plasma-nm",
    "plasma-pa",
    "polkit-kde-agent-1",
    "powerdevil",
    "qqc2-breeze-style",
    "qqc2-desktop-style",
    "systemsettings",
    "udisks",
    "xdg-desktop-portal-kde",  # flatpak save dialog etc
    "xdg-user-dirs-gtk",
    "xdg-utils",
]
pkgdesc = "KDE Plasma Desktop"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://kde.org/plasma-desktop"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-desktop-{pkgver}.tar.xz"
sha256 = "0131c6688d9b021067e46d1c14b8a25895f06d0f4f771ff5e49de416044924ce"
# FIXME: cfi kills systemsettings (when entering "Date & Time") in kcm_clock.so
hardening = ["vis", "!cfi"]

# most kdepim stuff depends on messagelib which depends on qtwebengine
_have_kdepim = False
if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    _have_kdepim = True


@subpackage("plasma-desktop-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        # alternate older theme
        "oxygen",
        "oxygen-icons",
        "oxygen-sounds",
        # ?
        "baloo",  # search
        "bluedevil",  # bluetooth
        "colord-kde",  # color profile management
        # "drkonqi",  # TODO: figure out what crash handler to use (also is quite useless without coredumpd)
        "kde-cli-tools",  # e.g. mount & open external media
        "kde-inotify-survey",  # inotify limit monitor
        "kdeplasma-addons",  # bunch of desktop widgets
        "kdialog",  # scripted message boxes
        "kmenuedit",
        # "krdp",  # TODO: remote desktop server kcm for Plasma 6.2
        "ksshaskpass",  # graphical askpass
        "orca",  # screen reader
        "plasma-browser-integration",  # browser integration with plasma
        "plasma-disks",  # smart monitoring
        "plasma-firewall",  # firewall configuration
        "plasma-thunderbolt",  # user device authentication
        "print-manager",  # printer configuration
        "wacomtablet",  # wacom tablet settings
        "xwaylandvideobridge",  # x11 screen capture compat under wayland, TODO: test on baremetal
        # non-kde, misc integrations
        "desktop-file-utils",
        "fprintd-meta",
        # "iio-sensor-proxy",  # FIXME: package and test on device with accelerometer
        "power-profiles-daemon-meta",  # battery power saving
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
        "discover",  # extra app management
        "dolphin",  # file manager
        "konsole",  # terminal
        # - extra
        "ark",  # file (un)archiving
        "dolphin-plugins",
        "elisa",  # music player
        "ffmpegthumbs",  # video thumbnails
        "filelight",  # disk space usage viewer
        "gwenview",  # image viewer
        "haruna",  # mpv frontend
        "kalk",  # calculator
        "kate",  # text editor(s)
        "kcharselect",  # fonts character picker
        "kdeconnect",  # phone integration
        "kdenlive",  # video editor
        "kgpg",  # gpg integration
        "kinfocenter",  # system info
        "konversation",  # irc client
        # "krdc",  # vnc/rdp client
        "markdownpart",
        # "neochat",  # local WIP, matrix client
        "plasma-systemmonitor",
        "spectacle",  # screenshot
        "svgpart",
        "kcachegrind",  # callgrind data visualizer
        "ksystemlog",  # log viewer (TODO: does it ask for root itself?)
        "okular",  # document viewer
        "partitionmanager",  # partition manager
        "plasmatube",  # youtube client
        "skanlite",  # image scanner
        "yakuake",  # drop-down terminal
        # - still qt5
        # "digikam",  # photo management
        # "heaptrack",  # heap memory profiler
        # "kamoso",  # camera
        # "kipi-plugins",  # image export
        # "kmymoney",  # finance manager
        # "kompare",  # gui diff
        # "krita",  # digital art studio
    ]
    # things missing on some arches
    if self.rparent.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
        self.depends += [
            "akregator",  # rss feeds
            "khelpcenter",  # documentation viewer
            "tokodon",  # mastodon client
        ]
    if self.rparent.profile().arch in [
        "aarch64",
        "ppc64le",
        "riscv64",
        "x86_64",
    ]:
        self.depends += [
            # gocryptfs -> go
            # there are other backends too, but one is abandoned and the other needs fuse2
            "plasma-vault",  # encrypted file storage
        ]
    self.options = ["empty"]

    return []


@subpackage("plasma-desktop-kdepim-meta", _have_kdepim)
def _kdepin_meta(self):
    # contact/calendar/etc
    self.pkgdesc = f"{pkgdesc} (kdepim recommends package)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        "akonadi-import-wizard",
        "kaddressbook",
        "kalarm",
        "kdepim-addons",
        "kmail",
        "knotes",
        "kontact",
        "korganizer",
        "merkuro",
        "zanshin",
    ]
    self.options = ["empty"]

    return []
