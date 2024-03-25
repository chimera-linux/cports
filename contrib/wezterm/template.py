pkgname = "wezterm"
pkgver = "20240203"
_ref = "110809-5046fc22"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=distro-defaults,vendored-fonts,wayland",
    "--bins",
]
make_check_args = make_build_args + [
    "--",  # FIXME: takes issue with $HOME being /tmp ?
    "--skip=e2e::sftp",
]
hostmakedepends = [
    "cargo-auditable",
    "ncurses",
    "pkgconf",
    "python",
]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "libgit2-devel",
    "libpng-devel",
    "libssh2-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "lua5.4-devel",
    "ncurses-devel",
    "openssl-devel",
    "rust-std",
    "wayland-devel",
    "xcb-imdkit-devel",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-wm-devel",
    "zlib-devel",
    "zstd-devel",
]
checkdepends = ["openssh"]
pkgdesc = "Terminal emulator and multiplexer"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://wezfurlong.org/wezterm"
source = f"https://github.com/wez/wezterm/releases/download/{pkgver}-{_ref}/wezterm-{pkgver}-{_ref}-src.tar.gz"
sha256 = "df60b1081d402b5a9239cc4cef16fc699eab68bbbeac9c669cb5d991a6010b2c"


def pre_prepare(self):
    self.rm(".cargo/config")


def post_build(self):
    self.do("tic", "-x", "-o", "terminfo", "termwiz/data/wezterm.terminfo")


def do_install(self):
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_bin("wezterm")
        self.install_bin("wezterm-gui")
        self.install_bin("wezterm-mux-server")
        self.install_bin("generate-bidi")
        self.install_bin("strip-ansi-escapes")
        self.install_bin("sync-color-schemes")


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_files("terminfo", "usr/share")
    self.install_completion("assets/shell-completion/bash", "bash")
    self.install_completion("assets/shell-completion/fish", "fish")
    self.install_completion("assets/shell-completion/zsh", "zsh")
    self.install_file("assets/shell-integration/wezterm.sh", "etc/profile.d")
    self.install_file("assets/wezterm.desktop", "usr/share/applications")
    self.install_file("assets/wezterm.appdata.xml", "usr/share/metainfo")
    self.install_file(
        "assets/icon/wezterm-icon.svg",
        "usr/share/icons/hicolor/scalable/apps/",
        name="org.wezfurlong.wezterm.svg",
    )


@subpackage("wezterm-terminfo")
def _terminfo(self):
    self.pkgdesc = f"{pkgdesc} (terminfo data)"

    return ["usr/share/terminfo"]


@subpackage("wezterm-gui")
def _gui(self):
    self.pkgdesc = f"{pkgdesc} (gui)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "wezterm-terminfo"]

    return [
        "usr/bin/wezterm-gui",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/metainfo",
    ]


@subpackage("wezterm-mux-server")
def _mux(self):
    self.pkgdesc = f"{pkgdesc} (mux server)"

    return ["usr/bin/wezterm-mux-server"]


@subpackage("wezterm-utils")
def _utils(self):
    self.pkgdesc = f"{pkgdesc} (utilities)"

    return [
        "usr/bin/generate-bidi",
        "usr/bin/strip-ansi-escapes",
        "usr/bin/sync-color-schemes",
    ]
