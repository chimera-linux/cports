pkgname = "mangohud"
pkgver = "0.8.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dappend_libdir_mangohud=false",
    "-Dimgui:glfw=enabled",
    "-Dimgui:opengl=enabled",
    "-Dimgui:sdl2=enabled",
    "-Dimgui:vulkan=enabled",
    "-Dmangoapp=true",
    "-Dmangohudctl=true",
    "-Dtests=disabled",
    "-Dwith_xnvctrl=disabled",
]
hostmakedepends = [
    "appstream",
    "glslang-progs",
    "meson",
    "ninja",
    "pkgconf",
    "python-mako",
    "wayland-progs",
]
makedepends = [
    "dbus-devel",
    "glew-devel",
    "glfw-devel",
    "libcxx-devel-static",
    "libx11-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "sdl2-devel",
    "spdlog-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Vulkan and OpenGL overlay for monitoring FPS"
license = "MIT"
url = "https://github.com/flightlessmango/MangoHud"
source = f"{url}/releases/download/v{pkgver}/MangoHud-v{pkgver}-Source.tar.xz"
sha256 = "4c8d8098f5deff7737978d792eef909b7469933f456a47132dccc06804825482"
# checks disabled upstream
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
