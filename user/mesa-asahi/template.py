pkgname = "mesa-asahi"
pkgver = "20250221"
pkgrel = 0
archs = ["aarch64"]
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Ddefault_library=shared",
    "-Degl=enabled",
    "-Dgbm=enabled",
    "-Dgles1=enabled",
    "-Dgles2=enabled",
    "-Dglvnd=disabled",
    "-Dglx=dri",
    "-Dllvm=enabled",
    "-Dlmsensors=enabled",
    "-Dosmesa=true",
    "-Dplatforms=x11,wayland",
    "-Dshared-glapi=enabled",
    "-Dvideo-codecs=all",
    "-Dgallium-vdpau=disabled",
]
hostmakedepends = [
    "bison",
    "cbindgen",
    "flex",
    "glslang-progs",
    "meson",
    "pkgconf",
    "python-mako",
    "python-ply",
    "python-pycparser",
    "python-pyyaml",
    "wayland-progs",
    "wayland-protocols",
]
makedepends = [
    "clang-devel",
    "llvm-devel",
    # base driver/platform stuff
    "libdrm-devel",
    # wayland
    "wayland-devel",
    "wayland-protocols",
    # x11
    "libx11-devel",
    "libxcb-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxrandr-devel",
    "libxshmfence-devel",
    "libxv-devel",
    "libxxf86vm-devel",
    # misc libs
    "elfutils-devel",
    "libarchive-devel",
    "libexpat-devel",
    "libffi8-devel",
    "libxml2-devel",
    "lm-sensors-devel",
    "lua5.4-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
    # video accel
    "libva-bootstrap",
]
provides = [self.with_pkgver("mesa")]
provider_priority = 0
pkgdesc = "Asahi Linux fork of the Mesa 3D Graphics Library"
license = "MIT"
url = "https://gitlab.freedesktop.org/asahi/mesa"
# so we don't also download vendored system libs, just rlib names
_subproject_list = [
    "equivalent",
    "hashbrown",
    "indexmap",
    "once-cell",
    "paste",
    "pest",
    "pest_derive",
    "pest_generator",
    "pest_meta",
    "proc-macro2",
    "quote",
    "roxmltree",
    "syn",
    "ucd-trie",
    "unicode-ident",
]
source = f"https://gitlab.freedesktop.org/asahi/mesa/-/archive/asahi-{pkgver}/mesa-asahi-{pkgver}.tar.gz"
sha256 = "3d8c4ca48b8cc420059968badc45141d68af762f57cac5bdb56a6af6d7ed9369"
# lots of issues in swrast and so on
hardening = ["!int"]
# cba to deal with cross patching nonsense
options = ["!cross", "linkundefver", "fullrustflags"]

_gallium_drivers = ["asahi"]
_vulkan_drivers = ["asahi"]
_have_llvm = True

if _have_llvm:
    configure_args += ["-Dllvm-orcjit=true"]
    _gallium_drivers += ["llvmpipe"]
    _vulkan_drivers += ["swrast"]

_have_hwdec = False
_have_opencl = True
_have_vulkan = True
_have_zink = True

if _have_opencl:
    makedepends += [
        "libclc",
        "spirv-llvm-translator-devel",
        "spirv-tools-devel",
    ]
    configure_args += [
        "-Dgallium-opencl=icd",
        "-Dgallium-rusticl=true",
    ]

# nvk/nouveau or rusticl need rust
if _have_opencl:
    hostmakedepends += ["rust-bindgen", "rust"]
    makedepends += ["rust"]

if _have_hwdec:
    configure_args += ["-Dgallium-va=enabled"]
else:
    configure_args += ["-Dgallium-va=disabled"]

if _have_vulkan:
    makedepends += ["vulkan-loader-devel"]
    configure_args += ["-Dvulkan-layers=device-select,overlay"]

if _have_zink:
    _gallium_drivers += ["zink"]

configure_args += ["-Dgallium-drivers=" + ",".join(_gallium_drivers)]
configure_args += ["-Dvulkan-drivers=" + ",".join(_vulkan_drivers)]


def post_extract(self):
    with open(self.cwd / "VERSION", "w") as f:
        f.write(self.pkgver)


def post_patch(self):
    self.do(
        "meson",
        "subprojects",
        "download",
        *_subproject_list,
        allow_network=True,
    )


def init_configure(self):
    ljobs = 4 if self.make_jobs >= 4 else self.make_jobs
    # mesa links a lot of big .so's at once so ensure there is not more than four
    self.configure_args += [f"-Dbackend_max_links={ljobs}"]


