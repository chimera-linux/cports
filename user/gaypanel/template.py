pkgname = "gaypanel"
pkgver = "1.0.0"
pkgrel = 1
build_style = "cargo"
make_build_args = [
    "--locked",
    "--bin",
    "gaypanel",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "rust-std",
]
makedepends = [
    "alsa-lib-devel",
    "blueprint-compiler",
    "dbus-devel",
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "libadwaita-devel",
    "libxkbcommon-devel",
    "openssl3",
    "pkgconf",
]
depends = [
    # technically a recommendation, not requirement, fallback for missing icons
    "adwaita-icon-theme",
    "alsa-lib",
    "blueprint-compiler",
    "bluez",
    "gtk4",
    "libadwaita",
    "libxkbcommon",
    "networkmanager",
    "openssl3",
]
pkgdesc = "Panel for Wayland compositors"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/pastthepixels/gaypanel"
source = f"https://codeberg.org/pastthepixels/gaypanel/archive/v{pkgver}.tar.gz"
sha256 = "5a9f9d2279b917217c8b098b85c2c0c4487feb799e4e296e27300ae5981e444f"
