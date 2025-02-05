pkgname = "mesa"
pkgver = "24.3.4"
pkgrel = 1
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
provider_priority = 999
pkgdesc = "Mesa 3D Graphics Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.mesa3d.org"
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
source = f"https://mesa.freedesktop.org/archive/mesa-{pkgver.replace('_', '-')}.tar.xz"
sha256 = "e641ae27191d387599219694560d221b7feaa91c900bcec46bf444218ed66025"
# lots of issues in swrast and so on
hardening = ["!int"]
# cba to deal with cross patching nonsense
options = ["!cross", "linkundefver", "fullrustflags"]

_gallium_drivers = []
_vulkan_drivers = []
_have_llvm = False

# llvmpipe only properly supports a few archs
match self.profile().arch:
    case "x86_64" | "aarch64" | "ppc64le" | "riscv64":
        _have_llvm = True
    case _:
        configure_args += ["-Ddraw-use-llvm=false"]
        # llvmpipe is strictly better so only bring this in where it isn't
        _gallium_drivers += ["softpipe"]

if _have_llvm:
    configure_args += ["-Dllvm-orcjit=true"]
    _gallium_drivers += ["llvmpipe"]
    _vulkan_drivers += ["swrast"]

# these are good assumptions on all targets we support for now
_have_nvidia = True
_have_amd = True
# intel_clc fails on big
_have_intel = self.profile().endian != "big"
_have_hwdec = True
_have_virgl = True

# these change with platforms
_have_intel_igpu = False
_have_vmware = False
_have_nine = False
_have_arm = False
_have_opencl = False
_have_vulkan = False
_have_zink = False

match self.profile().arch:
    case "x86_64":
        _have_intel = True
        _have_intel_igpu = True
        _have_vmware = True
        _have_nine = True
    case "aarch64":
        _have_arm = True
    case "ppc64le":
        configure_args += ["-Dpower8=true"]
    case "ppc64":
        configure_args += ["-Dpower8=false"]

_have_opencl = _have_amd or _have_intel
_have_vulkan = _have_amd or _have_intel or _have_arm
_have_zink = _have_vulkan

if _have_amd:
    _gallium_drivers += ["r300", "r600", "radeonsi"]
    if _have_vulkan:
        _vulkan_drivers += ["amd"]

if _have_intel:
    _gallium_drivers += ["iris"]
    if _have_vulkan:
        _vulkan_drivers += ["intel"]

if _have_intel_igpu:
    _gallium_drivers += ["crocus", "i915"]
    if _have_vulkan:
        _vulkan_drivers += ["intel_hasvk"]

if _have_nvidia:
    _gallium_drivers += ["nouveau"]
    _vulkan_drivers += ["nouveau"]
    if _have_arm:
        _gallium_drivers += ["tegra"]

if _have_arm:
    _gallium_drivers += [
        "v3d",
        "vc4",
        "freedreno",
        "etnaviv",
        "lima",
        "panfrost",
    ]
    if _have_vulkan:
        _vulkan_drivers += ["broadcom", "freedreno", "panfrost"]

if _have_virgl:
    _gallium_drivers += ["virgl"]
    _vulkan_drivers += ["virtio"]

if _have_nine:
    configure_args += ["-Dgallium-nine=true"]

if _have_vmware:
    _gallium_drivers += ["svga"]
    configure_args += ["-Dgallium-xa=enabled"]
else:
    configure_args += ["-Dgallium-xa=disabled"]

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
if _have_opencl or _have_nvidia:
    hostmakedepends += ["rust-bindgen", "rust"]
    makedepends += ["rust"]

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
    self.install_file(
        self.files_path / "00-radeonsi-gnome-no-glthread.conf",
        "usr/share/drirc.d",
    )
    self.install_license("docs/license.rst")


@subpackage("mesa-glapi-libs")
def _(self):
    self.pkgdesc = "Free implementation of the GL API"
    self.depends += [self.parent]
    # transitional
    self.provides = [self.with_pkgver("libglapi")]

    return ["usr/lib/libglapi.so.*"]


@subpackage("mesa-gbm-libs")
def _(self):
    self.pkgdesc = "Generic Buffer Management"
    self.depends += [self.parent]
    # transitional
    self.provides = [self.with_pkgver("libgbm")]

    return [
        "usr/lib/gbm",
        "usr/lib/libgbm.so.*",
    ]