def post_install(self):
    self.install_license("docs/license.rst")


@subpackage("mesa-asahi-gbm-libs")
def _(self):
    self.pkgdesc = "Generic Buffer Management"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libgbm"),
        self.with_pkgver("mesa-gbm-libs"),
    ]

    return [
        "usr/lib/gbm",
        "usr/lib/libgbm.so.*",
    ]


@subpackage("mesa-asahi-gbm-devel")
def _(self):
    self.pkgdesc = "Generic Buffer Management"
    self.provides = [
        self.with_pkgver("libgbm-devel"),
        self.with_pkgver("mesa-gbm-devel"),
    ]

    return [
        "usr/include/gbm.h",
        "usr/lib/libgbm.so",
        "usr/lib/pkgconfig/gbm.pc",
    ]


@subpackage("mesa-asahi-osmesa-libs")
def _(self):
    self.pkgdesc = "Mesa off-screen interface"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libosmesa"),
        self.with_pkgver("mesa-osmesa-libs"),
    ]

    return ["usr/lib/libOSMesa.so.*"]


@subpackage("mesa-asahi-gles1-libs")
def _(self):
    self.pkgdesc = "Free implementation of OpenGL ES 1.x API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libgles1"),
        self.with_pkgver("mesa-gles1-libs"),
    ]

    return ["usr/lib/libGLESv1_CM.so.*"]


@subpackage("mesa-asahi-gles2-libs")
def _(self):
    self.pkgdesc = "Free implementation of OpenGL ES 2.x API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libgles2"),
        self.with_pkgver("mesa-gles2-libs"),
    ]

    return ["usr/lib/libGLESv2.so.*"]


@subpackage("mesa-asahi-egl-libs")
def _(self):
    self.pkgdesc = "Free implementation of the EGL API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libegl"),
        self.with_pkgver("mesa-egl-libs"),
    ]

    return ["usr/lib/libEGL.so.*"]


@subpackage("mesa-asahi-gl-libs")
def _(self):
    self.pkgdesc = "Free implementation of the OpenGL API"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("libgl"),
        self.with_pkgver("mesa-gl-libs"),
    ]

    return ["usr/lib/libGL.so.*"]


@subpackage("mesa-asahi-opencl", _have_opencl)
def _(self):
    self.pkgdesc = "Mesa implementation of OpenCL"
    self.depends += [self.parent, "libclc"]
    self.provides = [self.with_pkgver("mesa-opencl")]

    return [
        "etc/OpenCL",
        "usr/lib/gallium-pipe",
        "usr/lib/libMesaOpenCL.so.*",
        "usr/lib/libRusticlOpenCL.so.*",
    ]


@subpackage("mesa-asahi-libgallium")
def _(self):
    self.pkgdesc = "Mesa gallium loader"
    self.depends += [self.parent]
    self.provides = [
        self.with_pkgver("mesa-libgallium"),
        self.with_pkgver("libglapi"),
        self.with_pkgver("mesa-glapi-libs"),
    ]

    return ["usr/lib/libgallium-*.so"]


@subpackage("mesa-asahi-dri")
def _(self):
    self.pkgdesc = "Mesa DRI drivers"
    self.depends += [self.parent]
    self.install_if = [self.parent]
    self.provides = [
        self.with_pkgver("mesa-vaapi"),
        self.with_pkgver("mesa-dri"),
    ]

    return ["usr/lib/dri"]


@subpackage("mesa-asahi-vulkan", _have_vulkan)
def _(self):
    self.pkgdesc = "Mesa Vulkan drivers"
    self.depends += [self.parent]
    self.install_if = [self.with_pkgver("mesa-dri"), "vulkan-loader"]
    self.provides = [self.with_pkgver("mesa-vulkan")]

    return [
        "usr/bin/mesa-overlay-control.py",
        "usr/lib/libvulkan_*.so",
        "usr/lib/libVkLayer_*.so",
        "usr/share/vulkan/explicit_layer.d/VkLayer_*.json",
        "usr/share/vulkan/implicit_layer.d/VkLayer_*.json",
        "usr/share/vulkan/icd.d/*_icd*.json",
    ]


@subpackage("mesa-asahi-devel")
def _(self):
    self.depends += [self.parent, self.with_pkgver("mesa-asahi-gbm-devel")]
    self.provides = [self.with_pkgver("mesa-devel")]

    return self.default_devel()
