pkgname = "plasma-desktop"
pkgver = "6.2.4"
pkgrel = 1
build_style = "cmake"
# FIXME: missing layout memory xml file? QTemporaryFile broken?
# tst_calibrationtool: broken on ppc64le
make_check_args = [
    "-E",
    "(kcm-keyboard-keyboard_memory_persister_test|tst_calibrationtool)",
]
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
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
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
    "fonts-hack-ttf",
    "fonts-noto",
    "fonts-noto-emoji-ttf",
    # very default base stuff
    "accountsservice",
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
sha256 = "81f2ab40cdec332918c90b1b732abb2aa0c0502854e48b8fa06fb82b52924da3"
hardening = ["vis"]

# most kdepim stuff depends on messagelib which depends on qtwebengine
_have_kdepim = False
if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    _have_kdepim = True


def post_install(self):
    self.uninstall("usr/lib/systemd/user/plasma-kaccess.service")


@subpackage("plasma-desktop-meta")
def _(self):
    self.subdesc = "recommends package"
    self.install_if = [self.parent]
    self.depends = [
        # alternate older theme
        "oxygen",
        "oxygen-icons",
        "oxygen-sounds",
        # breeze gtk theme
        "breeze-gtk",
        "kde-gtk-config",
        # QImage plugins for various images
        "kimageformats",
        "qt6-qtimageformats",
        # ?
        "baloo",  # search
        "bluedevil",  # bluetooth
        "colord-kde",  # color profile management
        # "drkonqi",  # TODO: figure out what crash handler to use (also is quite useless without coredumpd)
        "flatpak-kcm",  # flatpak permission settings
        "kaccounts-providers",  # online account providers
        "kde-cli-tools",  # e.g. mount & open external media
        "kde-inotify-survey",  # inotify limit monitor
        "kdegraphics-thumbnailers",  # various thumbnailers
        "kdenetwork-filesharing",  # network file sharing
        "kdeplasma-addons",  # bunch of desktop widgets
        "kdialog",  # scripted message boxes
        "kio-gdrive",  # kio plugin for gdrive
        "kmenuedit",
        # "krdp",  # (requires systemd): remote desktop server kcm for Plasma 6.2
        "ksshaskpass",  # graphical askpass
        "markdownpart",  # markdown renderer kpart plugin
        "plasma-browser-integration",  # browser integration with plasma
        "plasma-disks",  # smart monitoring
        "plasma-firewall",  # firewall configuration
        "plasma-thunderbolt",  # user device authentication
        "print-manager",  # printer configuration
        "svgpart",  # svg renderer kpart plugin
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
def _(self):
    self.subdesc = "X11 session recommends package"
    self.depends = [
        "xserver-xorg-input-libinput",  # general input
        # "xserver-xorg-input-evdev",  # TODO: used by mouse KCM? page loads even without it at least
        "setxkbmap",  # configure non-us layout
        "qt6-qtvirtualkeyboard",  # lockscreen virtual keyboard, any alternative that's also usable on wayland side (too?) -> maliit
    ]
    self.install_if = [self.parent, "xserver-xorg-core"]
    self.options = ["empty"]

    return []


@subpackage("plasma-desktop-apps-meta")
def _(self):
    self.subdesc = "apps recommends package"
    self.install_if = [self.with_pkgver("plasma-desktop-meta")]
    self.depends = [
        # - core
        "discover",  # extra app management
        "dolphin",  # file manager
        "konsole",  # terminal
        # - extra
        "ark",  # file (un)archiving
        "dolphin-plugins",
        "filelight",  # disk space usage viewer
        "francis",  # time tracker
        "gwenview",  # image viewer
        "haruna",  # mpv frontend
        "isoimagewriter",  # iso to usb writer
        "kalk",  # calculator
        "kate",  # text editor(s)
        "kcachegrind",  # callgrind data visualizer
        "kcharselect",  # fonts character picker
        "kcolorchooser",  # color palette tool
        "kdebugsettings",  # qloggingcategory display editor
        "kdeconnect",  # phone integration
        "keditbookmarks",  # bookmark editor
        "kget",  # download manager
        "kgpg",  # gpg integration
        "kinfocenter",  # system info
        "konversation",  # irc client
        "krdc",  # vnc/rdp client
        "kruler",  # on screen ruler
        "ksystemlog",  # log viewer (TODO: does it ask for root itself?)
        "ktorrent",  # torrent client
        "ktrip",  # trip planner
        "okular",  # document viewer
        "partitionmanager",  # partition manager
        "plasma-systemmonitor",
        "skanlite",  # image scanner
        # "skanpage",  # document scanner (TODO: tesseract)
        "spectacle",  # screenshot
        "sweeper",  # cache cleaner
        "yakuake",  # drop-down terminal
        # "neochat",  # local WIP, matrix client
        # - still qt5
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
            "digikam",  # photo manager
            "ghostwriter",  # markdown editor
            "khelpcenter",  # documentation viewer
            "konqueror",  # web browser
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


@subpackage("plasma-desktop-multimedia-meta")
def _(self):
    self.subdesc = "multimedia recommends package"
    self.install_if = [self.with_pkgver("plasma-desktop-meta")]
    self.depends = [
        "audiocd-kio",  # kio plugin for audio cds
        "audiotube",  # youtube music client
        "elisa",  # music player
        "ffmpegthumbs",  # video thumbnails
        # "k3b",  # disc ripper TODO: bunch of dvd/cd tools
        "kasts",  # podcast player
        "kdenlive",  # video editor
        "juk",  # music player and manager
        "plasmatube",  # youtube client
    ]
    self.options = ["empty"]
    return []


@subpackage("plasma-desktop-devtools-meta")
def _(self):
    self.subdesc = "devtools recommends package"
    self.install_if = [self.with_pkgver("plasma-desktop-meta")]
    self.depends = [
        "heaptrack",
        "kcachegrind",
        "massif-visualizer",
    ]
    self.options = ["empty"]
    return []


@subpackage("plasma-desktop-games-meta")
def _(self):
    self.subdesc = "games recommends package"
    self.install_if = [self.with_pkgver("plasma-desktop-meta")]
    self.depends = [
        "kpat",
    ]
    self.options = ["empty"]
    return []


@subpackage("plasma-desktop-accessibility-meta")
def _(self):
    self.subdesc = "accessibility recommends package"
    self.install_if = [self.with_pkgver("plasma-desktop-meta")]
    self.depends = [
        "accessibility-inspector",  # accesibility tree inspector
        # "kmag",  # magnifier TODO: broken?
        # "kmousetool",  # mouse clicker TODO: broken?
        # "kmouth",  # speech synthesizer TODO: hangs forever on init until speechd killed, orca works better
        "kontrast",  # contrast checker
        "orca",  # screen reader
    ]
    self.options = ["empty"]
    return []


@subpackage("plasma-desktop-kdepim-meta", _have_kdepim)
def _(self):
    # contact/calendar/etc
    self.subdesc = "kdepim recommends package"
    self.install_if = [self.with_pkgver("plasma-desktop-meta")]
    self.depends = [
        "akonadi-calendar-tools",
        "akonadi-import-wizard",
        "grantlee-editor",
        "itinerary",
        "kaddressbook",
        "kalarm",
        "kdepim-addons",
        #  "kleopatra", TODO: crashes in certificate search in std::sort
        "kmail",
        "kontact",
        "korganizer",
        "merkuro",
        "zanshin",
    ]
    self.options = ["empty"]

    return []


@subpackage("plasma-desktop-sddm-meta")
def _(self):
    self.subdesc = "SDDM recommends package"
    self.install_if = [self.parent]
    self.depends = [
        "sddm",
        "sddm-kcm",
    ]
    self.options = ["empty"]

    return []
