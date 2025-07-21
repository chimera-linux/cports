pkgname = "mesa-amber"
pkgver = "21.3.9"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Ddefault_library=shared",
    "-Dcpp_std=gnu++14",
    "-Ddraw-use-llvm=false",
    "-Dglvnd=false",
    "-Dosmesa=true",
    "-Duse-elf-tls=false",
    "-Dgbm=enabled",
    "-Degl=enabled",
    "-Dgles1=enabled",
    "-Dgles2=enabled",
    "-Ddri3=enabled",
    "-Dgallium-vdpau=disabled",
    "-Dgallium-xvmc=disabled",
    "-Dllvm=disabled",
    "-Dlmsensors=enabled",
    "-Dshared-glapi=enabled",
    "-Dplatforms=x11,wayland",
    "-Dglx=dri",
]
hostmakedepends = [
    "bison",
    "flex",
    "glslang-progs",
    "meson",
    "pkgconf",
    "python-mako",
    "wayland-progs",
    "wayland-protocols",
]
makedepends = [
    # misc libs
    "elfutils-devel",
    "libarchive-devel",
    # base driver/platform stuff
    "libdrm-devel",
    "libexpat-devel",
    "libffi8-devel",
    # video accel
    "libva-bootstrap",
    # x11
    "libx11-devel",
    "libxcb-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxml2-devel",
    "libxrandr-devel",
    "libxshmfence-devel",
    "libxv-devel",
    "libxxf86vm-devel",
    "lm-sensors-devel",
    "lua5.4-devel",
    "ncurses-devel",
    # wayland
    "wayland-devel",
    "wayland-protocols",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
provides = [self.with_pkgver("mesa")]
provider_priority = 0
pkgdesc = "Mesa 3D Graphics Library"
license = "MIT"
url = "https://www.mesa3d.org"
source = f"https://archive.mesa3d.org/older-versions/21.x/mesa-{pkgver}.tar.xz"
sha256 = "91fe6f20339884e37a7c47bfba42fb1cd397512c9ed5ad423de369f047cd8b5c"
# lots of issues in swrast and so on
hardening = ["!int"]
# cba to deal with cross patching nonsense
options = ["!cross"]

_gallium_drivers = ["swrast"]
_dri_drivers = []
_vulkan_drivers = []

# these are good assumptions on all targets we support for now
_have_nvidia = True
_have_amd = True
_have_hwdec = True
_have_virgl = True

# these change with platforms
_have_intel = False
_have_vmware = False
_have_nine = False
_have_arm = False
_have_vulkan = False
_have_zink = False

match self.profile().arch:
    case "x86_64":
        _have_intel = True
        _have_vmware = True
        _have_nine = True
    case "aarch64":
        _have_arm = True
    case "ppc64le":
        configure_args += ["-Dpower8=true"]
    case "ppc64":
        configure_args += ["-Dpower8=false"]

_have_vulkan = _have_intel
_have_zink = _have_vulkan

if _have_amd:
    # no radeonsi because amber branch does not support our latest llvm
    # therefore, no radv either as that would not make any sense
    _gallium_drivers += ["r300", "r600"]
    _dri_drivers += ["r100", "r200"]

if _have_intel:
    _gallium_drivers += ["crocus", "iris"]
    _dri_drivers += ["i915", "i965"]
    if _have_vulkan:
        _vulkan_drivers += ["intel"]

if _have_nvidia:
    _gallium_drivers += ["nouveau"]
    _dri_drivers += ["nouveau"]
    if _have_arm:
        _gallium_drivers += ["tegra"]

if _have_arm:
    _gallium_drivers += [
        "kmsro",
        "v3d",
        "vc4",
        "freedreno",
        "etnaviv",
        "lima",
        "panfrost",
    ]

if _have_virgl:
    _gallium_drivers += ["virgl"]

if _have_nine:
    configure_args += ["-Dgallium-nine=true"]

if _have_vmware:
    _gallium_drivers += ["svga"]
    configure_args += ["-Dgallium-xa=enabled"]
else:
    configure_args += ["-Dgallium-xa=disabled"]

if _have_hwdec:
    configure_args += ["-Dgallium-va=enabled"]
else:
    configure_args += ["-Dgallium-va=disabled"]

if _have_vulkan:
    makedepends += ["vulkan-loader-devel"]
    configure_args += [
        "-Dvulkan-layers=device-select,overlay"
        + (",intel-nullhw" if _have_intel else "")
    ]

if _have_zink:
    _gallium_drivers += ["zink"]

configure_args += ["-Dgallium-drivers=" + ",".join(_gallium_drivers)]
configure_args += ["-Dvulkan-drivers=" + ",".join(_vulkan_drivers)]
configure_args += ["-Ddri-drivers=" + ",".join(_dri_drivers)]


def post_install(self):
    self.install_license("docs/license.rst")


@subpackage("mesa-amber-glapi-libs")
def _(self):
    self.pkgdesc = "Free implementation of the GL API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libglapi"),
        self.with_pkgver("libglapi-amber"),
        self.with_pkgver("mesa-glapi-libs"),
    ]

    return ["usr/lib/libglapi.so.*"]


