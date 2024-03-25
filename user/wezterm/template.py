pkgname = "wezterm"
pkgver = "20240811"
_ref = "0ac1e948c5b4fb1d1dee532eba36c4669a64774e"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
make_build_args = [
    "--no-default-features",
    "--features=distro-defaults,vendored-fonts,wayland",
    "--bins",
]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=e2e::agent_forward",
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
    "pixman-devel",
    "rust-std",
    "sqlite-devel",
    "wayland-devel",
    "xcb-imdkit-devel",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-wm-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["openssh"]
pkgdesc = "Terminal emulator and multiplexer"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://wezfurlong.org/wezterm"
source = f"https://github.com/wez/wezterm/archive/{_ref}.tar.gz"
sha256 = "c806fe79f011c68393878e10ef61a17c5b45350685022c4fa6a1e9cf1c52f990"


def post_build(self):
    self.do("tic", "-x", "-o", "terminfo", "termwiz/data/wezterm.terminfo")


def install(self):
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
def _(self):
    self.subdesc = "terminfo data"

    return ["usr/share/terminfo"]


@subpackage("wezterm-gui")
def _(self):
    self.subdesc = "gui"
    self.install_if = [self.parent]
    self.depends = [self.with_pkgver("wezterm-terminfo")]

    return [
        "usr/bin/wezterm-gui",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/metainfo",
    ]


@subpackage("wezterm-mux-server")
def _(self):
    self.subdesc = "mux server"

    return ["usr/bin/wezterm-mux-server"]


@subpackage("wezterm-utils")
def _(self):
    self.subdesc = "utilities"

    return [
        "usr/bin/generate-bidi",
        "usr/bin/strip-ansi-escapes",
        "usr/bin/sync-color-schemes",
    ]