@subpackage("mesa-gbm-devel")
def _(self):
    self.pkgdesc = "Generic Buffer Management"
    # transitional
    self.provides = [self.with_pkgver("libgbm-devel")]

    return [
        "usr/include/gbm.h",
        "usr/lib/libgbm.so",
        "usr/lib/pkgconfig/gbm.pc",
    ]


@subpackage("mesa-osmesa-libs")
def _(self):
    self.pkgdesc = "Mesa off-screen interface"
    self.depends += [self.parent]
    # transitional
    self.provides = [self.with_pkgver("libosmesa")]

    return ["usr/lib/libOSMesa.so.*"]


@subpackage("mesa-gles1-libs")
def _(self):
    self.pkgdesc = "Free implementation of OpenGL ES 1.x API"
    self.depends += [self.parent]
    # transitional
    self.provides = [self.with_pkgver("libgles1")]

    return ["usr/lib/libGLESv1_CM.so.*"]


@subpackage("mesa-gles2-libs")
def _(self):
    self.pkgdesc = "Free implementation of OpenGL ES 2.x API"
    self.depends += [self.parent]
    # transitional
    self.provides = [self.with_pkgver("libgles2")]

    return ["usr/lib/libGLESv2.so.*"]


@subpackage("mesa-egl-libs")
def _(self):
    self.pkgdesc = "Free implementation of the EGL API"
    self.depends += [self.parent]
    # transitional
    self.provides = [self.with_pkgver("libegl")]

    return ["usr/lib/libEGL.so.*"]


@subpackage("mesa-gl-libs")
def _(self):
    self.pkgdesc = "Free implementation of the OpenGL API"
    self.depends += [self.parent]
    # transitional
    self.provides = [self.with_pkgver("libgl")]

    return ["usr/lib/libGL.so.*"]


@subpackage("mesa-xatracker-libs", _have_vmware)
def _(self):
    self.pkgdesc = "X acceleration library"
    self.depends += [self.parent]
    # transitional
    self.provides = [self.with_pkgver("libxatracker")]

    return ["usr/lib/libxatracker*.so.*"]


@subpackage("mesa-gallium-nine", _have_nine)
def _(self):
    self.pkgdesc = "Mesa implementation of D3D9"
    self.depends += [self.parent]

    return ["usr/lib/d3d"]


@subpackage("mesa-opencl", _have_opencl)
def _(self):
    self.pkgdesc = "Mesa implementation of OpenCL"
    self.depends += [self.parent, "libclc"]

    return [
        "etc/OpenCL",
        "usr/lib/gallium-pipe",
        "usr/lib/libMesaOpenCL.so.*",
        "usr/lib/libRusticlOpenCL.so.*",
    ]


@subpackage("mesa-libgallium")
def _(self):
    self.pkgdesc = "Mesa gallium loader"
    self.depends += [self.parent]

    return ["usr/lib/libgallium-*.so"]


@subpackage("mesa-dri")
def _(self):
    self.pkgdesc = "Mesa DRI drivers"
    self.depends += [self.parent]
    self.install_if = [self.parent]
    # transitional
    self.provides = [self.with_pkgver("mesa-vaapi")]

    return ["usr/lib/dri"]


@subpackage("mesa-vulkan", _have_vulkan)
def _(self):
    self.pkgdesc = "Mesa Vulkan drivers"
    self.depends += [self.parent]
    self.install_if = [self.with_pkgver("mesa-dri"), "vulkan-loader"]

    return [
        "usr/bin/mesa-overlay-control.py",
        "usr/lib/libvulkan_*.so",
        "usr/lib/libVkLayer_*.so",
        "usr/share/drirc.d/00-radv-defaults.conf",
        "usr/share/vulkan/explicit_layer.d/VkLayer_*.json",
        "usr/share/vulkan/implicit_layer.d/VkLayer_*.json",
        "usr/share/vulkan/icd.d/*_icd*.json",
    ]


@subpackage("mesa-devel")
def _(self):
    self.depends += [self.parent, self.with_pkgver("mesa-gbm-devel")]

    return self.default_devel()
