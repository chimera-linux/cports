pkgname = "hyprland"
pkgver = "0.46.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "ninja", "cmake", "pkgconf"]
makedepends = [
	"udis86-devel",
	"elogind-devel",
	"aquamarine-devel",
	"hyprcursor-devel",
	"hyprgraphics-devel",
	"hyprland-protocols",
	"hyprlang",
	"hyprutils-devel",
	"hyprwayland-scanner",
	"jq",
	"libdrm-devel",
	"libinput-devel",
	"libliftoff-devel",
	"libxcb-devel",
	"libxcursor-devel",
	"libxkbcommon-devel",
	"mesa-devel",
	"pango-devel",
	"pixman-devel",
	"re2-devel",
	"tomlplusplus-devel",
	"udis86-devel",
	"vulkan-loader-devel",
	"wayland-devel",
	"wayland-protocols",
	"xcb-util-errors-devel",
	"xcb-util-image-devel",
	"xcb-util-renderutil-devel",
	"xcb-util-wm-devel",
	"xkeyboard-config",
	"xwayland-devel",
]
depends = ["xwayland", "xdg-desktop-portal-hyprland", "hyprland-qtutils"]
pkgdesc = "Dynamic tiling Wayland compositor that doesn't sacrifice on its looks"
maintainer = "kkflt <kkftl@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://hyprland.org"
source = f"https://github.com/hyprwm/Hyprland/releases/download/v{pkgver}/source-v{pkgver}.tar.gz"
sha256 = "d072b50ac0bc48aebea7d0bdb3a0188c62103dde42ff3127a9962437f599b0c1"

def post_install(self):
	self.install_license("LICENSE")