@subpackage("mesa-amber-gbm-libs")
def _(self):
    self.pkgdesc = "Generic Buffer Management"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libgbm"),
        self.with_pkgver("libgbm-amber"),
        self.with_pkgver("mesa-gbm-libs"),
    ]

    return ["usr/lib/libgbm.so.*"]


@subpackage("mesa-amber-gbm-devel")
def _(self):
    self.pkgdesc = "Generic Buffer Management"
    self.provides = [
        self.with_pkgver("libgbm-devel"),
        self.with_pkgver("libgbm-amber-devel"),
        self.with_pkgver("mesa-gbm-devel"),
    ]
    self.depends += [self.parent]

    return [
        "usr/include/gbm.h",
        "usr/lib/libgbm.so",
        "usr/lib/pkgconfig/gbm.pc",
    ]


@subpackage("mesa-amber-osmesa-libs")
def _(self):
    self.pkgdesc = "Mesa off-screen interface"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libosmesa"),
        self.with_pkgver("libosmesa-amber"),
        self.with_pkgver("mesa-osmesa-libs"),
    ]

    return ["usr/lib/libOSMesa.so.*"]


@subpackage("mesa-amber-gles1-libs")
def _(self):
    self.pkgdesc = "Free implementation of OpenGL ES 1.x API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libgles1"),
        self.with_pkgver("libgles1-amber"),
        self.with_pkgver("mesa-gles1-libs"),
    ]

    return ["usr/lib/libGLESv1_CM.so.*"]


@subpackage("mesa-amber-gles2-libs")
def _(self):
    self.pkgdesc = "Free implementation of OpenGL ES 2.x API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libgles2"),
        self.with_pkgver("libgles2-amber"),
        self.with_pkgver("mesa-gles2-libs"),
    ]

    return ["usr/lib/libGLESv2.so.*"]


@subpackage("mesa-amber-egl-libs")
def _(self):
    self.pkgdesc = "Free implementation of the EGL API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libegl"),
        self.with_pkgver("libegl-amber"),
        self.with_pkgver("mesa-egl-libs"),
    ]

    return ["usr/lib/libEGL.so.*"]


@subpackage("mesa-amber-gl-libs")
def _(self):
    self.pkgdesc = "Free implementation of the OpenGL API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libgl"),
        self.with_pkgver("libgl-amber"),
        self.with_pkgver("mesa-gl-libs"),
    ]

    return ["usr/lib/libGL.so.*"]


@subpackage("mesa-amber-gallium-nine", _have_nine)
def _(self):
    self.pkgdesc = "Mesa implementation of D3D9"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("mesa-gallium-nine"),
        self.with_pkgver("mesa-gallium-nine-amber"),
    ]

    return ["usr/lib/d3d"]


@subpackage("mesa-amber-xatracker-libs", _have_vmware)
def _(self):
    self.pkgdesc = "X acceleration library"
    self.subdesc = "runtime library"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libxatracker"),
        self.with_pkgver("mesa-xatracker-libs"),
        self.with_pkgver("libxatracker-amber"),
    ]

    return ["usr/lib/libxatracker*.so.*"]


@subpackage("mesa-amber-dri")
def _(self):
    self.pkgdesc = "Mesa DRI drivers"
    self.depends += [self.parent]
    self.install_if = [self.parent]
    # transitional
    self.provides = [
        self.with_pkgver("mesa-vaapi"),
        self.with_pkgver("mesa-dri"),
        self.with_pkgver("mesa-dri-amber"),
    ]

    return ["usr/lib/dri"]


@subpackage("mesa-amber-vulkan", _have_vulkan)
def _(self):
    self.pkgdesc = "Mesa Vulkan drivers"
    self.install_if = [self.with_pkgver("mesa-dri-amber"), "vulkan-loader"]
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("mesa-vulkan"),
        self.with_pkgver("mesa-vulkan-amber"),
    ]

    return [
        "usr/bin/mesa-overlay-control.py",
        "usr/lib/libvulkan_*.so",
        "usr/lib/libVkLayer_*.so",
        "usr/share/vulkan/explicit_layer.d/VkLayer_*.json",
        "usr/share/vulkan/implicit_layer.d/VkLayer_*.json",
        "usr/share/vulkan/icd.d/*.json",
    ]


@subpackage("mesa-amber-devel")
def _(self):
    self.depends += [self.parent, self.with_pkgver("mesa-amber-gbm-devel")]
    self.provides = [self.with_pkgver("mesa-devel")]

    return self.default_devel()
